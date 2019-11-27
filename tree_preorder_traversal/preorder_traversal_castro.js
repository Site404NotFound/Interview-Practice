#!/usr/bin/env node

function preorderTraverse(headNode) {
  let current = headNode;
  let previous = null;
  
  while (current) {
    previous = current;
    
    if (current === headNode) {
      console.log(current.data);
    }
      
    if (current.left) {
      current = current.left;
      console.log(current.data);
    }
    
    if (current.right) {
      current = current.right;
      console.log(current.data);
    }
    
    if (current && (!current.left && !current.right)) {
      current = previous.right;
      console.log(current && current.data);
    }
  }
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

