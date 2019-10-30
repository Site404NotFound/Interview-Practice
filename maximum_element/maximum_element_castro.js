#!/usr/bin/env node

const fs = require('fs');

const input = fs.readFileSync('data.txt');
const queries = input.toString().split("\n");

const QUERY_TYPE_1 = '1';
const QUERY_TYPE_2 = '2';
const QUERY_TYPE_3 = '3';

const QUERY_TYPES = [
  QUERY_TYPE_1,
  QUERY_TYPE_2,
  QUERY_TYPE_3,
];

function maxElement() {
  const stack = [];

  queries.forEach((query, index) => {
    const parts = query.split(' ');
    const type = QUERY_TYPES.indexOf(parts[0]);

    switch (QUERY_TYPES[type]) {
      case QUERY_TYPE_1: {
        stack.push(parts[1]);
        break;
      }
      case QUERY_TYPE_2: {
        stack.pop();
        break;
      }
      case QUERY_TYPE_3: {
        console.log(Math.max.apply(this, stack));
        break;
      }
    }
  });
}

maxElement(queries);
