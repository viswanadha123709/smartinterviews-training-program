# Sum of XOR of Pairs

## Problem Statement

Given an array of integers, find the sum of XOR values of all **ordered pairs** formed by the array elements (including pairs where both elements are the same).

Formally, compute:

\[
\sum_{i=0}^{N-1}\sum_{j=0}^{N-1}(A_i \oplus A_j)
\]

---

## Key Observation

Consider a single bit position `b`.

Let:

- `count` = number of elements having the `b`-th bit set.
- `n - count` = number of elements having the `b`-th bit unset.

For the XOR of two numbers to have the `b`-th bit set, one number must have the bit set and the other must have it unset.

Number of such **unordered pairs**:

```text
count × (n - count)
```

Contribution of this bit:

```text
count × (n - count) × (2^b)
```

Since the problem counts **ordered pairs**, both `(a, b)` and `(b, a)` are included.

Therefore, multiply the final answer by `2`.

---

## Algorithm

For every bit from `0` to `30`:

1. Count how many numbers have the current bit set.
2. Let this count be `count`.
3. Add the contribution:

```text
count × (n - count) × (1 << bit)
```

4. After processing all bits, multiply the answer by `2`.

---

## Proof of Correctness

For a fixed bit position `b`:

- XOR contributes `2^b` only when the two numbers differ at that bit.
- There are `count` numbers with bit `b = 1`.
- There are `n - count` numbers with bit `b = 0`.

Thus, the number of unordered pairs contributing at bit `b` is:

```text
count × (n - count)
```

Each such pair contributes:

```text
2^b
```

Hence, total contribution of bit `b` is:

```text
count × (n - count) × 2^b
```

Since ordered pairs are required, each pair is counted twice:

```text
2 × count × (n - count) × 2^b
```

Summing over all bit positions gives the required answer.

---

## Complexity Analysis

- **Time Complexity:** `O(31 × N)`
- **Space Complexity:** `O(1)`

---

## Java Solution

```java
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t-- > 0) {

            int n = sc.nextInt();

            int[] arr = new int[n];

            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            long ans = 0;

            for (int bit = 0; bit < 31; bit++) {

                long count = 0;

                for (int i = 0; i < n; i++) {
                    if (((arr[i] >> bit) & 1) == 1) {
                        count++;
                    }
                }

                ans += count * (n - count) * (1L << bit);
            }

            System.out.println(2 * ans);
        }

        sc.close();
    }
}
```

---

## Example

### Input

```text
3
3
5 12 8
5
4 10 54 11 8
6
15 35 25 10 15 12
```

### Output

```text
52
560
680
```

---

## Takeaway

Instead of checking all `N²` pairs, we independently calculate the contribution of each bit using counting. This reduces the complexity from **O(N²)** to **O(31 × N)**, making it efficient even for large inputs.
