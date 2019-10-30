#!/usr/bin/env node

const sortMap = {
  a: 2,  
  b: 1,  
  c: 4,  
  d: 3  
};

function checkSorted(list) {
  let isSorted = true;

  list.sort((a, b) => {
    let newA = '';
    let newB = '';

    a.split('').forEach((letter) => {
      newA += sortMap[letter];
    });

    b.split('').forEach((letter) => {
      newB += sortMap[letter];
    });

    if (a < b) {
      isSorted = false;
    }
  });

  console.log(isSorted);
}

checkSorted(['acdb', 'dcba', 'cccc', 'badc']);
