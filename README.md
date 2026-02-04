# Binary Search Tree (BST) in Python

## About the Project

This project implements a **Binary Search Tree (BST)** using pure Python. The goal is to demonstrate how tree data structures work, including value insertion and different types of tree traversal such as **preorder**, **inorder**, and **postorder**.

---

## 🔄 Tree Traversal Types

Traversal refers to the process of visiting all nodes in a tree. There are three main types:

---

### 🔵 Inorder (Left → Root → Right)

Visits the left subtree first, then the current node, and finally the right subtree. Important characteristic: in a BST, **inorder traversal returns values in sorted order**.

---

### 🟢 Preorder (Root → Left → Right)

Visits the root node first, then the left subtree, and finally the right subtree. Commonly used for copying trees or serialization.

---

### 🟣 Postorder (Left → Right → Root)

Visits the children first and leaves the root for last. Often used in deletion operations or memory cleanup.
