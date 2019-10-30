#! /usr/bin/env python3
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return repr(self.data)

class Singly_Linked_List:
    def __init__(self):
        self.head = None
    def add_node(self, data):
        if not self.head:
            self.head = Node(data = data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data=data)
    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return ", ".join(nodes)

def main():
    data = read_data("data.txt")
    index = 1
    for _ in range(int(data[0])):
        linked_lists = [Singly_Linked_List(), Singly_Linked_List()]
        for linked_list in linked_lists:
            index = build_linked_list(linked_list, data, index)
        print(merge_lists(linked_lists[0], linked_lists[1]))

def read_data(filename):
    with open(filename) as fp:
        data = fp.read().splitlines()
    return data

def build_linked_list(linked_list, data, index):
    size = int(data[index])
    for numbers in range(index + 1, index + 1 + size):
        linked_list.add_node(int(data[numbers]))
    return index + size + 1

def merge_lists(list_1, list_2):
    sorted_list = Singly_Linked_List()
    node_1 = list_1.head
    node_2 = list_2.head
    while node_1 or node_2:
        if node_1 and not node_2:
            sorted_list.add_node(node_1)
            node_1 = node_1.next
        elif node_2 and not node_1:
            sorted_list.add_node(node_2)
            node_2 = node_2.next
        elif node_1.data <= node_2.data:
            sorted_list.add_node(node_1)
            node_1 = node_1.next
        else:
            sorted_list.add_node(node_2)
            node_2 = node_2.next
    return sorted_list

if __name__ == "__main__":
    main()