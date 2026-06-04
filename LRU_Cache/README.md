# LRU Cache

## Problem Statement
Design and implement a Least Recently Used (LRU) Cache of size K.

Given a sequence of page requests:
- If the page is already present in the cache, it becomes the Most Recently Used (MRU) page.
- If the page is not present:
  - Insert it into the cache.
  - If the cache is full, remove the Least Recently Used (LRU) page.

After processing all page requests, print the final contents of the cache from LRU to MRU.

---

## Approach

We use two hash maps:

### hm1
Stores:

`page -> latest index`

Used to check whether a page is already present in the cache.

### hm2
Stores:

`index -> page`

Maintains pages in access order.

### Processing Pages

- If a page is not present:
  - If the cache is full, remove the least recently used page.
  - Insert the new page.

- If a page is already present:
  - Remove its old occurrence.
  - Insert it again with the current index.
  - This makes it the most recently used page.

---

## Example

Input:
```text
5 3
3 8 2 8 1
```

Cache evolution:
```text
[3]
[3, 8]
[3, 8, 2]
[3, 2, 8]
[2, 8, 1]
```

Output:
```text
2 8 1
```

---

## Complexity Analysis

**Time Complexity:** `O(N)`

**Space Complexity:** `O(K)`

---


## Key Idea

Whenever a page is accessed again:
1. Remove its old position.
2. Insert it at the latest position.
3. It becomes the Most Recently Used page.

The remaining pages in `hm2` are naturally ordered from **Least Recently Used (LRU)** to **Most Recently Used (MRU)**, which directly gives the required output.
