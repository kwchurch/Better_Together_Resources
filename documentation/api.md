<html>
  <body>

<h2 id="APIs">APIs</h2>

<b><i>NOTE</i></b>: The links in the table below assume that you are running these APIs on your local machine.  To do that, you will
need to follow the instructions in the <a href="../README.md">README</a>.  If you want to run these examples on our server, please go <a href="http://34.204.188.58//similar_documentation.html#APIs">here</a>.
<p>

The following APIs return json objects:
<p>
<table border="1">
<tr><th align="left">API</th><th align="left">Examples</th><th align="left">Arguments</th><th align="left" width="50%">Description</th></tr>

<tr><td id="paper_search">Paper Search</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/paper_search?query=Word%20Association">example</a></td>
  <td><a href="#help">help</a>, <a href="#query">query</a>, <a href="#paper_fields">fields</a></td>
  <td>
    <ul>
      <li>Find papers matching input <a href="#query">query</a> (a string); output <a href="#paper_fields">fields</a> from S2 for each paper.</li>
      <li>See documentation on <a href="#paper_fields">fields</a> for more information on fields in S2.</li>
      <li>A common use case is to request paper <a href="#paper_id">id</a>s from titles of papers since many of the APIs below are based on ids in Semantic Scholar (and other sources).</li>
    </ul>
  </td>
</tr>

<tr><td id="author_search">Author Search</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/author_search?query=Kenneth+Church">example</a></td>
  <td><a href="#help">help</a>, <a href="#query">query</a>, <a href="#author_fields">fields</a></td>
  <td>
    <ul>
      <li>Find authors matching input <a href="#query">query</a> (a string); output <a href="#author_fields">fields</a> from S2 for each author.</li>
      <li>See documentation on <a href="#author_fields">fields</a> for more information on fields in S2.</li>
      <li>Note: author <a href="#author_fields">fields</a> are different from paper <a href="#paper_fields">fields</a>.</li>
    </ul>
</td></tr>

<tr><td id="lookup_paper">Lookup Paper</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=title&embeddings=prone">simple example</a>,
    <br>
<a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157,CorpusId:9558665&fields=title,authors,year,citationCount,referenceCount,externalIds,citations&embeddings=prone,s2_api,specter">more challenging example</a></td>
  <td><a href="#help">help</a>, <a href="#paper_id">id</a>, <a href="#paper_fields">fields</a>, <a href="#embeddings">embeddings</a></td>
  <td>
    <ul>
      <li>Input one or more comma separated paper <a href="#paper_id">id</a> and output <a href="#paper_fields">fields</a> from S2, as well as embeddings.</li>
      <li>If <a href="#embeddings">embeddings</a> argument is specified,
      then output embedding vectors for each input paper (missing
      values will have vectors of 0).
      </li>
    <li>See documentation on <a href="#embeddings">embeddings</a> for details on how to specify combinations of different embeddings to return.</li>
    </ul>
  </td>
</tr>

<tr><td id="lookup_author">Lookup Author</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=papers.venue,papers.citationStyles,papers.s2FieldsOfStudy,name,authorId,citationCount,paperCount,hIndex,papers.title,papers.citationCount,papers.authors">example</a></td>
  <td><a href="#help">help</a>, <a href="#author_id">id</a>, <a href="#Fields">fields</a></td>
  <td>
    <ul>
      <li>Input author <a href="#author_id">id</a> and output author <a href="#author_fields">fields</a> from S2.</li>
      <li>Note: author <a href="#author_id">ids</a> are different from paper <a href="#paper_id">ids</a>
      and author <a href="#author_fields">fields</a> are different from paper <a href="#paper_fields">fields</a>.</li>
    </ul>
  </td>
</tr>

