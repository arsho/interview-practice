# Shopping List

<div class="markdown"><p>As part of an Instacart beta testing group, Sara is trying out a brand new feature that automatically estimates the combined cost of the items in her handwritten shopping list. Her list contains both items and their prices. All Sara has to do is snap a photo of her list with the Instacart app, and she gets a quick estimate of what everything will cost.</p>
<p>Sara asked for your help, so it is up to you to devise an algorithm that calculates the cost after the image is converted into plain text. All you need to do is extract all numbers from the given string <code>items</code> and sum them up.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>items = "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4"</code>, the output should be<br>
<code>shoppingList(items) = 7.48</code>;</li>
<li>For <code>items = "blue suit for 24$, cape for 12.99$ &amp; glasses for 15.70"</code>, the output should be<br>
<code>shoppingList(items) = 52.69</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string items</strong></p>
<p>A shopping list given as a string. It is guaranteed that the only numbers in it are dollar prices for different items.<br>
Note that although each price is given in dollars, you do not know their exact form. Each of them can either be an integer, or a decimal number with one or two decimal places and it may or may not be followed by a dollar sign.<br>
However, you may assume that if there is a period (<code>'.'</code>) between two digits, then it's a decimal mark.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ items.length ≤ 6 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] float</strong></p>
<p>The total cost of all <code>items</code>.</p>
</li>
</ul>
</div>