# A Power B

## Problem Statement

Given two integers A and B, compute:

```
A^B
```

Since the result can be very large, print:

```
A^B mod 1000000007
```

Do not use any built-in power functions for the main logic.

## Example

Input:

```
5 2
```

Output:

```
25
```

Input:

```
2 30
```

Output:

```
73741817
```

## Intuition

A straightforward approach is to multiply A by itself B times.

```
result = 1
for i in range(B):
    result *= A
```

However, this takes O(B) time and becomes too slow when B is very large.

## Optimized Approach

Use Binary Exponentiation (Fast Exponentiation).

Observation:

```
A^10 = (A^5)^2
A^8  = ((A^2)^2)^2
```

Instead of multiplying A repeatedly, square the base and reduce the exponent by half at every step.

Rules:

* If B is odd:

  ```
  result = result * A
  ```

* Square the base:

  ```
  A = A * A
  ```

* Divide exponent by 2:

  ```
  B = B // 2
  ```

Apply modulo at every step to prevent overflow.

## Algorithm

1. Initialize result = 1.
2. While B > 0:

   * If B is odd, multiply result by A.
   * Square A.
   * Divide B by 2.
   * Apply modulo 1000000007.
3. Print the final result.

## Complexity Analysis

### Time Complexity

```
O(log B)
```

### Space Complexity

```
O(1)
```

## Concepts Used

* Binary Exponentiation
* Modular Arithmetic
* Bit Manipulation
* Mathematics

## Learning Notes

* Binary Exponentiation reduces complexity from O(B) to O(log B).
* Modular arithmetic prevents integer overflow.
* This technique is widely used in competitive programming and coding interviews.
* Understanding exponent decomposition is the key to solving this problem efficiently.

## Applications

* Cryptography
* Competitive Programming
* Large Number Computations
* Modular Arithmetic Problems

## Tags

`Binary Exponentiation` `Mathematics` `Modular Arithmetic` `Bit Manipulation` `Fast Power`