<tr><td id="lookup_citations">Lookup Citations</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/lookup_citations?id=CorpusId:9558665&offset=200&limit=100&fields=contexts,citationCount,referenceCount,title,authors">example</a></td>
  <td><a href="#help">help</a>, <a href="#offset">offset</a> (defaults to 0), <a href="#limit">limit</a> (defaults to 100; max is 1000), <a href="#paper_id">id</a>, <a href="#citation_fields">fields</a></td>
  <td>
    <ul>
      <li>Lookup Citations for paper <a href="#paper_id">id</a> and output <a href="#citation_fields">fields</a> from S2 for each citation.</li>
      <li>A useful field to request is contexts; that field returns citing sentences, sentences from other papers that cite the input paper <a href="#paper_id">id</a>.</li>
      <li>For papers with more than 1000 citations, call this API multiple times with different offsets.</li>
    </ul>
  </td>
</tr>

<tr><td id="coauthors">Coauthors</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/coauthors?query=Kenneth+Church&after_year=2020">example</a></td>
  <td><a href="#help">help</a>, <a href="#query">query</a>,
  after_year</td>
  <td>
    <ul>
      <li>Input <a href="#query">query</a> (a string); for each matching author ids, returns a list of coauthors filtered by after_year (a 4 digit number).</li>
      <li>Note: since Semantic Scholar may have multiple author
	ids for the same author, the json object contains a list of
	coauthors for each author matching the
	input <a href="#query">query</a></li>
    </ul>
  </td>
</tr>

<tr><td id="recommend papers">Recommend Papers</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=ProNE&fields=citationCount,externalIds">example</a></td>
  <td><a href="#help">help</a>, <a href="#paper_id">id</a>, <a href="#limit">limit</a>, <a href="#method">method</a>, <a href="#paper_fields">fields</a>,
  sort_by, <a href="#score1">score1</a>, <a href="#score2">score2</a></td>
  <td>
    <ul>
      <li>Recommend papers similar to paper <a href="#paper_id">id</a>
	using <a href="#method">method</a>.</li>
      <li>See documentation on <a href="#method">method</a> for choices
	of methods that are currently supported.</li>
      <li>Output <a href="#paper_fields">fields</a> from
	S2 for each recommended paper.</li>
      <li>The optional arguments, <a href="#score1">score1</a>
	and <a href="#score2">score2</a>, score recommendations one at a
	time (for score1) and pairwise (for score2), using one or more of
	four embeddings.</li>
    </ul>
</td>
</tr>

<tr><td id="recommend_authors">Recommend Authors</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/recommend_authors?id=CorpusId:9558665&method=ProNE&fields=citationCount,externalIds">example</a></td>
  <td><a href="#help">help</a>, <a href="#paper_id">id</a>, <a href="#limit">limit</a>, <a href="#method">method</a>, <a href="#paper_fields">fields</a>, sort_by, <a href="#score1">score1</a>, <a href="#score2">score2</a></td>
  <td>
    <ul>
      <li>Recommend authors near paper <a href="#paper_id">id</a>
	using <a href="#method">method</a></li>
      <li>Output <a href="#author_fields">fields</a> from S2 for each recommended
	author.</li>
    </ul>
</td>
</tr>

<tr><td id="compare_and_contrast">Compare and Contrast</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/compare_and_contrast?ids=CorpusId:10491450,CorpusId:29970479">example1</a>
<br>
<a href="http://0.0.0.0:8000//cgi-bin/api/compare_and_contrast?ids=c129e8025fffa065edb5b27dd7c2269abc0a138b,CorpusId:2640788">example2</a>
<br>
    <a href="http://0.0.0.0:8000//cgi-bin/api/compare_and_contrast?ids=ACL:P89-1010,ACL:P98-2127">example2</a>

</td>
  <td><a href="#help">help</a>, ids (two or more <a href="#paper_id">id</a>s, separated by commas)</td>
<td>
  <ul>
    <li>Use <a href="https://arxiv.org/abs/2005.11401">RAG</a> to compare and contrast the first <a href="#paper_id">id</a> with the rest.</li>
  </ul>
</td>
</tr>

