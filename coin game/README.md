# Coin Piles

## Problem Statement

Given two piles containing `a` and `b` coins, determine whether it is possible to remove all coins from both piles.

In a single move, you must remove:

- 2 coins from one pile, and
- 1 coin from the other pile.

Print `"YES"` if both piles can be emptied completely; otherwise print `"NO"`.

---

## Approach

Each move removes exactly **3 coins** in total.

Therefore:

1. The total number of coins must be divisible by 3.
   ```
   (a + b) % 3 == 0
   ```

2. The larger pile cannot contain more than twice the number of coins in the smaller pile.
   ```
   max(a, b) <= 2 * min(a, b)
   ```

If both conditions are satisfied, it is always possible to empty both piles.

---

## Algorithm

For each test case:

1. Read `a` and `b`.
2. Check:
   - `(a + b) % 3 == 0`
   - `max(a, b) <= 2 * min(a, b)`
3. If both conditions are true, print `"YES"`.
4. Otherwise, print `"NO"`.

---

## Complexity Analysis

- **Time Complexity:** O(1) per test case
- **Space Complexity:** O(1)

---

## Python Solution

```python
for _ in range(int(input())):
    a, b = map(int, input().split())

    if (a + b) % 3 == 0 and max(a, b) <= 2 * min(a, b):
        print("YES")
    else:
        print("NO")
```

---

## Example

### Input

```
3
2 1
2 2
3 3
```

### Output

```
YES
NO
YES
```

---

## Key Insight

A valid move always removes exactly 3 coins (`2 + 1`).

Thus:
- The total number of coins must be divisible by 3.
- Neither pile can have more than twice as many coins as the other.

These conditions are both necessary and sufficient to determine the answer.
