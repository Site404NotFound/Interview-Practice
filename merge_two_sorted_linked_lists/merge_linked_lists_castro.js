#!/usr/bin/env node

const fs = require('fs');

const buff = fs.readFileSync('data.txt');
const data = buff.toString().split("\n");

let index = 1;
let lists = null;

for (const i in Array(parseInt(data[0])).fill()) {
  lists = [new SinglyLinkedList(), new SinglyLinkedList()];

  for (const listIndex in lists) {
    index = makeLinkedList(lists[listIndex], data, index);
  }

  let current = mergeLists(lists[0].head, lists[1].head);

  const out = [];

  while (current) {
    out.push(getData(current));
    current = current.next;
  }

  console.log(out.join(' '));
}

function Node(data, next) {
  this.data = data;
  this.next = next;
}

function SinglyLinkedList() {
  this.head = null;

  this.addNode = (data) => {
    if (!this.head) {
      this.head = new Node(data);
    } else {
      let current = this.head;

      while (current.next) {
        current = current.next;
      }

      current.next = new Node(data);
    }
  };
}

function range(start, end) {
  return new Array(end - start + 1).fill().map((_, i) => i + start);
}

function makeLinkedList(list, data, index) {
  const size = parseInt(data[index]);
  const start = index + 1;
  const end = start + size;

  range(start, end - 1).forEach((i) => list.addNode(parseInt(data[i])));

  return index + size + 1;
}

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
  const lists = [head1, head2].sort((a, b) => a.data > b.data);
  let current1 = lists[0];
  let current2 = lists[1];
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

  return lists[0];
}
