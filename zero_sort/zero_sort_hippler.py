

'''
Description:
Interview question via @Site404NotFound

Sample Input:
Array = [0, 5, 6, -1, 0, 0, -4, 5, 1]

Sample Output:
[5, 6, -1, -4, 5, 1, 0, 0, 0]
'''


def zero_sort(numb_list):
  zero_count = 0
  if not numb_list.contains(0): return numb_list
  for x in range(len(numb_list)):
    if numb_list[x] == 0: zero_count += 1
    else:
      numb_list[x - zero_count] = numb_list[x]
  for y in range(len(numb_list) - zero_count, len(numb_list)):
    numb_list[y] = 0
