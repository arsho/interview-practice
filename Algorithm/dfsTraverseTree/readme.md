# BFS Traverse Tree

<div class="markdown"><p><em>Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.</em></p>
<p>Given a binary tree of integers <code>t</code>, return its node values in the following format:</p>
<ul>
<li>The first element should be the value of the tree root;</li>
<li>The next elements should be the values of the nodes at height <code>1</code> (i.e. the root children), ordered from the leftmost to the rightmost one;</li>
<li>The elements after that should be the values of the nodes at height <code>2</code> (i.e. the children of the nodes at height <code>1</code>) ordered in the same way;</li>
<li>Etc.</li>
</ul>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
</code></pre>
<p>the output should be<br>
<code>traverseTree(t) = [1, 2, 4, 3, 5]</code>.</p>
<p>This <code>t</code> looks like this:</p>
<pre><code>     1
   /   \
  2     4
   \   /
    3 5
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] tree.integer t</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ tree size ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array that contains the values at <code>t</code>'s nodes, ordered as described above.</p>
</li>
</ul>
</div>

