# Find First Substring Occurrence
<div class="markdown"><p><em>Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.</em></p>
<p>Implement a function that takes two strings, <code>s</code> and <code>x</code>, as arguments and finds the first occurrence of the string <code>x</code> in <code>s</code>. The function should return an integer indicating the index in <code>s</code> of the first occurrence of <code>x</code>. If there are no occurrences of <code>x</code> in <code>s</code>, return <code>-1</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>s = "CodefightsIsAwesome"</code> and <code>x = "IA"</code>, the output should be<br>
<code>strstr(s, x) = -1</code>;</li>
<li>For <code>s = "CodefightsIsAwesome"</code> and <code>x = "IsA"</code>, the output should be<br>
<code>strstr(s, x) = 10</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A string containing only uppercase or lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 10<sup>6</sup></code>.</p>
</li>
<li>
<p><strong>[input] string x</strong></p>
<p>String, containing only uppercase or lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ x.length ≤ 10<sup>6</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>An integer indicating the index of the first occurrence of the string <code>x</code> in <code>s</code>, or <code>-1</code> if <code>s</code> does not contain <code>x</code>.</p>
</li>
</ul>
</div>

### Reference
https://codefights.com/interview-practice/task/C8Jdyk3ybixqQdAvM/