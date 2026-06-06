# Product of XOR of Pairs

## Problem Statement

Given an array of size `N`, find the product of XOR values of all **good pairs** in the array.

A pair `(A[i], A[j])` is considered good if:

```text
0 ≤ i < j < N
```

Since the product can be very large, print the result modulo:

```text
10^9 + 7
```

---

## Key Observation

The constraints allow:

```text
A[i] ≤ 3000
```

There are only **3001 possible values (0 to 3000)**.

By the Pigeonhole Principle:

- If `N > 3001`, at least two elements must be equal.
- For equal elements:

```text
A[i] XOR A[j] = 0
```

- Since the product contains a factor `0`, the entire answer becomes:

```text
0
```

Therefore:

```text
If N > 3001, answer = 0
```

Otherwise, we can directly compute the product of XOR values for all pairs.

---

## Algorithm

### Case 1: N > 3001

Return:

```text
0
```

because duplicate values must exist, producing a XOR of `0`.

### Case 2: N ≤ 3001

For every pair `(i, j)` where:

```text
i < j
```

1. Compute:

```text
A[i] XOR A[j]
```

2. Multiply it into the answer.
3. Take modulo `10^9 + 7`.

---

## Proof of Correctness

For every good pair `(i, j)`:

```text
Contribution = A[i] XOR A[j]
```

The required answer is:

```text
Π (A[i] XOR A[j])
```

over all pairs with `i < j`.

If two equal values exist:

```text
x XOR x = 0
```

and therefore:

```text
Product = 0
```

When `N > 3001`, duplicates are guaranteed because all values lie in the range `[0, 3000]`.

Otherwise, computing every pair directly evaluates exactly the required product.

Hence the algorithm is correct.

---

## Complexity Analysis

For `N ≤ 3001`:

- Time Complexity: `O(N²)`
- Space Complexity: `O(1)`

The worst-case number of pairs is:

```text
3001 × 3000 / 2 ≈ 4.5 million
```

which is acceptable.

---

## Python Solution

```python
mod = 1000000007

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n > 3001:
        print(0)
        continue

    ans = 1

    for i in range(n):
        for j in range(i + 1, n):
            ans = (ans * (arr[i] ^ arr[j])) % mod

    print(ans)
```

---

## Example

### Input

```text
2
4
1 2 3 7
3
4 3 7
```

### Output

```text
720
84
```

---

## Example Walkthrough

For:

```text
[1, 2, 3, 7]
```

Good pairs:

```text
(1,2) → 3
(1,3) → 2
(1,7) → 6
(2,3) → 1
(2,7) → 5
(3,7) → 4
```

Product:

```text
3 × 2 × 6 × 1 × 5 × 4 = 720
```

Output:

```text
720
```
