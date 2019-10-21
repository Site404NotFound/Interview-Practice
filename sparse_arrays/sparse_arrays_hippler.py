#! /usr/bin/env python3

def main():
    for x in range(1, 4):
        data = read_data("data_{}.txt".format(x))
        search_specs = clean_data(data)
        results = perform_search(search_specs[0], dict.fromkeys(search_specs[1], 0))
        print_results(x, results)

def read_data(filename):
    with open(filename) as fp:
        data = fp.read().splitlines()
    return data

def clean_data(data):
    all_values = []
    index = 0
    for x in range(2):
        values = []
        length = int(data[index])
        for y in range(index + 1, index + 1 + length):
            values.append(data[y])
        all_values.append(values)
        index += (index + 1 + length)
    return all_values

def perform_search(strings, queries):
    for string in strings:
        if string in queries: queries[string] += 1
    return queries

def print_results(example, results):
    print("Example {} Results".format(example))
    for key, value in results.items():
        print(value)

if __name__ == "__main__":
    main()
