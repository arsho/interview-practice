# Incremental Backups

<div class="markdown"><p>One of the easiest ways to back up files is with an incremental backup. This method only backs up files that have changed since the last backup.</p>
<p>You are given a list of <code>changes</code> that were made to the files in your database, where for each valid <code>i</code>, <code>changes[i][0]</code> is the timestamp of the time the change was made, and <code>changes[i][1]</code> is the file id.</p>
<p>Knowing the timestamp of the last backup <code>lastBackupTime</code>, your task is to find the files which should be included in the next backup. Return the ids of the files that should be backed up as an array sorted in ascending order.</p>
<p><strong>Example</strong></p>
<p>For <code>lastBackupTime = 461620205</code> and</p>
<pre><code>changes = [[461620203, 1], 
           [461620204, 2], 
           [461620205, 6],
           [461620206, 5], 
           [461620207, 3], 
           [461620207, 5], 
           [461620208, 1]]
</code></pre>
<p>the output should be<br>
<code>incrementalBackups(lastBackupTime, changes) = [1, 3, 5]</code>.</p>
<p>Here's how the answer is calculated:</p>
<ul>
<li>File with <code>id = 1</code> was changed at <code>461620203</code> and <code>461620208</code>, and since the last backup was at <code>461620205</code>, it should be included in the next backup.</li>
<li>File with <code>id = 2</code> was changed only at <code>461620204</code>, so there's no need to back it up.</li>
<li>File with <code>id = 3</code> was changed at <code>461620207</code>, so it should be backed up next time.</li>
<li>File with <code>id = 5</code> was changed at <code>461620206</code> and <code>461620207</code>, so it should be included in the new backup as well.</li>
<li>File with <code>id = 6</code> was changed at <code>461620205</code>, so it can be ignored.</li>
</ul>
<p>Check out the image below for better understanding:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/incrementalBackups/img/example.png?_tm=1490626049337" alt=""></p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer lastBackupTime</strong></p>
<p>A non-negative integer, the timestamp of the previous backup.</p>
<p><em>Guaranteed constraints:</em><br>
<code>4 · 10<sup>8</sup> ≤ lastBackupTime &lt; 5 · 10<sup>8</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer changes</strong></p>
<p>Array of changes sorted <a href="keyword://lexicographical-order-for-arrays">lexicographically</a>, where each change is given in the format as described above.<br>
If for some <code>i</code> <code>changes[i][0] = lastBackupTime</code>, assume that the <code>i<sup>th</sup></code> file was successfully backed up during the last backup.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ changes.length ≤ 100</code>,<br>
<code>0 ≤ changes[i][0] ≤ 5 · 10<sup>8</sup></code>,<br>
<code>0 ≤ changes[i][1] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array of ids of the changes that should be backed up next time, sorted in ascending order.</p>
</li>
</ul>
</div> 
