#!/usr/bin/env node

const fs = require('fs');

const input = fs.readFileSync('data.txt');
let args = input.toString().split("\n");

function rotations(spec, initialState) {
  const state = {};

  const args = spec.split(' ');
  const length = args[0];
  const rotations = args[1];
  const list = initialState.split(' ');
  const over = rotations - length;

  list.forEach((num, index) => {
    let newIndex = index - over;

    return state[num] = (newIndex > length - 1)
      ? 0
      : newIndex;
  });

  const result = Object.keys(state).sort((a, b) => state[a] > state[b]);

  console.log(result.join(' '));
}

rotations(args[0], args[1]);
