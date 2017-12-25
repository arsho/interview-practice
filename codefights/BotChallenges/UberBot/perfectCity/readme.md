# Perfect City

<div class="markdown"><p>Consider a city where the streets are perfectly laid out to form an infinite square grid. In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities. As a new Uber developer, you are tasked to create an algorithm that does this calculation.</p>
<p>Given user's departure and destination coordinates, each of them located on some street, find the length of the shortest route between them assuming that cars can only move along the streets. Each street can be represented as a straight line defined by the <code>x = n</code> or <code>y = n</code> formula, where <code>n</code> is an integer.</p>
<p><strong>Example</strong></p>
<p>For <code>departure = [0.4, 1]</code> and <code>destination = [0.9, 3]</code>, the output should be<br>
<code>perfectCity(departure, destination) = 2.7</code>.</p>
<p><code>0.6 + 2 + 0.1 = 2.7</code>, which is the answer.</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/perfectCity/img/Uber_perfectCity.png?_tm=1490636471653" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.float departure</strong></p>
<p>An array <code>[x, y]</code> of <code>x</code> and <code>y</code> coordinates. It is guaranteed that at least one coordinate is integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0.0 ≤ departure[i] ≤ 10.0</code>.</p>
</li>
<li>
<p><strong>[input] array.float destination</strong></p>
<p>An array <code>[x, y]</code> of <code>x</code> and <code>y</code> coordinates. It is guaranteed that at least one coordinate is integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0.0 ≤ destination[i] ≤ 10.0</code>.</p>
</li>
<li>
<p><strong>[output] float</strong></p>
<p>The shorted distance between two points along the streets.</p>
</li>
</ul>
</div>
 
#### Reference

https://codefights.com/fight/ijYEybWnjBnyzENnc/solutions