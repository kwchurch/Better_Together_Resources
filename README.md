# Better Together Resources

<h2>Resources</h2>

<ol>
  <li><a href="documentation/api.md">APIs</a></li>
  <li>Embeddings</li>
  <li>Citation Prediction Benchmark</li>
</ol>

<h2>Installation</h2>

```sh
pip install -r requirements.txt
```


<h2>Obtaining Secrets</h2>

It is not necessary to have a key from semantic scholar, but it is recommended.  You can obtain a key from <a href="https://www.semanticscholar.org/product/api#api-key">here</a>.

<p>
VecML keys can be obtained from  <a href="www.vecml.com">here</a>.  Click on login -> API Key.
</p>

<p>Create an (optional) file in $HOME/.secrets.json containing this:</p>


```sh
{"s2_apikeys" : [ ** insert zero or more semantic scholar api keys here ** ], 
"vecml_apikeys" : [ ** insert one or more vecml api keys here ** ] }
```

To start the web server

```sh
cd ** directory containing this README.md file **
python3 -m http.server --cgi
```

Then you should be able run these examples on the local host.

<h2>Examples</h2>

Test server.  You should see "hello world" if the server is running when you click <a href="http://0.0.0.0:8000/cgi-bin/api/hello.py">here</a>.

If you see "hello world," then try these <a href="documentation/api.md">examples</a>.
    
