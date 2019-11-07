#! /usr/bin/env python3

import collections

'''
Hackerrank Problem:
Tree: Top View
https://www.hackerrank.com/challenges/tree-top-view/problem

Sample Input:
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  

Sample Output:
1 2 5 6
'''

class Node():
    def __init__(self, data, has_left, has_right, left_edge=None, right_edge=None):
        self.data = data
        self.has_left = has_left
        self.has_right = has_right
        self.left_edge = left_edge
        self.right_edge = right_edge

class Tree():
    def __init__(self):
        self.root = None
    def add_node(self, data, has_left, has_right):
        if not self.root:
            self.root = Node(data, has_left, has_right)
        else:
            current = self.root
            while current:
                if current.has_left and not current.left_edge:
                    current.left_edge = Node(data, has_left, has_right)
                    break
                elif current.has_right and not current.right_edge:
                    current.right_edge = Node(data, has_left, has_right)
                    break
                elif current.has_left and current.left_edge:
                    current = current.left_edge
                elif current.has_right and current.right_edge:
                    current = current.right_edge
                else:
                    current = None

def main():
    tree = build_tree()
    print_results([find_value_bfs(tree, 4), find_value_dfs(tree, 6)])


def build_tree():
    tree = Tree()                       # Instantiate tree class object
    values = {1 : {"left"  : False,     # Establish values for building tree (map)
                   "right" : True},
              2 : {"left"  : False,
                   "right" : True},
              5 : {"left"  : True,
                   "right" : True},
              3 : {"left"  : False,
                   "right" : True},
              6 : {"left"  : False, 
                   "right" : False},
              4 : {"left"  : False,
                   "right" : False}}
    for data, edges in values.items():
        tree.add_node(data, edges["left"], edges["right"])
    return tree

def find_value_bfs(tree, value):
    found = False
    node_queue = [tree.root]
    path = []
    while node_queue and not found:
        current = node_queue.pop(0)
        path.append(current.data)
        if current.data == value: 
            found = True
        else:
            if current.left_edge: node_queue.append(current.left_edge)
            if current.right_edge: node_queue.append(current.right_edge)
    return [found, path]

def find_value_dfs(tree, value):
    found = False
    node_stack = [tree.root]
    path = []
    while node_stack and not found:
        current = node_stack.pop()
        path.append(current.data)
        if current.data == value: found = True
        else:
            if current.right_edge: node_stack.append(current.right_edge)
            if current.left_edge: node_stack.append(current.left_edge)
    return [found, path]

def print_results(results):
    if results[0][0]: print("TRUE: Value Found with Breadth First Search!\nPATH: {}".format(" -> ".join(map(str, results[0][1]))))
    else: print("FALSE: Value Not Found with Depth First Search.")
    if results[1][0]: print("TRUE: Value Found with Depth First Search!\nPATH: {}".format(" -> ".join(map(str, results[1][1]))))
    else: print("FALSE: Value Not Found with Depth First Search.")

if __name__ == "__main__":
    main()