# Large Range Primes

## Problem Statement

Given two numbers **M** and **N** (**M ≤ N**), print all prime numbers in the range **[M, N]** (inclusive).

### Sample Input

```
2
1 10
3 5
```

### Sample Output

```
2
3
5
7

3
5
```

---

## Approach

Since **N** can be as large as **10¹²**, generating all primes up to **N** using a traditional Sieve of Eratosthenes is not feasible. Instead, this solution uses the **Segmented Sieve Algorithm**.

The main idea is to consider only the numbers in the required range **[M, N]**. A boolean array of size **(N - M + 1)** is created, where each position represents a number in the given range. Initially, every number is assumed to be prime.

For every number `i` from **2** to **√N**, all multiples of `i` inside the range are marked as non-prime. After processing all such numbers, the remaining unmarked numbers are prime and are printed.

---

## Important Logic

The most important part of the solution is finding the **first multiple of `i` that lies inside the range [M, N]**.

```
start = max(i * i, ((M + i - 1) // i) * i)
```

### Why is this needed?

* `i * i` ensures that we do not mark smaller multiples that have already been processed by smaller prime factors.
* `((M + i - 1) // i) * i` calculates the first multiple of `i` that is greater than or equal to `M`.
* Taking the maximum of these two values gives the correct starting point for marking multiples within the segment.

### Example

Suppose:

```
M = 20
N = 40
i = 3
```

First multiple of 3 inside the range:

```
((20 + 3 - 1) // 3) * 3
= (22 // 3) * 3
= 7 * 3
= 21
```

So marking starts from:

```
max(3 × 3, 21)
= max(9, 21)
= 21
```

The multiples marked will be:

```
21, 24, 27, 30, 33, 36, 39
```

---

## Time Complexity

**O((N − M + 1) log log N)**

---

## Space Complexity

**O(N − M + 1)**

---

## Key Concepts

* Prime Numbers
* Sieve of Eratosthenes
* Segmented Sieve
* Range-Based Prime Generation
* Mathematical Optimization

---

## Takeaway

This problem is a classic application of the **Segmented Sieve Algorithm**, which is widely used in competitive programming when the range of numbers is small but the values themselves can be extremely large. The formula

`start = max(i*i, ((M+i-1)//i)*i)`

is the heart of the algorithm, as it efficiently identifies where marking should begin within the current segment.
