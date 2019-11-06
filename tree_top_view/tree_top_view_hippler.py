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
    results = top_view(tree.root)
    print(" -> ".join(map(str, results)))

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

def top_view(root):
    results = []
    if root:
        results.append(root.data)
        found_nodes = [[root.left_edge, True], [root.right_edge, False]]
        while found_nodes:
            current = found_nodes.pop(0)
            if current[0]: 
                results.append(current[0].data)
                if current[0] and current[1] and current[0].left_edge: found_nodes.append([current[0].left_edge, True])
                if current[0] and not current[1] and current[0].right_edge: found_nodes.append([current[0].right_edge, False])
    return results

if __name__ == "__main__":
    main()