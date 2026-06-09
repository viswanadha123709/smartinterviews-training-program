# Optimal Prime Game

## Problem Statement

Two players play a game on a number **N**.

- Players take turns alternately.
- In each move, a player subtracts a prime number `p` such that `p ≤ N`.
- The player who cannot make a move loses.
- Both players play optimally.

Determine whether the winner is the **First** player or the **Second** player.

---

## Approach

This is a classic **Game Theory + Dynamic Programming** problem.

Let:

- `dp[i] = True` → Current player can force a win from state `i`.
- `dp[i] = False` → Current player will lose from state `i`.

### Base Cases

- `dp[0] = False`
- `dp[1] = False`

Since no prime number can be subtracted.

### Transition

For every number `i`:

- Try all prime numbers `p ≤ i`.
- If there exists a prime `p` such that `dp[i - p] == False`, then the current player can move the opponent into a losing state.

Therefore:

```python
dp[i] = True
```

Otherwise:

```python
dp[i] = False
```

### Prime Generation

Generate all prime numbers up to `10^4` using the **Sieve of Eratosthenes**.

---

## Algorithm

1. Generate all primes up to `10^4`.
2. Build the DP table:
   - `dp[0] = dp[1] = False`
   - For each `i` from `2` to `10^4`:
     - Check all primes `p ≤ i`
     - If `dp[i-p]` is losing, mark `dp[i]` as winning.
3. For each test case:
   - Print `"First"` if `dp[n]` is winning.
   - Otherwise print `"Second"`.

---

## Correctness Proof

We prove by induction that `dp[i]` correctly represents whether the current player can force a win.

### Base Cases

For `i = 0` and `i = 1`, no valid move exists.

Hence:

```python
dp[0] = dp[1] = False
```

which is correct.

### Inductive Hypothesis

Assume `dp[k]` is correctly computed for all `k < i`.

### Inductive Step

For state `i`:

- If there exists a prime `p` such that `dp[i-p] = False`, the current player can move to a losing state and therefore win.
- Otherwise, every move leads to a winning state for the opponent, so the current player loses.

Thus `dp[i]` is computed correctly.

By induction, the algorithm is correct for all values up to `10^4`.

---

## Complexity Analysis

### Time Complexity

- Sieve: `O(N log log N)`
- DP: `O(N × π(N))`

where `π(N)` is the number of primes up to `N`.

For `N = 10^4`, this is efficient enough.

### Space Complexity

```text
O(N)
```

---

## Reference Implementation

```python
maxi = 10**4
arr = [True] * (maxi + 1)
primes = []

arr[0] = arr[1] = False

for i in range(2, maxi + 1):
    if arr[i]:
        primes.append(i)

        for j in range(i * i, maxi + 1, i):
            arr[j] = False
    else:
        for j in primes:
            if j > i:
                break

            if arr[i - j] == False:
                arr[i] = True
                break

for _ in range(int(input())):
    n = int(input())

    if arr[n]:
        print("First")
    else:
        print("Second")
```

## Key Insight

A state is **winning** if at least one move leads to a **losing** state.

A state is **losing** if all possible moves lead to **winning** states.

This observation allows us to solve the problem efficiently using dynamic programming.
