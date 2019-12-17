#!/usr/bin/env node

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

  this.getComponentsResult = () => {
    const keys = this.adjList.keys();
    
    let components = {};
    let edgeHistory = [];
    let head = [];
    let tail = [];
    let last = null;
    let current = null;
    let previous = null;

    for (let v of keys) {
      let edges = this.adjList.get(v).concat([v]);
      
      let depth = 0;

      head = edges;
      
      while (edges.length) {
        for (let i = 0; i < edges.length; i++) {
          edges = this.adjList.get(edges[i]).concat([v]);

          for (let j = 0; j < edges.length; j++) {
            if (!edgeHistory.includes(edges[j])) {
              edgeHistory.push(edges[j]);
              
              last = edges[j];

              const edgetopush = edges[j];
              
              const lastHead = head.concat([last]);
              
              edges = this.adjList.get(edges[j]).concat([v]);

              if (!Object.keys(components).some(c => components[c].some(n => lastHead.includes(n)))) {
                previous = current;
                current = edgetopush;
                
                edgeHistory = [];
                
                components[current] = [];
              }

              if (!components[current].includes(edgetopush)) {
                components[current].push(edgetopush);
              }

              tail = lastHead;
            }

            depth++;

            if (depth === count) {
              edges = [];
            }
          }
        }
      }
    }

    return {
      sizes: Object.keys(components).map(c => components[c].length),
      components,
    };
  };
}

function componentsInGraph(vertices) {
  const count = vertices.length;
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
  
  const result = graph.getComponentsResult();
  
  return [Math.min.apply(this, result.sizes), Math.max.apply(this, result.sizes)];
}

console.log(
  componentsInGraph([
    /*[1, 17],
    [5, 13],
    [7, 12],
    [5, 17],
    [5, 12],
    [2, 17],
    [1, 18],
    [8, 13],
    [2, 15],
    [5, 20],*/
    [1, 6],
    [2, 7],
    [3, 8],
    [4, 9],
    [2, 6],
  ])
);
