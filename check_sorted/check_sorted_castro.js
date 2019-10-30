#!/usr/bin/env node

const sortMap = {
  a: 2,  
  b: 1,  
  c: 4,  
  d: 3,
};

function checkSorted(list) {
  const sorted = {};

  list.forEach((sentences, index) => {
    let isSorted = true;

    sentences.sort((a, b) => {
      let newA = '';
      let newB = '';
      let i;

      for (i = 0; i < a.length; i++) {
        newA += sortMap[a[i]];
      }

      for (i = 0; i < b.length; i++) {
        newB += sortMap[b[i]];
      }

      if (newA > newB) {
        isSorted = false;
      }
    });

    sorted[index] = isSorted;
  });

  Object.keys(sorted).forEach((index) => console.log(
    `Sentences ${list[index]} ARE${sorted[index] ? '' : ' NOT'} in alphabetical order!`
  ));
}

checkSorted([
  ['bbb', 'aaa', 'ddd', 'ccc'],
  ['bbb', 'ddd', 'aaa', 'ccc'],
  ['abcd', 'abcda'],
  ['abcda', 'abcd']
]);
