#!/usr/bin/env node

function getData(node = {}) {
  return node.data;
}

function getNextData(node = {}) {
  return getData(node.next);
}

function shouldInsert(root1, root2) {
  return getData(root1) <= getData(root2) && getData(root2) <= getNextData(root1);
}

function mergeLists(root1, root2) {
  let current1 = root1;
  let current2 = root2;
  let tail = null;
  
  while (current1) {
    if (shouldInsert(current1, current2)) {
      tail = current2.next;
      current2.next = current1.next;
      current1.next = current2;
      current2 = tail;
    }
    
    if (!current1.next) {
      current1.next = tail;
      break;
    }

    current1 = current1.next;
  }
  
  current1 = root1;
  
  while (current1) {
    console.log(getData(current1));
    current1 = current1.next;
  }
}

// TODO: Generate linked lists from data.txt

mergeLists({
  data: 1,
  next: {
    data: 2,
    next: {
      data: 3
    }
  }
}, {
  data: 3,
  next: {
   data: 4
  }
});
