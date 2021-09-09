# Algorithm Design and Implementation
CS602-Algorithm Design and Implementation - A course from MITB Program SMU

# Table of contents
- [Table of contents](#table-of-contents)
- [Part A - Algorithm](#part-a-algorithm)
- [1. Recursion](#1-recursion) 
- [2. Sorting](#2-sorting)
  - [2.1. Insertion Sort](#21-insertion-sort)
  - [2.2. Merge Sort](#22-merge-sort)


# Part A. Algorithm
# 1. Recursion
-  Example: Factorial, Fibonacci Number, Euclidean Algorithm, Extended Euclidean Algorithm
# 2. Sorting
## 2.1. Insertion Sort
- Time Complexity: `O(n^2)`
```Python
def insertion_sort(A):
    for i in range(1, len(A)): #i = start from the second the element to End of Array
        key = A[i] #Select A[i] as Key, and start to insert from j = i - 1 all the way to 0
        j = i - 1
        while (j >= 0 and key < A[j]):
            A[j+1] = A[j] #if A[j] > Key, swap A[j] to A[j+1] position
            j-=1
        A[j+1] = key #Place key to the right pos, which is A[j+1]
    return A
```
## 2.2. Merge Sort
- Time Complexity: `O(n*log(n))`
```Python
def merge_sort(A,lower, upper):
    if lower < upper:
        mid = (lower+upper)//2
        merge_sort(A, lower, mid)
        merge_sort(A, mid + 1, upper)
        merge(A, lower, mid, upper)
```
- For the merge function, we will create 2 copy of `A[lower, mid]` and `A[mid+1, upper` to `tmpL` and `tmpR` and start to sort back
- Need to add the stopper `float("inf")` to the end of both `tmpL` and `tmpR`
```Python
def merge(A, lower, mid, upper):
    #Step 1: Create Copy of A[lower, mid] to tmpL and A[mid+1, upper] to tmpR
    tmpL = [0]*((mid - lower + 1)+1)  #mid - lower + 1 = len(tmpL), +1 to add the place for Stopper
    for i in range(0, (mid - lower)+1): #len(A[lower, mid]) = mid - lower + 1
        tmpL[i] = A[i+lower]
    tmpL[mid-lower+1] = float('inf') #add the stopper to the end of tmpL
    
    tmpR = [0]*(upper - mid + 1) #[upper - (mid+1) + 1] + 1 = upper - mid + 1
    for j in range(0, upper - mid): #len(A[mid+1, upper]) = upper - (mid+1) + 1 = upper - mid
        tmpR[j] = A[j+mid+1]
    tmpR[upper - mid] = float('inf') #add the stopper to the end of tmpR
    
    #Step 2: Start to merge tmpL and tmpR back to A[lower, upper]
    i, j = 0, 0
    for k in range(lower, upper + 1):
        if tmpL[i] <= tmpR[j]:
            A[k] = tmpL[i]
            i+=1
        else:
            A[k] = tmpR[j]
            j+=1
```


[(Back to top)](#table-of-contents)
