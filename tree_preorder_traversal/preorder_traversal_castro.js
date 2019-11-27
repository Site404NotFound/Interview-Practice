#!/usr/bin/env node

function preorderTraverse(headNode) {
  const result = [];

  let current = headNode;
  let previous = null;
  
  while (current) {
    previous = current;
    
    if (current === headNode) {
      result.push(current.data);
    }
      
    if (current.left) {
      current = current.left;
      result.push(current.data);
    }
    
    if (current.right) {
      current = current.right;
      result.push(current.data);
    }
    
    if (current && (!current.left && !current.right)) {
      current = previous.right;
      result.push(current && current.data);
    }
  }
  
  console.log(result.join(' '));
}

preorderTraverse({
  data: 1,
  right: {
    data: 2,
    right: {
      data: 5,
      right: {
        data: 6
      },
      left: {
        data: 3,
        right: {
          data: 4
        }
      }
    }
  }
});

