#! /usr/bin/env python3

def main():
    data = read_file("data.txt")
    process_data(data)

def process_data(data):
    stack = []
    length = int(data.pop(0))
    for x in range(length):
        command = data[x].split()
        if int(command[0]) == 1:
            push_into_stack(stack, int(command[1]))
        if int(command[0]) == 2:
            remove_from_stack(stack)
        if int(command[0]) == 3:
            print_max_stack(stack)

def read_file(filename):
    with open(filename) as fp:
        data = fp.read().splitlines()
    return data

def push_into_stack(stack, number):
    stack.append(number)

def remove_from_stack(stack):
    stack.pop()

def print_max_stack(stack):
    print(max(stack))


if __name__ == "__main__":
    main()
