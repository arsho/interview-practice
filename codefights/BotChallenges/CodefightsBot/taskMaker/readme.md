# Task Maker

<div class="markdown"><p>CodeFights supports different challenge types. One of them asks you to find a bug on a single line of the given code, usually referred to as a <code>DEBUGGING</code> challenge. Behind the scenes, we correctly implement each challenge ourselves and then use special comments with specific prefixes to introduce the buggy lines. Here is an image to help you visualize what that looks like:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/taskMaker/img/code.png?_tm=1491409776190" alt=""></p>
<p>As you can see, each of the special comments looks like this:</p>
<p><code>&lt;spaces&gt;//DB &lt;id&gt;//&lt;buggy line&gt;</code></p>
<p>where <code>&lt;spaces&gt;</code> is a string consisting of zero or more spaces (for indentation), <code>DB</code> indicates that this comment is for a <code>DEBUGGING</code> challenge (let's assume this is the only type we support), <code>id</code> is a positive integer that helps us enumerate these and <code>&lt;buggy line&gt;</code> is some code that's almost identical to the line to be replaced but with an inserted bug (that is guaranteed not to contain any <code>'/'</code> symbols).</p>
<p>When importing these to our database, each of the special comments is used to create a debugging challenge. The importing script looks for the last non-special-comment line above the special comment and replaces it with <code>"&lt;spaces&gt;&lt;buggy line&gt;"</code> while removing all the other special comments from the code. Examples below can help clarify this process further.</p>
<p>Your task is to produce <code>DEBUGGING</code> challenges given source code that includes the special comments and the <code>id</code> of the desired <code>DEBUGGING</code> challenge.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For</p>
<pre><code>source = ["ans = 0",
          "for i in range(n):",
          "    for j in range(n):",
          "    //DB 3//for j in range(1, n):",
          "    //DB 2//for j in range(n + 1):",
          "        ans += 1",
          "return ans"]
</code></pre>
<p>and <code>challengeId = 3</code>, the output should be</p>
<pre><code>taskMaker(source, challengeId) = ["ans = 0",
                                  "for i in range(n):",
                                  "    for j in range(1, n):",
                                  "        ans += 1",
                                  "return ans"]
</code></pre>
</li>
<li>
<p>For</p>
<pre><code>source = ["ans = 0;",
          "for (var i = 0; i &lt; n; i++) {",
          "    for (var j = 0; j &lt; n; j++) {",
          "    //DB 3//for (var j = 1; j &lt; n; j++) {",
          "    //DB 2//for (var j = 0; j &lt; n + 1; j++) {",
          "        ans++;",
          "    }",
          "}",
          "return ans;"]
</code></pre>
<p>and <code>challengeId = 2</code>, the output should be</p>
<pre><code>taskMaker(source, challengeId) = ["ans = 0;",
                                  "for (var i = 0; i &lt; n; i++) {",
                                  "    for (var j = 0; j &lt; n + 1; j++) {",
                                  "        ans++;",
                                  "    }",
                                  "}",
                                  "return ans;"]
</code></pre>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string source</strong></p>
<p>The source string. It is guaranteed that it doesn't contain any comments except the special ones, and only special lines contain <code>//DB</code>. It is also guaranteed that for each possible subtask type and id, it contains not more than one special comment that starts with <code>"&lt;spaces&gt;//DB &lt;id&gt;//"</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ source.length ≤ 15</code>,<br>
<code>0 ≤ source[i].length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[input] integer challengeId</strong></p>
<p>The <code>id</code> of the desired <code>DEBUGGING</code> challenge.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ challengeId &lt; 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The resulting <code>DEBUGGING</code> challenge after the proper replacements are complete.</p>
</li>
</ul>
</div>
 
#### Reference

https://codefights.com/fight/PMCRqouS3phaatFYc/solutions