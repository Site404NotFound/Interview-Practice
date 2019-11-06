#! /usr/bin/env python3
'''
Hackerrank Problem:
Tree: Level Order Traversal
hackerrank.com/challenges/tree-level-order-traversal/problem

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
1 2 5 3 6 4
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
    results = traverse(tree.root)
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

def traverse(root):
    found_nodes = [root]
    results = []
    while found_nodes:
        current = found_nodes.pop(0)
        results.append(current.data)
        if current.left_edge: found_nodes.append(current.left_edge)
        if current.right_edge: found_nodes.append(current.right_edge)
    return results

if __name__ == "__main__":
    main()