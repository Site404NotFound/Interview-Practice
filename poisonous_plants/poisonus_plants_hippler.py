#! /usr/bin/env python3
'''
Hackerrank Problem:
Poisonous Plants
https://www.hackerrank.com/challenges/poisonous-plants/problem
'''

def main():
    data = read_data("data.txt")
    plants = [int(i) for i in data[1].split()]
    print(", ".join(map(str, plants)))
    alive_plants, days = poisonous_plants(int(data[0]), plants)
    print("Plants stop dying after day {}\nRemaining Plants: {}".format(days, ", ".join(map(str, alive_plants))))

def read_data(filename):
    with open(filename, "r") as fp:
        data = fp.read().splitlines()
    return data

def poisonous_plants(size, plants):
    days = 0
    while True:
        dead_indexes = []
        for x in range(size - 1):
            if plants[x] < plants[x + 1]:
                dead_indexes.insert(0, x + 1)
        if dead_indexes:
            days += 1
            size -= len(dead_indexes)
            for index in dead_indexes:
                del plants[index]
        else:
            return plants, days

if __name__ == "__main__":
    main()