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
- [4. BFS and DFS](#4-bfs-and-dfs)
  - [4.1. BFS](#41-bfs) 
  - [4.2. DFS](#42-dfs) 
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
  - [4.3. Queue](#43-queue)
- [5. Dynamic Arrays](#5-dynamic-arrays)
- [6. Tree](#6-tree)
  - [6.1. Binary Tree](#61-binary-tree) 
  - [6.2. Traverse A Tree](#62-traverse-a-tree)
  - [6.3. Level-order Traversal](#63-level-order-traversal)
  - [6.4. Binary Search Tree](#64-binary-search-tree)
- [7. Heaps](#7-Heaps)
  - [7.1. Heap Representation](#71-heap-representation) 
  - [7.2. Heap Operations](#72-heap-operations)
    - [7.2.1. Heapify](#721-heapify)  
    - [7.2.2. Insertion](#722-insertion)
    - [7.2.3. Pop](#723-pop) 
  - [7.3. Heap Advantage](#73-heap-advantage) 

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

# 4. BFS and DFS
## 4.1. BFS
- **BFS**: needs to use [queue](#43-queue) as processing order of the nodes in First-in-First-out (FIFO) manner.
- **Application**: do [traversal](#63-level-order-traversal) or find the `shortest path from the root node to the target node`
  - Round 1: we process the root node
  - Round 2: we process the nodes next to the root node 
  - Round 3: we process the nodes which are two steps from the root node; so on and so forth.
  - Similar to tree's level-order traversal, the nodes closer to the root node will be traversed earlier.
  - If a **target** node  is added to the queue in the `kth` round, the *length of the shortest path* between the root node and **target** node is exactly `k`. 
  - That is to say, you are already in the shortest path the first time you find the target node.
<p align="center"><img height="280" alt="Screenshot 2021-10-06 at 22 46 16" src="https://user-images.githubusercontent.com/64508435/136227680-d5db434d-35f4-4dfb-8557-5eff2fba8dd9.png"></p>

### 4.1.1. BFS Template 1
- After each outer while loop, we are one step farther from the root node. 
- Variable `step` indicates the distance from the root node and the current node we are visiting.
- `Template 1` not need keep the visited hash set becauese:
  - There is no cycle, for example, in tree traversal
  - You do want to add the node to the queue multiple times.
```Python
def BFS(root, target):
    queue = dequeue()  #store all nodes which are waiting to be processed
    step = 0           #number of steps neeeded from root to current node
    queue.append(root) #append root to queue

    while queue: 
        step = step + 1
        #iterate the nodes which are already in the queue
        size = len(queue)
        for _ in range(size):
            cur_node = queue.popleft() #dequeue the first node in queue
            if cur_node == target: return step #return step if cur is target
            #else: continue to add the neighbors of cur_node to queue
            for (Node next : the neighbors of cur_node):
                add next to queue

    return -1 #there is no path from root to target
```
### 4.1.1. BFS Template 2
- It is important to make sure that we **never visit a node twice**. 
- Otherwise, we might get stuck in an infinite loop, e.g. in graph with cycle. 
- If so, we can add a hash set or other method to mark the node is visted to the code above to solve this problem. For example: [Leetcode: Number of Islands](https://github.com/CodexploreRepo/leetcode/blob/master/solution/200_Number_of_Islands.py)

```Python
def BFS(root, target):
    queue = dequeue()  #store all nodes which are waiting to be processed
    visited = []       #store all the nodes that we've visited
    step = 0           #number of steps neeeded from root to current node
    queue.append(root) #append root to queue

    while queue: 
        step = step + 1
        #iterate the nodes which are already in the queue
        size = len(queue)
        for _ in range(size):
            cur_node = queue.popleft() #dequeue the first node in queue
            if cur_node == target: return step #return step if cur is target
            #else: continue to add the neighbors of cur_node to queue
            for neighbour in cur_node.neighbour:
                if neighbour not in visited: #ensure that the neighbor is not visited
                    visited.append(neighbour)
                    queue.append(neighbour)
                
    return -1 #there is no path from root to target
```

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

## 4.3. Queue
- **Application**: [BFS](#41-bfs)
### 4.3.1. Queue Implementation
- To implement a **queue using dynamic array** and an index pointing to the `head` of the queue.
  - Drawback: With the movement of the `head` pointer when dequeue, more and more space is wasted 
    - In this example, when we dequeue(5), the head pointer move to the second position, but then array[0] pos will never be used 
    - <p align="center"><img height="100" alt="Screenshot 2021-09-13 at 14 36 43" src="https://user-images.githubusercontent.com/64508435/136234975-23a637b1-887e-4109-a55a-819db5c37b02.png"></p>
- Solution: `Circular queue` Specifically, we may use a **fixed-size array** and **two pointers** to indicate the starting position and the ending position. And the goal is to reuse the wasted storage we mentioned previously.
  - Example: [Design Circular Queue](https://github.com/CodexploreRepo/leetcode/blob/master/solution/622_Design_Circular_Queue.py) Please refer the link for [Circular Queue animation]( https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1396/)

### 4.3.2. Queue Usage in Python
- Queue with List: **dequeue** `list.pop(0)` (But requiring O(n) as need to shift all elements) time and **enqueue** `list.append(item)`
- Queue with Built-in Function:
```Python
from collections import deque
q = deque() # Initializing a queue
q.append('a') # Adding elements to a queue
# Removing elements from a queue - only O(1) in compare with using List to implement Queue
q.popleft()
```
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
- From graph view, a tree can also be defined as a directed *acyclic graph* which has `N` nodes and `N-1` edges.

#### Level & Heights
- **Level of a Node**:
  - If Root &#8594; Level 0
  - If not Root &#8594; Level of Node = Level of Parent + 1
- **Height of the Tree**: maximum level of its nodes
<p align="center"><img height="150" alt="Screenshot 2021-09-13 at 17 49 55" src="https://user-images.githubusercontent.com/64508435/133063070-bdec5b78-b5f7-4c0a-a646-ce4de7d5dd5d.png"></p>

## 6.1. Binary Tree
- An empty tree or a node with at most 2 branches
<img width="800" alt="Screenshot 2021-09-13 at 17 54 50" src="https://user-images.githubusercontent.com/64508435/133063816-f8800df5-8fe0-4f15-b3a9-76eee34fa442.png">

### 6.1.1. Full Binary Tree vs Complete Binary Tree
- **Full Binary Tree**: Either empty or A node with both left and right subtrees being full binary trees of the same height
  - **# of Nodes** of a full binary tree of height h:  `2^(h+1) - 1`
<p align="center"><img width="370" alt="Screenshot 2021-09-13 at 18 02 13" src="https://user-images.githubusercontent.com/64508435/133064905-9cbe5430-68da-4274-8ced-6f12c24e13ed.png"></p>

- **Complete Binary Tree**: Left-justified Tree
  -  A completely filled tree on all levels except possibly the lowest level, which is filled from the left. 
  -  A complete binary tree has at most one node with only one child.
<p align="center"><img width="360" alt="Screenshot 2021-09-13 at 18 02 43" src="https://user-images.githubusercontent.com/64508435/133064954-c07a3416-703d-4439-b970-1d9f1ceb1ef7.png"></p>

## 6.2. Traverse A Tree
- **Traversal Type**
  - `Pre-Order`: Root - Left - Right
  - `In-Order` : Left - Root - Right
  ```Python
  class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs_inorder(root, res)
        return res
    def dfs_inorder(self, root, res):
        if (root):
            self.dfs_inorder(root.left, res)
            res.append(root.val)
            self.dfs_inorder(root.right, res)
  ```
  - `Post-Order` : Left - Right - Root
    - Note 1: Delete nodes in a tree, deletion process will be in post-order. That is to say, when you delete a node, you will delete its left child and its right child before you delete the node itself. 
    - Note 2: Post-order is widely use in mathematical expression. 
      -  original expression using the inorder traversal. However, it is not easy for a program to handle this expression since you have to check the priorities of operations. 
      -  If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack. 
![IMG_0012](https://user-images.githubusercontent.com/64508435/133863125-adebc932-f5a5-4cca-a0ff-f60b5143f77f.jpg)

## 6.3. Level-order Traversal
- `Breadth-First Search` is an algorithm is to traverse the tree level by level.
- We will use a queue to help us to do BFS.
  ```Python
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if (root):
            queue = [root]
            while(len(queue) > 0):
                #in order to keep track on Level, we will based on len of queue
                size, cur_level = len(queue), []
                #at level 0, size_level_0 = 1
                #at level 1, size_level_2 = 2
                for _ in range(size):
                    cur_node = queue.pop(0)
                    cur_level.append(cur_node.val)
                    if (cur_node.left):
                        queue.append(cur_node.left)
                    if (cur_node.right):
                        queue.append(cur_node.right)
                res.append(cur_level)
        return res
  ```

## 6.4. Binary Search Tree
- A `binary search tree` (BST), a special form of a binary tree, satisfies the binary search property:
  - The value in each node must be greater than (or equal to) any values stored in its left subtree.
  - The value in each node must be less than (or equal to) any values stored in its right subtree.
- **inorder traversal** in BST will be in **ascending** order
- BSTs support three main operations: search, insertion and deletion.

### 6.4.1. BST - Search
```Python
class Solution:
    def searchBST(self, root, val):
        if (root):
            if root.val == val:
                return root
            elif root.val > val:
                return self.searchBST(root.left, val)
            elif root.val < val:
                return self.searchBST(root.right, val)
        else:
            return None
```

### 6.4.2. BST - Insertion
```Python
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val) #Base Case: Null Node, then return a new Node with "val"
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val) #If root.right is Null, so TreeNode(val) will be returned from Base Case & assign to root.right
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val) #If root.left is Null, so TreeNode(val) will be returned from Base Case & assign to root.left
        return root #return root after insertion
```

### 6.4.3. BST - Deletion
<p align="center"><img width="720" alt="Screenshot 2021-09-23 at 23 40 44" src="https://user-images.githubusercontent.com/64508435/134540702-d7f72f26-6644-438b-a8ae-007c93c6b137.png"></p>

- First, traverse it until `root.val == key`.
- **Case 0**: node do not have any children, like 1, 8, 11, 14, 6 or 18: then we just delete it and nothing else to do here.
- **Case 1**: node has left children, but do not have right, for example 3 or 20. In this case we can just delete this node and put connection betweeen its parent and its children: for example for 3, we put connection 5->1 and for 20 we put connection 17->18. Note, that the property of BST will be fulfilled, because for parent all left subtree will be less than its value and nothing will change for others nodes.
- **Case 2**: node has both children, like 12, 5, 7, 9 or 15. In this case we can not just delete it. 
  - Let us consider node 5. We want to find succesor of this node: the node with next value, to do this we need to go one time to the right and then as left as possible. 
  - For node 5 our succesor will be 6: we go 5->7->6. 
  - How we can delete node 5 now? We swap nodes 5 and 6 (or just put value 6 to 5) and then we need to deal with new tree, where we need to delete node which I put in square. 
  - How to do it? Just understand, that this node do not have left children, so it is either Case 1 or Case 3, which we already can solve.

```Python
class Solution:
    def deleteNode(self, root, key):
        if not root: return None #Base Case
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: #root.val = key
            #Case 0: node has no child
            if not root.left and not root.right: return None 
            
            #Case 1: node has 1 child
            if not root.left: return root.right #if no left child, so right child will replace root
            if not root.right: return root.left #if no right child, so left child will replace root
            
            #Case 2: node has 2 child, will replace root with its successor
            if root.left and root.right:
                #root's succssor = left-most child of the root's right sub-tree
                temp = root.right
                while(temp.left):
                    temp = temp.left
                #replace root with it successor's val 
                root.val = temp.val
                #delete root's succssor: Since root's succssor will have no left child
                #so delete it will fall under case 0, or case 1 only
                root.right = self.deleteNode(root.right, temp.val)
                
        return root          
```


[(Back to top)](#table-of-contents)



# 7. Heaps
<i>definition.</i> A <b>binary heap</b> is a **complete binary tree** with the following binary heap property:
- (1) if the key at a node is greater than or equal to the key of its parent, we call it a <b>min-heap</b>.
- (2) if the key at a node is smaller than or equal to the key of its parent, we call it a <b>max-heap</b>.


## 7.1. Heap Representation
- A heap can be represented by a list with indices **starting from 1**.
- <b><i>example.</i></b> A max-heap in the previous example can be represented by a list `[None, 6, 5, 3, 4, 2, 1]`.

#### Finding Parent & Child
Given a key at position `i`:
- Position of the left child: `2*i`
- Position of the right child: `2*i + 1`
- Position of the parent: `i//2`
  - <b><i>example.</i></b> i = 4, value = 17 &#8594; parent = `i//2` Left Child = `2*i`, Right Child = `2*i+ 1`

#### Height of Heap
- **# of Internal Nodes** = `floor(log(n)) + 1`
- if heap has 1 node it's height will be 1
- if heap has from 2 to 3 nodes it's height will be 2
- if heap has from 4 to 7 nodes it's height will be 3
- ...
- if heap has from 2^i to 2^(i+1) - 1 nodes it's height will be i


#### Internal Nodes vs Leafs
Since Heap is is a **complete binary tree**, therefore:
- **# of Internal Nodes** = `floor(n/2)` or `n//2`
- **# of Leafs** = `# of internal nodes` or `# of internal nodes + 1`

<p align="center"><img width="450" alt="Screenshot 2021-09-14 at 14 56 28" src="https://user-images.githubusercontent.com/64508435/133210030-3107509a-01ff-47fc-8229-fb5eaf4faa22.png"></p>


## 7.2. Heap Operations
- `heapify`: convert an arbitrary list &#8594; a list that satisfies max-heap property. For ex: `[None, 1, 2, 3]` &#8594; `[None, 3, 2, 1]`
- `insert`: insert an element into the list without violating the max-heap property.
- `pop`: retrieve the maximum element of the list.

### 7.2.1. Heapify
- Time Complexity of Heapify: `O(n)` (See Proof Below)
- Time Complexity of Heapify_at(i): `O(log(n))` since worst case, we need to shift down from root to leaf = all levels (h = log(n)) 
<p align="center"><img height="350" alt="Screenshot 2021-09-14 at 14 56 28" src="https://user-images.githubusercontent.com/64508435/133222065-32456143-c209-433f-8a2f-625c1a53ea9e.jpg"></p>

- **Step 1**: Start from the last internal node
  - For a heap of size `n`, there are exactly `n//2` internal node, so we can start checking the max-heap property from the last internal node, with index `n//2` to the root node (index 1).
 ```Python
 def heapify (self):
    for i in range (self.__size // 2, 0, -1):
        self.__heapify_at(i)
 ```
- **Step 2**: Execute  <b>heapify_at(i)</b> for all the internal nodes
  - <b>heapify_at(i)</b> function does is to make sure, every sub-heap rooted at element with position i satisfies the heap property, i.e., the key at the root is not smaller than any other keys in the sub-heap.
  -  <b>try_swap</b> function: if the child key is greater than the parent key, we swap the two keys, and return true for the success of swap action. Otherwise, it is false. The heapify will be notified by the returned true or false, and decide if it is necessary to heapify the sub-heap rooted at the child, since the key has changed smaller.
  ```Python
  def __heapify_at (self, i):
    if 2*i > self.__size: #Base case: There is no left or right child, i.e: it is the leaf node now
        return
    elif 2*i == self.__size: #Case 1: internal node has only child, i.e: this left child (2*i) at the end of the list
        if self.__try_swap(i, 2*i):
            __heapify_at(2*i) 
    elif self.__content[2*i] > self.__content[2*i+1]: #Case 2.1: internal node has 2 child & left child is larger
        if self.__try_swap(i, 2*i): 
            __heapify_at(2*i) #Swap i with its left child and perform heapify_at(its_left_child)
    else: #Case 2.2: internal node has 2 child &  right child is larger
        if self.__try_swap(i, 2*i+1):
            __heapify_at(2*i+1) #Swap i with its right child and perform heapify_at(its_right_child)
  ```
  ```Python
  def __try_swap(self, i,j):
    if self.__content[i] >= self.__content[j]: #if value_at_i > value_at_j, dont need to swap as Parent > its child
        return False
    else:
        self.__content[i], self.__content[j] = self.__content[j], self.__content[i] #if parent < child, need to swap
        return True
  ```
  
#### Proof Time Complexity of Heapify is O(n)
<p align="center"><img height="350" alt="Screenshot 2021-09-14 at 14 56 28" src="https://user-images.githubusercontent.com/64508435/133271150-3d1f9b3d-2f6e-4db7-b58e-bae6d43eb681.jpg"></p>

### 7.2.2. Insertion
- Time Complexity of Insertion: `O(log(n))` since worst case, we need to shift up from left to root = all levels (h = log(n))
- <b>insert</b> is to append a new element at the end of the list. 
- After we inserted this new element, we have to check if it is larger than its parent, 
  - if yes, we swap it with the parent, until the next parent is larger. 
  - The <b>try_swap</b> function is used here to break the loop when the parent contains a larger key.
```Python
def insert (self, k):
    self.__size += 1
    i = self.__size
    self.__content[i] = k
    while i > 1 and self.__try_swap(i // 2, i):
        i = i // 2
```

### 7.2.3. Pop
- Time Complexity of Insertion: `O(log(n))` as same as T(heapify_at(root))
- <b>pop</b> is to return the maximum key in the heap, which is contained in the root of the heap, at index 1. 
- However, we cannot leave the heap without its root. 
- So the last element of the heap is now put at the root, and 
- this is followed by <b>heapify_at</b> to maintain the heap property.

```Python
def pop (self):
    if self.__size == 0:
        return None
    else:
        k = self.__content[1]
        self.__content[1], self.__content[self.__size] = self.__content[self.__size], None
        self.__size -= 1
        self.__heapify_at(1)
        return k
```

## 7.3. Heap Advantage
Question: For a priority queue, where does the saving come from using heap extract and insert instead of merge sort?
- Since priority queue problem is to extract the maximum
- Using heap, we can use **heapify**, which take `O(n)`, to maintain the max heap, say `10 9 7 8 4 5 3` (&#8594; this is *partially sorted order*) &#8594; then we can extract the maximum `10`.
- Meanwhile, if using **merge sort**, which will take `O(nlogn)`, to maintain *totally sorted order*, say `10 9 8 7 5 4 3` &#8594; then we can extract the maximum `10`.
- Answer: depend on the use-case, for this use-case, we only need to maintain *partially sorted order*, so using Heap `O(n)` is Better than Merge Sort `O(nlogn)`

[(Back to top)](#table-of-contents)
