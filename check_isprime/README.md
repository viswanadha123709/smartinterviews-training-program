# Check isPrime

## Overview

This project determines whether a given number is prime or not. The solution uses the Miller-Rabin Primality Test to efficiently handle very large numbers up to (10^{18}).

## Problem Statement

Given a number `N`, determine whether it is a prime number.

For each test case:

* Print `"Yes"` if `N` is prime.
* Print `"No"` otherwise.

## Input Format

* The first line contains an integer `T` — the number of test cases.
* The next `T` lines each contain a single integer `N`.

## Output Format

For each test case, print:

* `"Yes"` if `N` is prime.
* `"No"` otherwise.

## Constraints

* `1 ≤ T ≤ 10^4`
* `0 ≤ N ≤ 10^18`

## Approach

The solution implements the Miller-Rabin Primality Test:

1. Handle special cases (`N <= 1`, `2`, `3`, and even numbers).
2. Express `N - 1` as `2^k × m`, where `m` is odd.
3. Compute modular exponentiation using Python's built-in `pow()` function.
4. Repeatedly square the result and check whether it reaches `N - 1`.
5. Determine whether the number is prime based on the test outcome.

## Time Complexity

* **O(log³ N)** per test case

## Space Complexity

* **O(1)**

## Sample Input

3
3
11
15

## Sample Output

Yes
Yes
No

## Technologies Used

* Python 3
* Number Theory
* Miller-Rabin Primality Test

## Author

Veera Viswanadha Swamy
