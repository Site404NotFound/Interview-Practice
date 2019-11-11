def traverse(root):
  queue = [root]
  results = []
  while(len(queue)):
    node = queue.pop(0)
    results.append(node.data)
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
  return results

def prints_results(data):
  print(" -> ".join(map(str, data)))