const fs = require('fs');

const input = fs.readFileSync('data_1.txt');
let args = input.toString().split("\n")

function compareValues(aStr, bStr) {
  let a = aStr.split(' ');
  let b = bStr.split(' ');
  let len = Math.max(a.length, b.length);
  let index = 0;
  let aScores = {};
  let bScores = {};

  while (len--) {
    aScores[index] = !aScores[index] ? 0 : aScores[index];
    bScores[index] = !bScores[index] ? 0 : bScores[index];

    if (a[index] > b[index]) {
      aScores[index] = aScores[index] + 1;
    } else if (a[index] < b[index]) {
      bScores[index] = bScores[index] + 1;
    } else {
      // do nothing
    }

    index++;
  }

  const aScoreOut = Object.keys(aScores).map((index) => aScores[index]);
  const bScoreOut = Object.keys(bScores).map((index) => bScores[index]);

  console.log(aScoreOut.join(' '));
  console.log(bScoreOut.join(' '));
}

compareValues(args[0], args[1]);
