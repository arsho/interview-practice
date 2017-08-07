# Is Admissible Overpayment

<div class="markdown"><p>After recently joining Instacart's beta testing developer group, you decide to experiment with their new API. You know that the API returns item-specific display-ready strings like <code>10.0% higher than in-store</code> or <code>5.0% lower than in-store</code> that inform users when the price of an item is different from the one in-store. But you want to extend this functionality by giving people a better sense of how much more they will be paying for their entire shopping cart.</p>
<p>Your app lets a user decide the total amount <code>x</code> they are willing to pay via Instacart over in-store prices. This you call their <em>price sensitivity</em>.</p>
<p>Your job is to determine whether a given customer will be willing to pay for the given items in their cart based on their stated <em>price sensitivity</em> <code>x</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For<br>
<code>prices = [110, 95, 70]</code>,</p>
<pre><code>notes = ["10.0% higher than in-store", 
         "5.0% lower than in-store", 
         "Same as in-store"]
</code></pre>
<p>and <code>x = 5</code>, the output should be<br>
<code>isAdmissibleOverpayment(prices, notes, x) = true</code>.</p>
<p>In-store prices of the first and the second items are <code>100</code>, and the price of the third item is <code>70</code>, which means the customer is overpaying <code>10 - 5 + 0 = 5</code>, which they are willing to do based on their <em>price sensitivity</em>.</p>
</li>
<li>
<p>For<br>
<code>prices = [48, 165]</code>,</p>
<pre><code>notes = ["20.00% lower than in-store", 
         "10.00% higher than in-store"]
</code></pre>
<p>and <code>x = 2</code>, the output should be<br>
<code>isAdmissibleOverpayment(prices, notes, x) = false</code>.</p>
<p>The in-store price of the first item is <code>60</code>, and the second item is <code>150</code>. The overpayment equals <code>15 - 12 = 3</code>, which is too much for the customer to be willing to pay.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.float prices</strong></p>
<p>Positive numbers, representing prices of the items in the shopping cart.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ prices.length ≤ 10</code>,<br>
<code>20.0 ≤ prices[i] ≤ 35.0 · 10<sup>3</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.string notes</strong></p>
<p>Array of the same length as <code>prices</code>. For each valid <code>i</code> <code>notes[i]</code> has one of the following forms:</p>
<ul>
<li><code>"x% higher than in-store"</code>, which means that Instacart price of the <code>i<sup>th</sup></code> item is <code>x%</code> higher than the local one;</li>
<li><code>"x% lower than in-store"</code>, which means  that Instacart price of the <code>i<sup>th</sup></code> item is <code>x%</code> lower than the local one;</li>
<li><code>"Same as in-store"</code>, which means that the <code>i<sup>th</sup></code> item costs the same in Instacart and in the local store,</li>
</ul>
<p>where <code>x</code> is a positive float number with the decimal point and at least one digit after it.</p>
<p><em>Guaranteed constraints:</em><br>
<code>notes.length = prices.length</code>,<br>
<code>16 ≤ notes[i].length ≤ 30</code>.</p>
</li>
<li>
<p><strong>[input] float x</strong></p>
<p>A non-negative float, the maximum amount of money the customer is willing to overpay.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ x ≤ 150.0</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the overpayment is admissible, <code>false</code> otherwise.</p>
</li>
</ul>
</div>