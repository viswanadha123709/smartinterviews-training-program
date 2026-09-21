# 🐀 Rat in a Maze

## 📌 Problem Statement

Given a binary matrix `maze[][]` of size `n × n`, find all possible paths for a rat to travel from the source cell `(0, 0)` to the destination cell `(n - 1, n - 1)`.

The rat can move in **four directions**:

- `U` → Up
- `D` → Down
- `L` → Left
- `R` → Right

### Cell Representation

- `1` → Open cell. The rat can move through it.
- `0` → Blocked cell. The rat cannot move through it.

The rat **cannot visit the same cell more than once** in a single path.

Return all valid paths as strings containing `U`, `D`, `L`, and `R`.

The paths must be returned in **lexicographically increasing order**.

If no valid path exists, return an empty list.

---

## 💡 Approach

This problem can be solved using **Backtracking / DFS**.

### Steps

1. Check if the source `(0, 0)` or destination `(n-1, n-1)` is blocked.
2. Start DFS from `(0, 0)`.
3. Mark the current cell as visited.
4. Try moving in all four directions:
   - Down `D`
   - Left `L`
   - Right `R`
   - Up `U`
5. If the rat reaches `(n-1, n-1)`, store the current path.
6. After exploring a cell, **backtrack** by marking it unvisited.
7. Sort the resulting paths lexicographically.

---

## 🧠 Algorithm

```text
1. Create an empty list ans to store all valid paths.
2. If maze[0][0] == 0 or maze[n-1][n-1] == 0:
      return []

3. Create a visited matrix initialized with False.

4. Perform DFS from (0, 0):

   a. Mark current cell as visited.

   b. If current cell is the destination:
         Add current path to ans.
         Return.

   c. Try moving to every valid neighboring cell:
         - The cell must be inside the matrix.
         - The cell must contain 1.
         - The cell must not be visited.

   d. Mark the cell as unvisited while backtracking.

5. Sort ans lexicographically.

6. Return ans.
