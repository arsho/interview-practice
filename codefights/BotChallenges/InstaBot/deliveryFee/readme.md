# Delivery Fee

<div class="markdown"><p>To make sure that groceries can always be delivered, Instacart tries to equally distribute delivery requests throughout the day by including an additional delivery fee during busy periods.</p>
<p>Each day is divided into several <code>intervals</code> that do not overlap and cover the whole day from <code>00:00</code> to <code>23:59</code>.  For each <code>i</code> the delivery fee in the <code>intervals[i]</code> equals <code>fees[i]</code>.</p>
<p>Given the list of delivery requests <code>deliveries</code>, your task is to check whether the delivery fee is directly correlated to the order volume in each interval i.e. the <code>interval_fee / interval_deliveries</code> value is constant for each interval throughout the day.</p>
<p><strong>Example</strong></p>
<p>For<br>
<code>intervals = [0, 10, 22]</code>, <code>fees = [1, 3, 1]</code> and</p>
<pre><code>deliveries = [[8, 15],
              [12, 21], 
              [15, 48], 
              [20, 17], 
              [23, 43]]
</code></pre>
<p>the output should be<br>
<code>deliveryFee(intervals, fees, deliveries) = true</code>.</p>
<p>The day is divided into <code>3</code> intervals:</p>
<ul>
<li>from <code>00:00</code> to <code>09:59</code>, the first delivery was made, <code>fees[0] / 1 = 1</code>;</li>
<li>from <code>10:00</code> to <code>21:59</code>, the 2<sup>nd</sup>, 3<sup>rd</sup> and 4<sup>th</sup> deliveries were made, <code>fees[1] / 3 = 1</code>;</li>
<li>from <code>22:00</code> to <code>23:59</code>, the last delivery was made, <code>fees[2] / 1 = 1</code>.</li>
</ul>
<p><code>interval_fee / interval_deliveries = 1</code> for each interval, so the answer is <code>true</code>.</p>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/deliveryFee/img/example.png?_tm=1494708629375" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer intervals</strong></p>
<p>Each interval starts at <code>xx:00</code> and ends at <code>yy:59</code>, where <code>xx</code> equals <code>intervals[i]</code> and <code>yy</code> equals <code>intervals[i + 1] - 1</code>, or <code>23</code> if <code>intervals[i + 1]</code> doesn't exist. <code>intervals[i]</code> represents the hour at which the <code>i<sup>th</sup></code> interval starts. It is guaranteed that <code>intervals[0] = 0</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ intervals.length ≤ 24</code>,<br>
<code>0 ≤ intervals[i] ≤ 23</code>,<br>
<code>intervals[0] = 0</code>.</p>
</li>
<li>
<p><strong>[input] array.integer fees</strong></p>
<p>Array of non-negative integers of the same length as <code>intervals</code>. <code>fees[i]</code> is the delivery fee in the <code>i<sup>th</sup></code> interval.</p>
<p><em>Guaranteed constraints:</em><br>
<code>fees.length = intervals.length</code>,<br>
<code>0 ≤ fees[i] ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer deliveries</strong></p>
<p>Deliveries in the order they were made. Each delivery is represented as the <code>[h, m]</code> array, <code>h</code> is the hour and <code>m</code> is the minute it was done. It is guaranteed that there were no deliveries at the same time.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ deliveries.length ≤ 30</code>,<br>
<code>0 ≤ deliveries[i][0] ≤ 23</code>,<br>
<code>0 ≤ deliveries[i][1] ≤ 59</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the delivery fee is directly correlated to the order volume in each interval, <code>false</code> otherwise.</p>
</li>
</ul>
</div>