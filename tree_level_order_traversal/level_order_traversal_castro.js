#!/usr/bin/env node

const fs = require('fs');

const input = fs.readFileSync('data.json');
const rootNode = JSON.parse(input);

function levelOrder(rootNode) {
  let start = rootNode;

  const queue = [start];
  const result = [];

  while (queue.length) {
    start = queue.shift();

    if (start) {
      result.push(start.data);

      if (start.left) {
        queue.push(start.left);
      }

      if (start.right) {
        queue.push(start.right);
      }
    }
  }

  console.log(result.join(' -> '));
}

levelOrder(rootNode);
