#/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
    
    def __repr__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            queue = deque([self.root])
            while True:
                current = queue.popleft()
                if current.left is None:
                    current.left = node
                    break
                if current.right is None:
                    current.right = node
                    break
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        self.size += 1
            
    def extract(self):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            yield node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.data == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def display_subtree(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.data != data:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                list_nodes = []
                queue = deque([node])
                while len(queue) > 0:
                    node = queue.popleft()
                    list_nodes.append(node.data)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                print(list_nodes)

    def pop_subtree(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.left.data == data:
                subtree_root = node.left
                node.left = None
                break
            if node.right.data == data:
                subtree_root = node.right
                node.right = None
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        queue = deque([subtree_root])
        list_nodes = []
        while len(queue) > 0:
            node = queue.popleft()
            list_nodes.append(node.data)
            self.size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)   
        return list_nodes

    def display_leaves(self):
        leaves = []
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if (node.left is None) and (node.right is None):
                leaves.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(leaves)
    
    def pop_leaf(self, data):
        if self.search(data):
            queue = deque([self.root])
            while len(queue) > 0:
                node = queue.popleft()
                if node.left.data == data and (node.left.left is None) and (node.left.right is None):
                    leaf = node.left.data
                    node.left = None
                    self.size -= 1
                    return leaf
                if node.right.data == data and (node.right.left is None) and (node.right.right is None):
                    leaf = node.right.data
                    node.right = None
                    self.size -= 1
                    return leaf
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        else:
            return None
        
    def min_node(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def max_node(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def level_node(self, data):
        if self.search(data):
            queue = deque([self.root])
            depth = 0
            c = 0
            while len(queue) > 0:
                layer = 2 ** depth
                node = queue.popleft()
                if data == node.data:
                    return depth
                c += 1
                queue.append(node.left)
                queue.append(node.right)
                if c == layer:
                    depth += 1
                    c = 0
        else:
            return None

    def height(self):
        queue = deque([self.root])
        depth = 0
        c = 0
        heights = [] 
        while len(queue) > 0:
            layer = 2 ** depth
            node = queue.popleft()
            heights.append(depth)
            c += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if c == layer:
                depth += 1
                c = 0
        return max(heights)

    def width(self):
        queue = deque([self.root])
        depth = 0
        c = 0
        width = []
        while len(queue) > 0:
            layer = 2 ** depth
            node = queue.popleft()
            c += 1
            width.append(c)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if c == layer:
                depth += 1
                c = 0
        return max(width)
    
    def flush(self):
        self.root = None
        self.size = 0
