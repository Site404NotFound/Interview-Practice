#! /usr/bin/env python3

def main ():
    data = read_data("data.txt")
    scores = compare_values(data[0].split(), data[1].split())
    print_results(scores)

def read_data(filename):
    with open(filename) as fp:
        data = fp.read().splitlines()
    return data

def compare_values(a, b):
    scores = [0, 0]
    for x in range(min(len(a), len(b))):
        if int(a[x]) > int(b[x]):
            scores[0] += 1
        elif int(b[x]) > int(a[x]):
            scores[1] += 1
        else:
            continue
    if len(a) > len(b):
        for y in range(len(a) - len(b)):
            scores[0] += 1
    if len(b) > len(a):
        for y in range(len(b) - len(a)):
            scores[1] += 1

    return scores

def print_results(scores):
    print(" ".join(map(str, scores)))

if __name__ == "__main__":
    main()
