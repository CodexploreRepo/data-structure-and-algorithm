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
  - [3.3. Recurrence](#33-recurrence)
- [Part B - Data Structure](#part-b-data-structure)
- [1. What is Data Structure](#1-what-is-data-structure)
  - [1.1. Abstract Data Type ](#11-abstract-data-type) 
- [2. Arrays](#2-arrays)
- [3. Linked List](#3-linked-list)
  - [3.1. Advantage vs Disadvantage of Linked List](#31-advantage-vs-disadvantage-of-linked-list) 
  - [3.2. Other Linked List Variants](#32-other-linked-list-variants)
  - [3.3. Arrays vs Linked List](#33-arrays-vs-linked-list)
- [4. Stacks, Queues and Deques](#4-stacks-queues-and-deques)
  - [4.1. ADT Design for Stacks, Queues, and Deques](#41-adt-design-for-stacks-queues-and-deques) 
  - [4.2. Stacks Queues and Deques Implementation using Linked List](#42-stacks-queues-and-deques-implementation-using-linked-list)
- [5. Dynamic Arrays](#5-dynamic-arrays)
- [6. Tree](#6-tree)
  - [6.1. Binary Tree](#61-binary-tree) 

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

## 3.3. Recurrence
### 3.3.1 Divide and Conquer
- Motivation: **Divide and Conquer** Break a problem of size n into smaller problems such that by solving the smaller problems, we can construct a solution the entire problem:
1) Divide
2) Solve each of the smaller problems
3) Combine solutions

### 3.3.2. Recurrence
- Recurrence describes a function `T(n)` in terms of its values on smaller inputs `T(m)`, where m < n
- There are 3 ways to solve Recurrence
#### Method 1. Substitution Method
#### Method 2. Recursion Tree Method
<p float="left">
  <img src="https://user-images.githubusercontent.com/64508435/132649906-196183de-a017-4d2e-be16-82ac00d48468.jpg"  width="50%">
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://user-images.githubusercontent.com/64508435/132649922-c6929055-3f10-4c20-80e5-dc2e2c1126f1.jpg" width="45%">
</p>

#### Method 3. Master Theorem Method
<p float="left">
  <img src="https://user-images.githubusercontent.com/64508435/132654625-452f8168-71d3-4277-ab96-3edf16585707.png"  width="50%">
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://user-images.githubusercontent.com/64508435/132654268-1dd1425f-2387-4096-9551-760b9840612c.png" width="45%">
</p>

- **Example of Master Theorem:**
<p float="left">
  <img src="https://user-images.githubusercontent.com/64508435/132659603-f95e2a8b-2e7e-4beb-993f-9e5ec7fea23d.png"  width="50%">
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://user-images.githubusercontent.com/64508435/132659695-3c2c14c2-7edd-4109-b8e9-b4cde4cc19d0.jpg" width="45%">
</p>

[(Back to top)](#table-of-contents)


# Part B. Data Structure
- ADTs: designing abstractions
- Data Structures: concrete implementations

# 1. What is Data Structure
- Data Structures are ways to store and organize of data to facilitate efficient
  - Access(Read)
  - Modification(Write)

## 1.1. Abstract Data Type 
- An Abstract Data Type (ADT) is a **mathematical models** of the data structures (DS is implemenetation), which defines
  - Types of data stored
  - Operations that should be supported (For ex: design DS easily to insert and delete)
  - Parameters for the operations
  
[(Back to top)](#table-of-contents)

# 2. Arrays
Array is a continuous chunks of memory. Computer registers:
- **Starting Address**: 0x8600 (0x is prefix for hexadecimal). Address of nth cell =  `starting addr + index*sizeOf(data_type)`
- **Data Type**: of values stored in the cells
- **Size**: How many cells are there
 ![image](https://user-images.githubusercontent.com/64508435/132990483-59c0b12e-54ff-414f-81c4-3b9b7f33600b.png)

[(Back to top)](#table-of-contents)

# 3. Linked List
- **Node**, is a data structure, consists of a value and a pointer to the next node
- **Linked List** is the parent of data structure of node
- Computer registers: head of the Linked List
![image](https://user-images.githubusercontent.com/64508435/132990576-9539acc7-b28f-4bdd-af34-51fe9c408b63.png)

## 3.1. Advantage vs Disadvantage of Linked List
- Advantage: Easy to expand
- Disadvantage:
  - (1) Space: Half of space is wasted on pointer as need to store address of next value (modern computer's address is 8 bytes)
  - (2) Slow to retrieve: as need to jump here and there in the memory (Array you can continuously search and retrieve, say 30th element = starting addr + 30x4 - O(1))
 
## 3.2. Other Linked List Variants
- **Circular Linked List**:  a linked list where all nodes are connected to form a circle. There is no NULL at the end.
- **Doubly Linked List**: usually use both Head & Tail for reversing the list, as Tail will be another Head of the list from the other direction.
<p align="center"><img width="471" alt="Screenshot 2021-09-12 at 22 13 43" src="https://user-images.githubusercontent.com/64508435/132990979-94d48484-a45d-4cdf-81d2-7ce75cb7ae5e.png"></p>

## 3.3. Arrays vs Linked List 
<p align="center"><img width="500" alt="Screenshot 2021-09-12 at 22 13 43" src="https://user-images.githubusercontent.com/64508435/132991388-634a7e19-c5f1-4db6-a24e-57a3d62f014d.png"></p>

- `Lef()`: Linked List O(n) as need to travel from Head to next not me
- `Insert()` and `Delete()`: for Array O(n) as need to shift anything when insert or delete a cell

# 4. Stacks Queues and Deques
## 4.1. ADT Design for Stacks Queues and Deques
- Deques: Since we have 2 ends, so we can enqueue & deque from both the front and back

<p align="center"><img height="300" alt="Screenshot 2021-09-13 at 14 36 43" src="https://user-images.githubusercontent.com/64508435/133035310-89179a0e-417b-4167-bf2f-9444f556f065.png"></p>

## 4.2. Stacks Queues and Deques Implementation using Linked List
- **Stacks**: Singly Linked List with `Head`
- **Queues**: Singly Linked List with `Head` & `Tail`
- **Deques**: Doubly Linked List with `Head` & `Tail`

[(Back to top)](#table-of-contents)

# 5. Dynamic Arrays
## 5.1. Dynamic Array Properties
- **5.1.1. Dynamic Arrays**: a linked list of arrays
  - Which Level ? (i.e: which array): `Array_Index = (pos + 1).bit_length - 1 = h`
  - Which Cell ? (at the particular Array index): `Cell_Index = pos - array_index = pos - (2**h - 1)`
  - For example: pos = 5 &#8594; pos + 1 = 6 = (110) &#8594; bit_len(110) = 3 &#8594; Array_Index = bit_len(110) - 1 = 2. 
    - Therefore, the element @ pos = 5 at 2nd array_index, and the cell index = 5 - (2**2-1) = 2. 

```Python
def __translate(self, pos):
    h = (pos + 1).bit_length() - 1
    return h, pos + 1 – 2 ** h
```

<p align="center"><img height="300" alt="Screenshot 2021-09-13 at 14 36 43" src="https://user-images.githubusercontent.com/64508435/133039495-5d272ebc-37de-4266-91ff-cfc9f90ce519.jpg"></p>

- **5.1.2. Number of Arrays**: `# of arrays = log(capcity + 1)`
  - Capacity = 1 &#8594; 1 array
  - Capacity = 3 &#8594; 2 arrays
  - Capacity = 7 &#8594; 3 arrays

- **5.1.3. Dynamic Arrays in Python**: In Python, the capacity grows ~1/8 of the current size
```Python
def grow(curr_size):
    new_allocated = (curr_size >> 3) + (3 if curr_size < 9 else 6)
    return curr_size + new_allocated
```

## 5.2. Arrays vs Linked Lists vs Dynamic Arrays
<p align="center"><img height="400" src="https://user-images.githubusercontent.com/64508435/133053164-79040b05-a313-4c8f-a754-77b2aad677b0.jpg"></p>

- **Access(i) = O(log(n))**: Since we first we need to travel at most log(n), which is max level of arrays from **5.1.2. Number of Arrays**, then O(1) to access the horizontal position within that array level.
- **Append(i) = O(log(n))**: As we will need to traverse to the last array by log(n) then O(1) to the last position. 
- **Delete & Insert = O(n)**: We need to shift anyone

[(Back to top)](#table-of-contents)

# 6. Tree
- **Tree**: is made up of a single node r (called the `root`) connected to disjoint sets of nodes (called subtrees of r)
- **Internal Node**: A node with at least one child
- **Leaf Node**: A node with no children

#### Level & Heights
- **Level of a Node**:
  - If Root &#8594; Level 0
  - If not Root &#8594; Level of Node = Level of Parent + 1
- **Height of the Tree**: maximum level of its nodes
<p align="center"><img height="150" alt="Screenshot 2021-09-13 at 17 49 55" src="https://user-images.githubusercontent.com/64508435/133063070-bdec5b78-b5f7-4c0a-a646-ce4de7d5dd5d.png"></p>

## 6.1. Binary Tree

<img width="800" alt="Screenshot 2021-09-13 at 17 54 50" src="https://user-images.githubusercontent.com/64508435/133063816-f8800df5-8fe0-4f15-b3a9-76eee34fa442.png">

### 6.1.1. Full Binary Tree vs Complete Binary Tree
- **Full Binary Tree**: Either empty or A node with both left and right subtrees being full binary trees of the same height
  - **# of Nodes** of a full binary tree of height h:  `2^(h) - 1`
<p align="center"><img width="370" alt="Screenshot 2021-09-13 at 18 02 13" src="https://user-images.githubusercontent.com/64508435/133064905-9cbe5430-68da-4274-8ced-6f12c24e13ed.png"></p>

- **Complete Binary Tree**: Left-justified Tree
<p><img width="360" alt="Screenshot 2021-09-13 at 18 02 43" src="https://user-images.githubusercontent.com/64508435/133064954-c07a3416-703d-4439-b970-1d9f1ceb1ef7.png"></p>

[(Back to top)](#table-of-contents)
