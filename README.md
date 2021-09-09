# Algorithm Design and Implementation
CS602-Algorithm Design and Implementation - A course from MITB Program SMU

# Table of contents
- [Table of contents](#table-of-contents)
- [Part A - Algorithm](#part-a-algorithm)
- [1. Recursion](#1-recursion) 
- [2. Sorting](#2-sorting)
  - [2.1. Insertion Sort](#21-insertion-sort)
  - [2.2. Merge Sort](#22-merge-sort)
- [3. Analysis of Algorithm](#3-analysis-of-algorithm)
  - [3.1. Types of Analysis](#31-types-of-analysis) 
  - [3.2. Asymptotic Order of Growth](#32-asymptotic-order-of-growth)

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
- For the merge function, we will create 2 copy of `A[lower, mid]` and `A[mid+1, upper]` to `tmpL` and `tmpR` and start to sort back
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
# 3. Analysis of Algorithm
## 3.1. Types of Analysis
- **Worst Case**:
- **Average Case**: difficult to compute as need to find combination of inputs and then take the average of run time
- **Amortized Case**: sampling with replacement

## 3.2. Asymptotic Order of Growth
- **Asymptotic Order of Growth**: know how the function behaves as the input gets larger, towards infinity (i.e: **in the limit**)
  - For example: the  blue algo is scale better then the red on 
  <p align="center"><img height="250" alt="Screenshot 2021-09-09 at 14 48 29" src="https://user-images.githubusercontent.com/64508435/132636684-19a33b59-816f-4c33-b693-fbfdbe9ce37a.png"></p>
  
### 3.2.1. Upper Bound (Big O) Notation
- **Note 1**: Exponential > (dominates) polynomial > (dominates) logarithmic
  - For example: `n*log(n)` = `O(n^(1.5)) = O(n*sqrt(n))`, since log is growth slower than sqrt(n), so `n*log(n)` will be upper bounded by `n*sqrt(n)`
  - Generalize: `n*log(n)` = `O(n^(k))` for any k > 0
- **Note 2**: `log⁡(n)<n` &rarr; `log⁡(log⁡(n)) < log⁡(n)`   have  as log is monotonic increasing function
- **Note 3**: `n! = O(n^n)`
<img width="620" alt="Screenshot 2021-09-09 at 14 56 21" src="https://user-images.githubusercontent.com/64508435/132637675-0cc9eb14-91cc-4500-9549-fb8a45c69a8e.png">

### 3.2.2. Lower Bound (Omega) Notation
### 3.2.3. Tight Asymptotic (Theta) Bound
<p align="center"><img height="250" alt="Screenshot 2021-09-09 at 14 53 59" src="https://user-images.githubusercontent.com/64508435/132637355-4fd119ee-1662-4bd4-bbc5-b062bfb39206.png"></p>

#### Exercise of Big O, Omega and Theta
- Determine which relationship is correct and briefly explain why
<p align="center"><img height="200" alt="Screenshot 2021-09-09 at 15 00 56" src="https://user-images.githubusercontent.com/64508435/132638284-705b69be-749a-4d76-8132-87b5f6a5a3ab.png"></p>

- a. f(n) = log(n^2) = 2log(n), so **f(n) = Theta(g(n))**
- b. g(n) = log(n^2) = 2log(n), so f(n) = Omega(g(n))
- c. log(n) < n => log(log(n)) < log(n), so f(n) = O(g(n))
- d. since (log(n))^2 lower than n, so **f(n) = Omega(g(n))**
- e. f(n) = Omega(g(n))
- f. f(n) = Theta(g(n))
- g. f(n) = O(g(n))
- h. f(n) = O(g(n))

[(Back to top)](#table-of-contents)
