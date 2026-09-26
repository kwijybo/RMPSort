# RMPSort
Recursive Median Partition Sort proof of concept for a new lightning fast sorting algorithm, based on QuickSort but runs in O(2n) time

## Introduction and rationale

QuickSort picks an arbitrary pivot which risks a worst case run time of O(n²). Instead, let us compute the arithmetic mean of the smallest and largest numbers in the set, and choose that as the pivot, dividing the list into numbers smaller than the pivot, and numbers equal to or greater than the pivot. We can then recursively repeat this process to sort the entire list in the minimum steps possible.

## Proof of concept
A proof of concept is provided in rmp.py for the case where the list consists of integers. Expanding the implementation to other types is trivial.