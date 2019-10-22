
/*
Description:
Interview question via @Site404NotFound

Sample Input:
Sum = 10
Array = [2, 7, 5, 3, 2]
*/


function findSum(arr, sum) {
  let min = 3;
  let result = 0;
  let meetsSum = false;

  let len = arr.length;
  let index = 0;

  while (len--) {
    result += arr[index];

    if (index+1 >= min && result === sum) {
      meetsSum = true;
      return false;
    }

    if (result > sum) {
      result = arr[index];
    }

    index++;
  }

  return meetsSum;
}
