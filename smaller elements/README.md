# Smaller Elements

## Problem Statement

Given an array of integers, determine the number of smaller elements present on the right side of each element and print the total count.

## Example

Input:

```
4 10 54 11 8
```

Smaller elements on the right:

```
4  -> 0
10 -> 1
54 -> 2
11 -> 1
8  -> 0
```

Total Count:

```
0 + 1 + 2 + 1 + 0 = 4
```

Output:

```
4
```

## Intuition

For every element, we need to count how many elements to its right are smaller than it.

A brute-force approach compares every pair:

```
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            count += 1
```

This takes O(N²) time and is inefficient for large inputs.

## Optimized Approach

This problem can be treated as an Inversion Count problem.

An inversion is a pair:

```
(i, j)
```

such that:

```
i < j and arr[i] > arr[j]
```

During Merge Sort:

* Left half and right half are already sorted.
* When an element from the right half is placed before an element from the left half, it forms inversions with all remaining elements in the left half.
* Count those inversions during the merge step.

## Algorithm

1. Divide the array into two halves.
2. Recursively sort both halves.
3. During merge:

   * If left element <= right element, copy left element.
   * Otherwise add (mid - p1 + 1) to the answer.
4. Merge the arrays.
5. Return the total count.

## Complexity Analysis

### Time Complexity

```
O(N log N)
```

### Space Complexity

```
O(N)
```

## Concepts Used

* Arrays
* Merge Sort
* Divide and Conquer
* Recursion
* Inversion Count

## Learning Notes

* This problem is a variation of the Inversion Count problem.
* Merge Sort can be used for more than sorting.
* Counting inversions during merging reduces complexity from O(N²) to O(N log N).
* The key observation is that when a right-half element is smaller than a left-half element, it is smaller than all remaining elements in the left half.

## Tags

`Arrays` `Merge Sort` `Divide and Conquer` `Recursion` `Inversion Count`
