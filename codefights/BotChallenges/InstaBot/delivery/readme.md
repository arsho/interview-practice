# Delivery

<div class="markdown"><p>Instacart customers are able to set the delivery window during which they want to receive their groceries. There are always plenty of shoppers in the area ready to take a customer's order, but unfortunately they can't always do it right away. Before taking an order a shopper wants to ensure they will make it in time. They also don't want to stay idle, so arriving early <strong>isn't an option</strong> either.</p>
<p>Our task is to implement an algorithm that determines whether shoppers should take the given order or not.</p>
<p>For each shopper you know their travel speed, distance to the store and the estimated amount of time they will spend there. Figure out which of them can take the order, assuming it is known when the customer wants to receive the groceries and the distance between their house and the store.</p>
<p><strong>Example</strong></p>
<p>For <code>order = [200, 20, 15]</code> and <code>shoppers = [[300, 40, 5], [600, 40, 10]]</code>, the output should be</p>
<p><code>delivery(order, shoppers) = [false, true]</code>.</p>
<p>The store is located <code>200</code> m away from the customer's house.</p>
<p>The customer will be ready to receive the groceries in <code>20</code> minutes, but they shouldn't be delivered more than <code>15</code> minutes late.</p>
<p>The first shopper is <code>300</code> m away from the store, his speed is <code>40</code> m/min, and he will spend <code>5</code> minutes in the store, which means that he will need <code>(300 + 200) / 40 + 5 = 17.5</code> minutes to fulfill the order. This will leave him with <code>20 - 17.5 = 2.5</code> idle minutes, so he shouldn't take the order.</p>
<p>The second shopper is <code>600</code> m away from the store, his speed is <code>40</code> m/min, and he will spend <code>10</code> minutes in the store, which means it will take him <code>(600 + 200) / 40 + 10 = 30</code> minutes to fulfill the order. The customer can wait for <code>20 + 15 = 35</code> minutes, which means that the shopper will make it in time.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer order</strong></p>
<p>The order is given as an array of <code>3</code> positive integers. <code>order[0]</code> is the distance from the customer's home to the store in meters, <code>order[1]</code> is the time by which the customer will be ready to receive the delivery in minutes, and <code>order[2]</code> is the number of minutes they are willing to wait.</p>
<p><em>Guaranteed constraints:</em></p>
<p><code>1 ≤ order[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer shoppers</strong></p>
<p>Each element of this array represents a shopper. For each shopper three positive integers are stored in the exact given order: their distance from the shop in meters, their speed in meters per minute and the estimated time they will spend in the store in minutes.</p>
<p><em>Guaranteed constraints:</em></p>
<p><code>1 ≤ shoppers.length ≤ 5</code>,</p>
<p><code>1 ≤ shoppers[i][j] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.boolean</strong></p>
<p>For each shopper return if they should take the order or not.</p>
</li>
</ul>
</div>