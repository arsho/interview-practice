# Launch Sequence Checker

<div class="markdown"><p>The <em>master launch sequence</em> consists of several independent sequences for different systems. Your goal is to verify that all the individual system sequences are in strictly increasing order. In other words, for any two elements <code>i</code> and <code>j</code> (<code>i &lt; j</code>) of the <em>master launch sequence</em> that belong to the same system (having <code>systemNames[i] = systemNames[j]</code>), their values should be in strictly increasing order (i.e. <code>stepNumbers[i] &lt; stepNumbers[j]</code>).</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>systemNames = ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"]</code> and <code>stepNumbers = [1, 10, 11, 2, 12, 111]</code>, the output should be<br>
<code>launchSequenceChecker(systemNames, stepNumbers) = true</code>.</p>
<p>There are three independent sequences for systems <code>"stage_1"</code>, <code>"stage_2"</code>, and <code>"dragon"</code>. These sequences are <code>[1, 2]</code>, <code>[10, 12]</code>, and <code>[11, 111]</code>, respectively. The elements are in strictly increasing order for all three.</p>
</li>
<li>
<p>For <code>systemNames = ["stage_1", "stage_1", "stage_2", "dragon"]</code> and <code>stepNumbers = [2, 1, 12, 111]</code>, the output should be<br>
<code>launchSequenceChecker(systemNames, stepNumbers) = false</code>.</p>
<p>There are three independent sequences for systems <code>"stage_1"</code>, <code>"stage_2"</code>, and <code>"dragon"</code>. These sequences are <code>[2, 1]</code>, <code>[12]</code>, and <code>[111]</code>, respectively. In the first sequence, the elements are not ordered properly.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string systemNames</strong></p>
<p>An array of non-empty strings. <code>systemNames[i]</code> contains the name of the system to which the <code>i<sup>th</sup></code> element of the <em>master launch sequence</em> belongs.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ systemNames.length ≤ 5 · 10<sup>4</sup></code>,<br>
<code>1 ≤ systemNames[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.integer stepNumbers</strong></p>
<p>An array of positive integers. <code>stepNumbers[i]</code> contains the value of the <code>i<sup>th</sup></code> element of the <em>master launch sequence</em>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>stepNumbers.length = systemNames.length</code>,<br>
<code>1 ≤ stepNumbers[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if all the individual system sequences are in strictly increasing order, otherwise return <code>false</code>.</p>
</li>
</ul>
</div>