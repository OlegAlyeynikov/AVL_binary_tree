# AVL Tree Implementation in Python

This project provides an implementation of an **AVL Tree** — a self-balancing binary search tree that guarantees 
efficient performance for fundamental operations (search, insertion, deletion) in $O(\log n)$ time.

## Features

* **Insertion (`insert`)**: adds a new element while maintaining balance.
* **Deletion (`delete_node`)**: removes a node by key and rebalances the tree.
* **Rotations (`left_rotate`, `right_rotate`)**: ensure AVL properties are preserved.
* **Find minimum node (`min_value_node`)**: used during deletion.
* **Balancing**: updates node heights and balance factors.
* **Returns the sum of all keys in the tree. (`sum_tree`)**
* **Tree visualization (`__str__`)**: provides a readable text representation of the tree.


## Advantages of AVL Trees

* Guaranteed height of $O(\log n)$.
* Fast search, insert, and delete operations.
* Maintains balanced structure regardless of insertion order.

## Applications

* Databases and file systems.
* Caching and indexing.
* Any system requiring efficient operations on dynamic datasets.
