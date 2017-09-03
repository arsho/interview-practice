# BFS Distances Unweighted Graph
<div class="markdown"><p>Given the <a href="keyword://adjacency-matrix-unweighted">adjacency matrix</a> of the <em>connected undirected</em> graph with <em>no loops or multiple edges</em> and the index of the start vertex, find the distances between the start vertex and each vertex of the graph.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>matrix = [[false, false, true],
          [false, false, true],
          [true, true, false]]
</code></pre>
<p>and <code>startVertex = 0</code>, the output should be<br>
<code>bfsDistancesUnweightedGraph(matrix, startVertex) = [0, 2, 1]</code>.</p>
<p>Here's what the given graph looks like:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/bfsDistancesUnweightedGraph/img/example.png?_tm=1490625581317" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.boolean matrix</strong></p>
<p><em>Adjacency matrix</em> of the given graph.</p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ matrix.length ≤ 10</code>,<br>
<code>matrix[i].length = matrix.length</code>.</p>
</li>
<li>
<p><strong>[input] integer startVertex</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ startVertex ≤ matrix.length - 1</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array of distances between the start vertex and each vertex of the graph.</p>
</li>
</ul>
</div>

# Reference

[গ্রাফ থিওরিতে হাতেখড়ি-৪(ব্রেডথ ফার্স্ট সার্চ)](http://www.shafaetsplanet.com/planetcoding/?p=604) 
