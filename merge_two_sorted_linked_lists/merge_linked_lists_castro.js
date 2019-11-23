#!/usr/bin/env node

function getData(node = {}) {
  return node.data;
}

function getNextData(node = {}) {
  return getData(node.next);
}

function shouldMerge(head1, head2) {
  return getData(head1) <= getData(head2) && getData(head2) <= getNextData(head1);
}

function mergeLists(head1, head2) {
  let current1 = head1;
  let current2 = head2;
  let tail = null;
  
  while (current1) {
    if (shouldMerge(current1, current2)) {
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
  
  current1 = head1;
  
  while (current1) {
    console.log(getData(current1));
    current1 = current1.next;
  }
}

// TODO: Build singly linked lists from data.txt

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
