# BFS Distances Weighted Graph
<div class="markdown"><p>It's vacation time! Luckily, a nationwide network of Hyperloop tunnels has just been built, so all you have to do is find the lowest cost route to your destination.</p>
<p><strong>Example</strong><br>
For <code>city1 = "Los Angeles"</code>, <code>city2 = "San Francisco"</code> and</p>
<pre><code>tunnels = [
  ["Los Angeles","San Francisco","1000"],
  ["Los Angeles","Fresno","150"],
  ["Fresno","San Francisco","300"]
]
</code></pre>
<p>the output should be<br>
<code>hyperloop(city1, city2, tunnels) = 450</code>.</p>
<p>For this case, there are <code>2</code> options for a trip from LA to San Francisco. The first option is a direct trip costing <code>1000</code>.  The second option is a trip with one stop at Fresno costing <code>150 + 300 = 450</code>.  So, the lowest cost trip is <code>450</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string city1</strong></p>
<p>The city where the trip begins.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ city1.length &lt; 15</code>.</p>
</li>
<li>
<p><strong>[input] string city2</strong></p>
<p>The destination city.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ city2.length &lt; 15</code>.</p>
</li>
<li>
<p><strong>[input] array.array.string tunnels</strong></p>
<p>The list of one-way tunnels between <code>2</code> cities.  Each tunnel is an array of <code>3</code> strings: <code>tunnels[i][0]</code> is the city at the beginning of the tunnel, <code>tunnels[i][1]</code> is the city at the end of the tunnel, and <code>tunnels[i][2]</code> is the cost of the trip for the tunnel.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 &lt; tunnels.length &lt; 50</code>,<br>
<code>tunnels[i].length = 3</code>,<br>
<code>2 ≤ tunnels[i][0].length &lt; 15</code>,<br>
<code>2 ≤ tunnels[i][1].length &lt; 15</code>,<br>
<code>0 ≤ int(tunnels[i][2]) &lt; 1500</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The lowest possible cost of a trip from <code>city1</code> to <code>city2</code></p>
</li>
</ul>
</div>
# Reference

[গ্রাফ থিওরিতে হাতেখড়ি-৯ (ডায়াক্সট্রা)](http://www.shafaetsplanet.com/planetcoding/?p=1500) 
