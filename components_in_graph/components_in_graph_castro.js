#!/usr/bin/env node

// NOTE: Work in progress...

function Graph(count) {
  this.count = count;
  this.adjList = new Map();
  
  this.addVertex = (v) => {
    this.adjList.set(v, []);
  };
  
  this.addEdge = (a, b) => {
    this.adjList.get(a).push(b);
    this.adjList.get(b).push(a);
  };
  
  this.connections = () => {
    const keys = this.adjList.keys();
    
    let largest = [];

    const lens = [];
    
    let conn = [];
    let tail = null;
      
    for (let v of keys) {
      let edges = this.adjList.get(v);
      let depth = 0;
      
      while (edges.length) {
        for (let i = 0; i < edges.length; i++) {
          edges = this.adjList.get(edges[i]);
          
          for (let j = 0; j < edges.length; j++) {
            if (!conn.includes(edges[j])) {
              tail = edges;

              conn.push(edges[j]);
              
              edges = this.adjList.get(edges[j]);
            }

            depth++;

            if (depth === count) {
              edges = [];
            }
          }
        }
        
      }
    }
    
    return conn;
  };
}

function componentsInGraph(count, vertices) {
  const graph = new Graph(count);
  const nodes = [];
  
  vertices.forEach(vertex => {
    const [a, b] = vertex;
    
    if (!nodes.includes(a)) {
      nodes.push(a);
      graph.addVertex(a);
    }

    if (!nodes.includes(b)) {
      graph.addVertex(b);
      nodes.push(b);
    }
    
    graph.addEdge(a, b);
  });
  
  console.log(graph.connections().join(' -> '));
  
  console.log('');
  
  console.log(graph);
}

componentsInGraph(5, [
  [1,6],
  [2,7],
  [3,8],
  [4,9],
  [2,6],
]);
