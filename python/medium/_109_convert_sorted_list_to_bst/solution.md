Solution 1: Convert linked list to array then do PreOrder Traversal

Convert linked list to array, then the problem become 108. Convert Sorted Array to Binary Search Tree
Choose arr[mid] as a root
Solve sub problem (left, mid - 1), make it as left node
Solve sub problem (mid + 1, right), make it as right node

Solution 2: Use 2 pointers, one fast and one slow to find the middle in linked-list
recursively create the tree