#!/usr/bin/env node

const fs = require('fs');

const input = fs.readFileSync('data.txt');
let args = input.toString().split("\n");

function rotations(spec, initialState) {
  const args = spec.split(' ');
  const rotate = args[0];
  
  let rotations = args[1];
  let list = initialState.split(' ');

  const rotateIndex = list.indexOf(rotate);
  const newRotateIndex = rotateIndex - (rotate - 1);
  const over = list.length - rotations;

  const state = {};

  state[rotate] = newRotateIndex;

  list.forEach((num, index) => {
    if (num !== rotate) {
      state[num] = index + over;
    }
  });

  const result = Object.keys(state).sort((a, b) => state[a] > state[b]);

  console.log(result.join(' '));
}

rotations(args[0], args[1]);
