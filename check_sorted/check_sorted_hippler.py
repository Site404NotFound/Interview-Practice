#! /usr/bin/env python3

def check_sorted(sentences):
    numb_values = {'a' = 2,
                   'b' = 1,
                   'c' = 4,
                   'd' = 3}
    for x in range(len(sentences) - 1):
        for y in range(len(sentences[x])):
            if numb_values[sentences[x[y]]] < numb_values[sentences[x[y]] + 1]:
                return False
            if len(sentences) > len(sentences + 1):
                return False
    return True

sentences = ['acdb', 'cba', 'cccc', 'badc']
check_sorted(sentences)
