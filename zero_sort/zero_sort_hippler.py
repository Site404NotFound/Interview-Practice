#! /usr/bin/env python3

'''
Description:
Interview question via @Site404NotFound

Sample Input:
Array = [0, 5, 6, -1, 0, 0, -4, 5, 1]

Sample Output:
[5, 6, -1, -4, 5, 1, 0, 0, 0]
'''


def main():
    numb_list = [[0, 5, 6, -1, 0, 0, -4, 5, 1],
                 [5, 6, -1, -4, 5, 1],
                 [0],
                 [1],
                 [0, 0, 0, 0, 0, 1, 0, 0]]
    for x in numb_list:
        print_results("Original", x)
        zero_sort(x)
        print_results("Sorted", x)

def zero_sort(numb_list):
    zero_count = 0
    if 0 not in numb_list or len(numb_list) <= 1:
        return numb_list
    else:
        for x in range(len(numb_list)):
            if numb_list[x] == 0:
                zero_count += 1
            else:
                numb_list[x - zero_count] = numb_list[x]
        for y in range(len(numb_list) - zero_count, len(numb_list)):
            numb_list[y] = 0
    return numb_list

def print_results(version, numb_list):
    print("{} List: {}".format(version, ", ".join(map(str, numb_list))))

if __name__ == "__main__":
    main()
