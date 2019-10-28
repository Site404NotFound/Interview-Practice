#! /usr/bin/env python3
def main():
    data = read_file("data.txt")
    specs = clean_data(data)
    print(determine_max_toys(int(specs[0][0]), int(specs[0][1]), list(map(int, specs[1]))))

def read_file(filename):
    with open(filename) as fp:
        data = fp.read().splitlines()
    return data

def clean_data(data):
    cleansed = []
    for line in data:
        cleansed.append(line.split())
    return cleansed

def determine_max_toys(toys, budget, prices):
    max_toys = 0
    total_spent = 0
    prices.sort()
    for price in prices:
        if total_spent + price <= budget:
            total_spent += price
            max_toys += 1
        else:
            break
    return max_toys

if __name__ == "__main__":
    main()