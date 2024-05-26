# Better Together Resources

<h2>Resources</h2>

There are three resources in this github repository:

<ol>
  <li><a href="https://github.com/petervickers/TimeCite">TimeCite Benchmark</a>: A classification task for
  predicting whether paper <i>a</i> cites paper <i>b</i>.  The system
  is given as input a pair of papers that are 1-4 hops apart in the
  citation graph.  The system is asked to distinguish positives
  (1-hop) from negatives (2-4 hops).  In addition, the papers in S2
  are assigned to a time bin (0-99).  The system should train on
  papers in bins 0 through bin <i>t</i> and test on bin <i>t+h</i>,
  where <i>h</i> is the forecasting horizon.  For the test set, each
  pair, <i>a,b</i> is assigned to max(bin(<i>a</i>), bin(<i>b</i>)).
    <p>The first figure below trains ProNE on 50 bins.  Note that performance degrades with <i>h</i> (forecasting further into the future).</p>
    <p>The second figure below shows that larger graphs favor ProNE.  Many benchmarks evaluate systems on a single graph, but we should be interested in how performance scales with the size of the input.  Graph-based (GB) methods based on citations (ProNE) scale differently than Content-based Filtering (CBF) methods based on abstracts (Specter).</p>
  </li>

  <li><a href="documentation/bulk_download.md">Embeddings</a>: ProNE-s, Specter2, SciNCL, GNNs</li>

  <li><a href="documentation/api.md">APIs</a>: Easy-to-Use tools based on <a href="https://api.semanticscholar.org/api-docs/">Semantic Scholar (S2) APIs</a>, but extended to include additional recommendation engines and embeddings.</li>

</ol>

<img src="figures/train_on_50_bins.pdf" alt="Train on 50 Bins" width="300">
<img src="figures/crossover.pdf" alt="Crossover" width="300">

<h2>Installation</h2>

```sh
pip install -r requirements.txt
```


<h2>Obtaining Secrets</h2>

It is not necessary to have a key from semantic scholar to use our APIs, but it is recommended.  You can obtain a key from <a href="https://www.semanticscholar.org/product/api#api-key">here</a>.

<p>
VecML keys can be obtained from  <a href="www.vecml.com">here</a>.  Click on login -> API Key.
</p>

<p>Create an (optional) file in $HOME/.secrets.json containing this:</p>


```sh
{"s2_apikeys" : [ ** insert zero or more semantic scholar api keys here ** ], 
"vecml_apikeys" : [ ** insert zero or more vecml api keys here ** ] }
```

<h2>Running APIs on the Local Host</h2>

It is not necessary to create a local host.  If you want to run these APIs on our host, please go <a href="http://34.204.188.58//similar_documentation.html#APIs">here</a>.

<p>
To start the web server

```sh
cd ** directory containing this README.md file **
python3 -m http.server --cgi
```

Then you should be able run these examples on the local host.

<p>
  To test server, click <a href="http://0.0.0.0:8000/cgi-bin/api/hello.py">here</a>  You should see "hello world" if the server is running.
  <p>
If you see "hello world," then try these <a href="documentation/api.md">examples</a>.
    
