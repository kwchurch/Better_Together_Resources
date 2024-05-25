#!/usr/bin/env python

import json,requests,argparse
import os,sys,argparse,time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pdb

t0 = time.time()

# print('id_to_floats: ' + str(sys.argv), file=sys.stderr)

apikey=os.environ.get('SPECTER_API_KEY')

# assumes the dir argument contains
#   embedding.f  sequence of N by K floats32
#   map.old_to_new.i  sequence of N int32
#   record_size  specifies K

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="a directory such as $proposed or $specter", required=True)
parser.add_argument("-V", '--verbose', action='store_true')
parser.add_argument('--no_map', action='store_true')
parser.add_argument('--skip_cos', action='store_true')
parser.add_argument('--binary_output', default=None)
parser.add_argument('--topN', type=int, default=10)
parser.add_argument('--pad_factor', type=int, default=3)
parser.add_argument('--limit', type=int, default=1000000)
parser.add_argument('--landmarks_dir', default='')
parser.add_argument("--use_references", help="never|always|when_necessary", default="never")
parser.add_argument("-G", "--graph", help="file (without .X.i and .Y.i)", default=None)

args = parser.parse_args()

if args.no_map:
    assert args.use_references == 'never', 'with --no_map option, please use --use_references == "never"'

def map_int64(fn):
    fn_len = os.path.getsize(fn)
    return np.memmap(fn, dtype=np.int64, shape=(int(fn_len/8)), mode='r')

def map_int32(fn):
    fn_len = os.path.getsize(fn)
    return np.memmap(fn, dtype=np.int32, shape=(int(fn_len/4)), mode='r')

Y = idx = None

if not args.graph is None:
    Y = map_int32(args.graph + '.Y.i')

    if not os.path.exists(args.graph + '.X.i.idx'):
        print('%0.0f sec: computing idx' % (time.time() - t0), file=sys.stderr)
        sys.stderr.flush()
        X = map_int32(args.graph + '.X.i')
        res = np.cumsum(np.bincount(X))
        res.tofile(args.graph + '.X.i.idx')
        print('%0.0f sec: idx computed' % (time.time() - t0), file=sys.stderr)
        sys.stderr.flush()

    idx = map_int64(args.graph + '.X.i.idx')

def extract_row(x):
    # print('extract_row: ' + str(x))
    if x >= len(idx) or x < 0:
        return []
    if x == 0:
        return Y[:idx[0]]
    else:
        return Y[idx[x-1]:idx[x]]

def my_int(s):
    for i,c in enumerate(s):
        if not c.isdigit():
            return int(s[0:i])

def record_size_from_dir(dir):
    with open(dir + '/record_size', 'r') as fd:
        return my_int(fd.read())

def map_from_dir(dir):
    fn = dir + '/map.old_to_new.i'
    fn_len = os.path.getsize(fn)
    return np.memmap(fn, dtype=np.int32, shape=(int(fn_len/4)), mode='r')

def imap_from_dir(dir):
    fn = dir + '/map.new_to_old.i'
    fn_len = os.path.getsize(fn)
    return np.memmap(fn, dtype=np.int32, shape=(int(fn_len/4)), mode='r')

def embedding_from_dir(dir, K):
    fn = dir + '/embedding.f'
    fn_len = os.path.getsize(fn)
    return np.memmap(fn, dtype=np.float32, shape=(int(fn_len/(4*K)), K), mode='r')

def postings_from_dir(dir):
    fn = dir + args.landmarks_dir + '/landmarks.i'
    fn_len = os.path.getsize(fn)
    number_of_landmarks = int(fn_len/os.path.getsize(dir + '/map.new_to_old.i'))
    landmarks = np.memmap(fn,
                          shape=(int(fn_len/(number_of_landmarks*4)),
                                 number_of_landmarks),  
                          dtype=np.int32, mode='r')
    fn = dir + args.landmarks_dir + '/postings.i'
    assert os.path.exists(fn), str(fn) + ' does not exist'
    fn_len = os.path.getsize(fn)
    postings = np.memmap(fn, shape=(int(fn_len/4)),  dtype=np.int32, mode='r')

    fn = dir + args.landmarks_dir + '/postings.idx.i'
    assert os.path.exists(fn), str(fn) + ' does not exist'
    fn_len = os.path.getsize(fn)
    postings_idx = np.memmap(fn, shape=(int(fn_len/8)),  dtype=int, mode='r')

    return { 'landmarks' : landmarks,
             'postings' : postings,
             'postings_idx' : postings_idx }

