## Sample Interview Questions - Set 1
#### Duration: 1 Hour

* <b>What is the output of following code? </b>
```c
#include<cslib>
#define C 9+1
int main()
{
	printf("%d\n",C*C);
	return 0;
}
```
* <b>Reverse order of dot-delimited elements in a string. </b>
```
Input: i.love.you.so.much
Output: much.so.you.love.i
```
* <b>Count ways to reach the n’th stair: [Leetcode problem](https://leetcode.com/problems/climbing-stairs/)</b><p>
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
</p>

```
Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
```
* <b>Maximum AND: [Hackerearth Problem](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/maximum-and/)</b><div class="starwars-lab"><p>Given two numbers <strong>A</strong> and <strong>B</strong>. Find the value of pair (P,Q) such that <strong>A &lt;= P &lt; Q &lt;= B</strong> value of <strong>P <a href="http://en.wikipedia.org/wiki/Bitwise_operation#AND">AND</a> Q</strong> is maximum where AND is a binary operator. Refer to this link for more information about AND operator : http://en.wikipedia.org/wiki/Bitwise_operation#AND </p><p><strong>Input:</strong><br>
First line of input contains number of test cases <strong>T</strong>. Each test case contains two numbers <strong>A</strong> and <strong>B</strong>.  </p><p><strong>Output:</strong> For each test case print the value of maximum AND.  </p><p><strong>Constraints: </strong> <br>
1&lt;=<strong>T</strong>&lt;=1000<br>
1&lt;= <strong>A</strong> &lt; <strong>B</strong> &lt;=10<sup>18</sup> </p></div>

```
Sample Input:
2
2 3
4 8

Sample Output:
2
6
```
* <b>Swap Case: [Hackerrank Problem](https://www.hackerrank.com/challenges/swap-case)</b><div>You are given a string <i>S</i>. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.</div><div>For Example: <pre>HackerRank ? hACKERrANK
Pythonist 2 ? pYTHONIST 2</pre></div>
* <b>Same Tree: [Leetcode Problem](https://leetcode.com/problems/same-tree/description/)</b><div>
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.</div>

* <b>Search Insert Position: [Leetcode Problem](https://leetcode.com/problems/search-insert-position/description/)</b><div>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

```
Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
```
</div>