#! /usr/bin/env python3

'''
Description:
Interview question via @Site404NotFound

Sample Input:
Sum = 10
Array = [2, 7, 5, 3, 2]
'''

def main():
    sum_total = 10
    numb_list = [2, 7, 5, 3, 2]
    result, values = find_sum(sum_total, numb_list)
    print_results(result, values, sum_total, numb_list)

def find_sum(sum_total, numb_list):
    current_values = []
    index = 0
    result = 0
    while index < len(numb_list):
        result += numb_list[index]
        current_values.append(numb_list[index])
        if result <= sum_total:
            if sum_total == 10 and len(current_values) >= 3:
                return True, current_values
            else:
                index += 1
        else:
            current_values = []
            result = 0
    return False

def print_results(results, values, sum_total, numb_list):
    if results:
        print("{}: The following string of numbers from {} equals {}.\n{}".format(str(results).upper(),  numb_list, sum_total, ", ".join(map(str, values))))
    else:
        print("{}: No string of numbers from {} equals {}.".format(str(results).upper(),  numb_list, sum_total, ))

if __name__ == "__main__":
    main()