def directory_to_config(dir):
    K = record_size_from_dir(dir)
    return { 'record_size' : K,
             'dir' : dir,
             'map' : {'old_to_new' : map_from_dir(dir),
                      'new_to_old' : imap_from_dir(dir)},
             'postings' : postings_from_dir(dir),
             'embedding' : embedding_from_dir(dir, K)}

config = directory_to_config(args.dir)

def get_postings(c):
    
    idx = config['postings']['postings_idx']

    if c == 0:
        start = 0
    else:
        start = idx[c-1]

    end = idx[c]
    res = config['postings']['postings'][start:end]
    return res

def my_cos(v1, v2):
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return (v1 @ v2.T)[0,0]/(n1 * n2)

def summarize_nears(nears):
    l = sum([len(n) for n in nears])
    res = np.zeros(l, dtype=np.int32)
    i=0    
    for n in nears:
        i2 = i + len(n)
        res[i:i2] = n
        i=i2
    return np.unique(res, return_counts=True)

if args.skip_cos:
    print('corpus_id1\tcorpus_id2\tintersections')
else:
    print('corpus_id1\tcorpus_id2\tcos\trank\tintersections')

for line in sys.stdin:
    fields = line.rstrip().split('\t')
    if len(fields) == 1:
        old_id = int(fields[0])
        new_id = -1
        if old_id >= 0 and old_id < len(config['map']['old_to_new']):
            new_id = config['map']['old_to_new'][old_id]
        classes = None
        if new_id >= 0 and new_id < len(config['postings']['landmarks']):
            classes = config['postings']['landmarks'][new_id,:].reshape(-1)
            if args.verbose: print('classes: ' + str(classes), file=sys.stderr)
            if classes[0] == classes[1]:
                classes = None
            if args.verbose:
                print('classes: ' + str(classes))
        if classes is None:
            print(fields[0] + '\tNA')
            continue
    elif len(fields) != 3: continue
    else:
        row = fields[0]
        if row == 'row': continue
        classes = fields[1].split('|')
        new_id = int(row)
        old_id = config['map']['new_to_old'][new_id]
    vec = config['embedding'][new_id,:].reshape(1,-1)

    nears = [get_postings(int(c)) for c in classes]

    summary_ids,summary_counts = summarize_nears(nears)

    c = np.bincount(summary_counts)
    cc = np.cumsum(c)
    
    N = np.sum(c)
    T = 0
    for i,x in enumerate(N - cc):
        if x > args.pad_factor*args.topN:
            T=i

    T = T+1
    s0 = summary_counts > T

    near0 = summary_ids[s0]
    inter0 = summary_counts[s0]

    shortfall = args.pad_factor*args.topN - len(near0)

    if shortfall > 0:
        s1 = summary_counts == T
        sum_s1 = sum(s1)
        
        if sum_s1 < shortfall:
            shortfall=s1

        near1 = summary_ids[s1][0:shortfall]
        near = np.append(near0, near1)

        inter1 = summary_counts[s1][0:shortfall]
        intersections = np.append(inter0, inter1)
    else:
        near = near0
        intersections = inter0

    o = config['map']['new_to_old'][near]

    if args.skip_cos:
        for oo,inter in zip(o, intersections):
            print('\t'.join(map(str, [old_id, oo, inter])))
    else:
        nvec = config['embedding'][near,:]
        s = cosine_similarity(vec,nvec)
        best = np.argsort(-s[0,:])
        if len(best) > args.topN:
            best = best[0:args.topN]
        for jj, oo,ss,inter in zip(np.arange(len(best)), o[best], s[0,:][best], intersections[best]):
            print('\t'.join(map(str, [old_id, oo, ss, jj, inter])))
    sys.stdout.flush()

print('%0.3f sec: near' % (time.time() - t0), file=sys.stderr)
