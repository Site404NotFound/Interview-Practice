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

  this.getComponents = () => {
    const keys = this.adjList.keys();
    const sizes = [];

    let comp = {};
    let conn = [];
    let edgeHistory = [];
    let head = [];
    let tail = [];
    let last = null;
    let current = null;
    let previous = null;

    let loops = 0;

    for (let v of keys) {
      loops++;

      let edges = this.adjList.get(v);
      let depth = 0;

      head = edges;
      
      while (edges.length) {
        loops++;

        for (let i = 0; i < edges.length; i++) {
          loops++;

          edges = this.adjList.get(edges[i]);

          for (let j = 0; j < edges.length; j++) {
            loops++;

            if (!edgeHistory.includes(edges[j])) {
              edgeHistory.push(edges[j]);
              last = edges[j];
            }

            if (!conn.includes(edges[j])) {
              const edgetopush = edges[j];
              const lastHead = head.concat([last]);
              
              edges = this.adjList.get(edges[j]);

              if (!tail.some(n => lastHead.includes(n))) {
                previous = current;
                current = edgetopush;

                comp[current] = [];

                if (previous) {
                  sizes.push(comp[previous].length);
                }
              }

              if (!comp[current].includes(edgetopush)) {
                comp[current].push(edgetopush);
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
      loops,
      smallestCount: Math.min.apply(this, sizes),
      largestCount: Math.max.apply(this, sizes),
      components: comp,
    };
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

  console.log(graph.getComponents());
}

componentsInGraph(7, [
  [1,6],
  [2,7],
  [3,8],
  [4,9],
  [2,6],
  [11,13],
  [13,18]
]);
