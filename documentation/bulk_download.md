# Bulk Downloads of Precomputed embeddings

There are several large embeddings that you can download <a href="embeddings">here</a>.  That file contains
the following subdirectories:
<table border="1">
  <tr><th>Subdirectory</th> <th>Papers (N)</th><th>Dimensions (K)</th><th>Size of embedding.f</th></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/ProNE-s">ProNE-s</a></td><td>112M</td><td>280</td><td>125GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/Specter2">Specter2</a></td><td>119M</td><td>768</td><td>365GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/SciNCL">SciNCL</a></td><td>90M</td><td>768</td><td>279GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/GNN">GNN</a></td><td>99M</td><td>200</td><td>79GB</td></tr>
</table>

This README file explains what you can do with those subdirectories.
<p>

There are also some embeddings for a few ProNE-s models trained on subgraphs:

<table border="1">
  <tr><th>Subdirectory</th> <th>Papers (N)</th><th>Dimensions (K)</th><th>Size of embedding.f</th></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/ProNE-s/bins/010">ProNE-s (bin 10)</a></td><td>8M</td><td>280</td><td>9GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/ProNE-s/bins/020">ProNE-s (bin 20)</a></td><td>19M</td><td>280</td><td>21GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/ProNE-s/bins/030">ProNE-s (bin 30)</a></td><td>29M</td><td>280</td><td>32GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/ProNE-s/bins/040">ProNE-s (bin 40)</a></td><td>39M</td><td>280</td><td>44GB</td></tr>
  <tr><td><a href="http://34.204.188.58/files/embeddings/ProNE-s/bins/050">ProNE-s (bin 50)</a></td><td>49M</td><td>280</td><td>55GB</td></tr>
</table>

It is assumed that each of these directories contain the following files:
<ol>
  <li>embedding.f: a sequence of N by K floats, where N is the number of nodes (papers) in the embedding, and K is the number of hidden dimensions</li>
  <li>record_size: defines a few configuration variables such as K (number of hidden dimensions) and B (number of random bytes in approximate neareast neighbors)</li>
  <li>record_size.sh: similar to above</li>
  <li>map.old_to_new.i: mappings between corpus ids (old) and offsets into embedding.f (new)</li>
  <li>map.new_to_old.i: inverse of above</li>
  <li>indexing files for approximate nearest neighbors
    <ol>
      <li>old version
	<ol>
	  <li>idx.*.i: permutation of N, used in .  Papers that are near one another in the permutation should have large cosines.</li>
	  <li>idx.*.i.inv: inverse of above</li>
	</ol>
      </li>
      <li>new version
	<ol>
	  <li>landmarks.i
	  <li>postings.i</li>
	  <li>postings.idx.i</li>
	</ol>
      </li>
    </ol>
</ol>

See <a href="http://34.204.188.58/similar_documentation.html">here</a> for documentation on an API that provides convenient access to pieces of these embeddings.
<p>
Consider this example:
<ol>
  <li>Find the id for a paper from (part of) its title with <a href="../cgi-bin/paper_search?query=Personalizing%20Search%20via%20Association">this</a></li>
  <li>Use that id Recommend papers with:
    <ol>
      <li><a href="http://34.204.188.58//cgi-bin/recommend_papers?id=CorpusId:316030&method=s2_api&fields=citationCount,externalIds,title&score1=ProNE,Specter">a recommendation API from Semantic Scholar (S2)</a></li>
      <li><a href="http://34.204.188.58//cgi-bin/recommend_papers?id=CorpusId:316030&method=ProNE&fields=citationCount,externalIds,title&score1=ProNE,Specter">ProNE</a></li>
      </ol>
</ol>

The links above show that the top recommendation for 316030 is 47066000 by the S2 API, and 6496359 by ProNE-s.
<p>
  The code below shows how to get cosine scores for these pairs by the embeddings in this directory.  The code in the src directory is intended to illustrate how to memory map these embeddings into Python.  It should be easy to modify that code to get vectors.
<p>
    Note: when a vector is missing, the cosine is -1.

```sh
for dir in embeddings/*
do
echo $dir
echo '316030    47066000' | python src/simple_pairs_to_cos.py --dir $dir
done

for dir in embeddings/*
do
echo $dir
echo '316030    6496359' | python src/simple_pairs_to_cos.py --dir $dir
done
```
    
The following is like above but for several ProNE-s models.

```sh
for dir in embeddings/ProNE-s/bins/0?? embeddings/ProNE-s
do
echo $dir
echo '316030    47066000' | python src/simple_pairs_to_cos.py --dir $dir
done

for dir in embeddings/ProNE-s/bins/0?? embeddings/ProNE-s
do
echo $dir
echo '316030    6496359' | python src/simple_pairs_to_cos.py --dir $dir
done
```
    

The input are a pair of corpus ids from Semantic Scholar.  See <a href="src">here</a> for the code; it shows how to compute cosine similarities for pairs of corpus ids using several different embeddings.

<p>
  The following implements the approximate nearest neighbor search.  The Python program, src/near.py, inputs a corpus id and outputs topN corpus ids.  The code assumes the --dir argument contains several indexing files named postings.* and landmarks.*.
  These indexing files are available for ProNE-s and Specter2, but not for SciNCL and GNN.  

```sh
echo 316030 | src/near.py --dir embeddings/ProNE-s --topN 5
echo 316030 | src/near.py --dir embeddings/Specter2 --topN 5
```

