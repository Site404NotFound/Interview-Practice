
/*
Description:
Interview question by @Site404NotFound

Sample Input:
Array = [0, 5, 6, -1, 0, 0, -4, 5, 1]

Sample Output:
[5, 6, -1, -4, 5, 1, 0, 0, 0]
*/


function zeroSort(arr) {
  let zeroes = 0;

  arr.forEach((num, index) => {
    if (num === 0) {
      zeroes++;
    } else {
      arr[index - zeroes] = num;
    }

    if (index === arr.length - 1) {
      let start = arr.length - zeroes - 1;

      arr.slice(start, arr.length).forEach((num, index) => {
        arr[index] = 0;
      });
    }
  });

  return arr;
}
