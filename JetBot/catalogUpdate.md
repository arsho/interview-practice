# Catalog Update

<div class="markdown"><p>Jet.com customers can easily find the item they are looking for by browsing by category. Categories are stored in a catalog that is updated on a regular basis as inventory changes. Your goal is to implement an algorithm that updates the catalog with new items.</p>
<p>The <code>catalog</code> is given as a two-dimensional array. For each <code>i</code>, <code>catalog[i][0]</code> represents the name of the corresponding category, and <code>catalog[i][j]</code> for <code>j &gt; 0</code> is the name of some item within this category, which can also be the category of some other items. For each <code>i</code> all elements of <code>catalog[i]</code> except the first are sorted <a href="keyword://lexicographical-order-for-strings">lexicographically</a>, and <code>catalog</code> arrays are sorted <em>lexicographically</em> by their first elements. The name of the topmost directory is <code>"root"</code>.</p>
<p>Given a list of <code>updates</code>, update the <code>catalog</code> with the new items and return the result.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>catalog = [["Books", "Classics", "Fiction"],
           ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
           ["Grocery", "Beverages", "Snacks"],
           ["Snacks", "Chocolate", "Sweets"],
           ["root", "Books", "Electronics", "Grocery"]]
</code></pre>
<p>and</p>
<pre><code>updates = [["Snacks", "Marmalade"],
           ["Fiction", "Harry Potter"],
           ["root", "T-shirts"],
           ["T-shirts", "CodeFights"]]
</code></pre>
<p>the output should be</p>
<pre><code>catalogUpdate(catalog, updates) = [["Books", "Classics", "Fiction"],
                                   ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
                                   ["Fiction", "Harry Potter"],
                                   ["Grocery", "Beverages", "Snacks"],
                                   ["Snacks", "Chocolate", "Marmalade", "Sweets"],
                                   ["T-shirts", "CodeFights"],
                                   ["root", "Books", "Electronics", "Grocery", "T-shirts"]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.string catalog</strong></p>
<p>The initial catalog in the format described above. It is guaranteed that the catalog is correct, i.e. there are no duplicate elements, <code>category[i][0] = "root"</code> for some <code>i</code>, and for each <code>t ≠ i</code> <code>category[t][0]</code> is equal to exactly one <code>category[j][k]</code>, where <code>j ≠ t</code> and <code>k &gt; 0</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ catalog.length ≤ 10</code>,<br>
<code>2 ≤ catalog[i].length ≤ 5</code>,<br>
<code>1 ≤ catalog[i][j].length ≤ 45</code>.</p>
</li>
<li>
<p><strong>[input] array.array.string updates</strong></p>
<p>Array of updates. Each update is a two-element array in the format <code>[&lt;parent_category&gt;, &lt;item_name&gt;]</code>, where <code>&lt;parent_category&gt;</code> is the name of the category the item belongs to, and <code>&lt;item_name&gt;</code> is the item name.<br>
The elements of <code>update</code> should be considered in the order they are given.<br>
It is guaranteed that <code>&lt;parent_category&gt;</code> is always present in the catalog at the time the corresponding update is made.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ updates.length ≤ 15</code>,<br>
<code>2 ≤ updates[i].length ≤ 2</code>,<br>
<code>3 ≤ updates[i][j].length ≤ 24</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>The updated catalog, formatted as it is initially given. The elements should be sorted as described above, and all elements of the resulting array should contain at least two elements each.</p>
</li>
</ul>
</div>
 
#### Reference

https://codefights.com/fight/rBC5ydqfQuvPoEkvb/solutions