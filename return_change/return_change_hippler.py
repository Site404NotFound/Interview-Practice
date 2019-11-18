#! /usr/bin/env python3

'''
https://www.youtube.com/watch?v=HWW-jA6YjH
Example:
31 : 1 Quarter (25), 1 Nickle (5), 1 Pennies (1), 0 Dimes (10)
3
'''
def main():
    coins, total = calculate_change(31)
    print_results(coins, total)

def calculate_change(total):
    coins = {"Quarters" : {"value" : 25, "amount" : 0},    # Quarter count
             "Dimes"    : {"value" : 10, "amount" : 0},    # Dime count
             "Nickles"  : {"value" : 5,  "amount" : 0},    # Nickle count
             "Pennies"  : {"value" : 1,  "amount" : 0}}    # Penny count
    total_coins = 0
    for coin, details in coins.items():
        details["amount"] = total // details["value"]
        total_coins += details["amount"]
        total %= details["value"]
    return coins, total_coins

def print_results(coins, total):
    print("Total Coins: {}".format(total))
    for coin, details in coins.items():
        print("{}: {}".format(coin, details["amount"]))
    
if __name__ == "__main__":
    main()