<tr><td id="compare_and_contrast_tests">Compare and Contrast Texts</td>
  <td><a href="http://0.0.0.0:8000//cgi-bin/api/compare_and_contrast_texts?text1=I love you.&text2=I hate you.">example</a>
</td>
  <td><a href="#help">help</a>, text1, text2</td>
  <td>
    <ul>
      <li>Use <a href="https://arxiv.org/abs/2005.11401">RAG</a> to compare and contrast text1 with text2, where both texts are strings.</li>
    </ul>
</td>
</tr>
</table>


<h3>Arguments</h3>

<ol>
  <li id="help">help: return short documentation</li>
  <li id="query">query: input string</li>
  <li id="paper_id">id: input for lookup_paper, recommendations and lookup_citations; many of the externalId formats are supported, including:
    <ol>
      <li>sha (40 byte hex); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=ea7886975510353c194303931b333af983a63ed7&fields=title,authors,citationCount,externalIds">example</a></li>
      <li>CorpusId (the primary key in Semantic Scholar); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10491450&fields=title,authors,citationCount,externalIds">example</a></li>
      <li>PMID (pubmed ids); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=title,authors,citationCount,externalIds">example</a></li>
      <li>ACL (<a href="https://aclanthology.org/">acl anthology</a> ids); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=ACL:2022.lrec-1.676&fields=title,authors,citationCount,externalIds">example</a></li>
      <li><a href="https://arxiv.org/">arXiv</a>; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=arXiv:2111.03628&fields=title,authors,citationCount,externalIds">example</a></li>
      <li>MAG (<a href="https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/">Microsoft Academic Graph</a>); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=MAG:3167354871&fields=title,authors,citationCount,externalIds">example</a></li>
      </ol></li>
  <li id="author_id">id: input for lookup_author (Note: author ids are different from <a href="#paper_id">paper ids</a>)</li>
  <li id="offset">offset: start of papers to return (defaults to 0)</li>
  <li id="limit">limit: number of results to return</li>
  <li><a href="#Fields">fields</a>: one or more comma separated values.  Many values are supported including title, authors, publication year, bibtex entries, references, citations, citing sentences and much more (see discussion <a href="#Fields">below</a>)</li>
  <li id="method">method (for generating recommendations); method should be one of the following (comma separated values and case insensitive):
    <ol>
      <li>combined: <a href="cgi-bin/recommend_papers?id=CorpusId:10491450&method=combined&fields=title">example</a> (a fast precomputed combination of ProNE and Specter)</li>
        <li>ProNE: <a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=prone&fields=title">example</a></li>
      <li>Specter: <a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=specter&fields=title">example</a></li>
      <li>s2_api: <a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=s2_api&fields=title">example</a></li>
      <li>pubmed_api: <a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=pubmed_api&fields=title">example</a></li>
      </ol>
    The first two, ProNE and Specter, use cached embeddings to generate recommendations.  The last two generate recommendations from Semantic Scholar (S2) and PubMed, respectively
</li>

  <li id="embeddings">Embeddings (for lookup paper); one or more of the following (comma separated values and case insensitive):
    <ol>
      <li>ProNE: <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10491450&embeddings=prone&fields=title">example</a></li>
      <li>Specter: <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10491450&embeddings=specter&fields=title">example</a></li>
      <li>SciNCL: <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10491450&embeddings=SciNCL&fields=title">example</a></li>
      <li>GNN: <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10491450&embeddings=gnn&fields=title">example</a></li>
      <li>s2_api: <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10491450&embeddings=s2_api&fields=title">example</a></li>
      </ol>
    
    The first four ProNE, Specter and GNN, use cached vectors.  The last one, s2_api, uses an API from Semantic Scholar to return the most recent values.
    Specter and s2_api should return the same vectors, as long as the Specter vector is not missing.
    There will be one vector for each input paper.  Vectors of zeros are returned for missing values.
</li>
  
