
'''
Description:
Interview question via @Site404NotFound

Sample Input:
Sum = 10
Array = [2, 7, 5, 3, 2]
'''


def find_sum(sum, numb_list):
  index = 0
  result = 0
  numbers = 0
  while index < len(numb_list):
    result += numb_list[index]
    number += 1
    if results <= sum:
      if sum == 10 and index >= 3: 
        return True
      else:
        index += 1
    else: 
      results = 0
      numbers = 0
  return False
