#! /usr/bin/env python3

def main():
    specs, numb_list = read_file("data.txt")
    sorted_data = rotations(int(specs[0]), int(specs[1]), numb_list)
    print_results(sorted_data)

def read_file(filename):
    with open(filename) as fp:
        data = fp.read().splitlines()
    return data[0].split(), data[1].split()

def rotations(length, operations, numb_list):
    for x in range(operations):
        temp = numb_list[length - 1]
        for y in range(length - 1):
            numb_list[length - 1 - y] = numb_list[length - 1 - y - 1]
        numb_list[0] = temp
    return numb_list

def print_results(numb_list):
    print(" ".join(numb_list))

if __name__ == "__main__":
    main()