prone, scincl, specter, gnn, s2_api (case insensitive).

  <li id="score1">score1: outputs 1d vectors of cosine scores between each recommendation.  The value of score1 is a (case insensitive) comma separated list of embeddings: ProNE, Specter, SciNCL, GNN; <a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=ProNE&score1=prone,specter,gnn,scincl">example</a>. 
    <br>Note: missing values will have cosines of 0</li>
<li id="score2">score2: outputs pairwise cosine scores between each
pair recommendations.  The value of score2 is a (case insensitive)
comma separated list of embeddings: ProNE, Specter, SciNCL, GNN comma
separated list of embeddings (pairwise cosines of
  recommendations); <a href="http://0.0.0.0:8000//cgi-bin/api/recommend_papers?id=CorpusId:10491450&method=ProNE&score2=prone,specter,gnn,scincl">example</a>.
  <br>
Note: missing values will have cosines of 0</li>
  </ol>

<h3 id="Fields">Fields</h3>

Fields are based on Semantic Scholar APIs; see <a href="https://api.semanticscholar.org/api-docs/">here</a> for their documentation.

Some useful values are shown below (with separate lists for <a href="#paper_fields">papers</a>, <a href="#author_fields">authors</a> and <a href="#citation_fields">citations</a>).  Fields is set to a comma separated list such as fields=title,authors.

<ol>
  <li id="paper_fields">Fields for papers:  
    <ol>
      <li>externalIds (outputs one or more of the following ids from the 8 sources behind Semantic Scholar)
	<ol>
	  <li>CorpusId (the primary key for Semantic Scholar); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:172192617&fields=externalIds">example</a></li>
	  <li>MAG (Microsoft Academic Graph); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:172192617&fields=externalIds">example</a></li>
	  <li>DOI; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:10350567&fields=externalIds">example</a></li>
	  <li>PubMed; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=externalIds">example</a></li>
	  <li>PubMedCentral; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:38265596&fields=externalIds">example</a></li>
	  <li>DBLP; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:207417927&fields=externalIds">example</a></li>
	  <li>arXiv; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:209531806&fields=externalIds">example</a></li>
	  <li>ACL; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:18807392&fields=externalIds">example</a></li>
	</ol>
      </li>
      <li>url (pointer into Semantic Scholar); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=url">example</a></li>
      <li>title (of paper); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=title">example</a></li>
      <li>abstract; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=abstract">example</a></li>
      <li>tldr; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=tldr">example</a></li>
      <li>authors; you can request a list of author objects and/or specific fields from the author objects:
	<ol>
	  <li>authors (list of author objects); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=authors">example</a></li>
	  <li>authors.name (list of author names); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=authors.name">example</a></li>
	  <li>authors.authorId (list of author ids); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=authors.authorId">example</a></li>
	</ol>
      </li>
      <li>year; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=year">example</a></li>
      <li>venue; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=venue">example</a></li>
      <li>citationStyles; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=citationStyles">example</a> (outputs bibtex entries)</li>
      <li>referenceCount; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=referenceCount">example</a></li>
      <li>citationCount; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=citationCount">example</a></li>
      <li>openAccessPdf (pointer to PDF file, if known); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=CorpusId:18807392&fields=openAccessPdf">example</a></li>
      <li>fieldsOfStudy (probably from MAG); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=fieldsOfStudy">example</a></li>
      <li>s2FieldsOfStudy (like fieldsOfStudy, but from Semantic Scholar); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=s2FieldsOfStudy">example</a></li>
      <li>embedding.specter_v2 (vector of 768 floats based on an encoding of the title and abstract using a BERT-like model); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=embedding.specter_v2">example</a></li>
      <li>citations (list of papers that cite this paper); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=citations">example</a>
	<ol>
	  <li>citations.title; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=citations.title">example</a></li>
	  <li>citations.authors; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=citations.authors">example</a></li>
	  <li>citations.citationCount; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=citations.citationCount">example</a></li>
	  <li>citations.<i>xyz</i> where <i>xyz</i> is authors, citationCount and most other <a href="#paper_fields">paper fields</a></li>
	</ol>
      </li>
      <li>references; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=references">example</a>
	<ol>
	  <li>references.title; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=references.title">example</a></li>
	  <li>references.authors; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=references.authors">example</a></li>
	  <li>references.citationCount; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_paper?id=PMID:24335157&fields=references.citationCount">example</a></li>
	  <li>references.<i>xyz</i> where <i>xyz</i> is authors, citationCount and most other <a href="#paper_fields">paper fields</a></li>
	</ol>
      </li>
  </ol>
  </li>
  <li id="author_fields">Fields for authors:
    <ol>
      <li>authorId; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=authorId">example</a></li>
      <li>externalIds; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=externalIds">example</a></li>
      <li>url; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=url">example</a></li>
      <li>name; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=name">example</a></li>
      <li>affiliations; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=affiliations">example</a></li>
      <li>homepage; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=homepage">example</a></li>
      <li>paperCount; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=paperCount">example</a></li>
      <li>hIndex; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=hIndex">example</a></li>
      <li>citationCount; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=citationCount">example</a></li>
      <li>papers (list of papers); <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=papers">example</a>
	<ol>
	  <li>papers.title; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=papers">example</a></li>
	  <li>papers.externalIds; <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_author?id=2244184&fields=papers.externalIds">example</a></li>
	  <li>papers.<i>xyz</i> where <i>xyz</i> is authors, citationCount and most other <a href="#paper_fields">paper fields</a></li>
	</ol>
      </li>
    </ol>
  <li id="citation_fields">Fields for citations:
    <ol>
      <li>contexts (citing sentences): <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_citations?id=CorpusId:9558665&fields=contexts">example</a></li>
      <li>intents: <a href="http://0.0.0.0:8000//cgi-bin/api/lookup_citations?id=CorpusId:9558665&fields=intents">example</a></li>
      <li><i>xyz</i> where <i>xyz</i> is authors, citationCount and most other <a href="#paper_fields">paper fields</a></li>
    </ol>
  </li>
