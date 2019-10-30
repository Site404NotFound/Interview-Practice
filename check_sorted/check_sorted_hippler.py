#! /usr/bin/env python3

def main():
    sentences = [["bbb", "aaa", "ddd", "ccc"],
                 ["bbb", "ddd", "aaa", "ccc"],
                 ["abcd", "abcda"],
                 ["abcda", "abcd"]]
    for sentence in sentences:
        print_results(check_sorted(sentence), sentence)

def check_sorted(sentences):
    numb_values = {"a" : 2,     # Establish Map with custom letter priority values
                   "b" : 1,
                   "c" : 4,
                   "d" : 3}
    for words in range(len(sentences) - 1):     # Loop through each word in our list of sentences
        for letters in range(min(len(sentences[words]), len(sentences[words + 1]))):   # Loop through each letter of the current and next work (use min to avoid out of bound memory)
            if numb_values[sentences[words][letters]] > numb_values[sentences[words + 1][letters]]:
                return False
        if len(sentences[words]) > len(sentences[words + 1]):
            return False
    return True

def print_results(results, sentence):
    if results:
        print("TRUE: Sentences {} ARE in alphabetical order!".format(", ".join(sentence)))
    else:
        print("FALSE: Sentences {} ARE NOT in alphabetical order!".format(", ".join(sentence)))

if __name__ == "__main__":
    main()