</ol>

<h2 id="Quick_Tour">Quick Tour</h2>
<h3>Specifying Input Documents</h3>
Many inputs are supported.  The simplest case is a corpus id from Semantic Scholar:

<ol>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?CorpusId=3051291">similar?CorpusId=3051291</a></li>
</ol>

Search, query and author are also supported:

<ol>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?search=deepwalk">similar?search=deepwalk</a></li>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?query=deepwalk">similar?query=deepwalk</a></li>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?author=Povey&limit=10">similar?author=Povey&limit=10</a></li>
</ol>

All of these use APIs from Semantic Scholar.  Query uses autocomplete, and Search uses another method from Semantic Scholar
for mapping strings to one or more corpus ids.  Author maps strings to author ids.  For each author id,
we list a number of papers sorted by citations, with links to find similar papers for each of them.
<p>

<h3>Specifying Embeddings</h3>
There is an embedding option.  Four values are currently supported: specter, specter2, scincl and proposed [default].
  <ol> 
      <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?CorpusId=3051291&embedding=specter">embedding=specter</a></li>
      <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?CorpusId=3051291&embedding=specter2">embedding=specter2</a></li>
      <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?CorpusId=3051291&embedding=scincl">embedding=scincl</a></li>
      <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?CorpusId=3051291&embedding=proposed">embedding=proposed</a></li>
</ol>

<h3>Json Output</h3>
  
Example:
<ol>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?query=deepwalk">similar?query=deepwalk</a></li>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?query=deepwalk&output_mode=json">similar?query=deepwalk&output_mode=json</a> Same as above, but outputs json</li>
</ol>

<h3>limit</h3>

Most of the commands above take a limit option [default=50]
<ol>
  <li><a href="http://0.0.0.0:8000//cgi-bin/api/similar?author=Povey&limit=10">similar?author=Povey&limit=10</a></li>
</ol>

  </body>
</html>
