def find_gcd_euclidean(a,b):
    """Topic: Math"""
    """Find GCD using Euclidean algorithm, a,b > 0"""
    while b:
        a, b = b, a % b
    return a

def count_frequency(lst):
    """Topic: Hash map"""
    """Count frequency of elements in a list and return as a dictionary"""
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def dfs(node, state):
    """Topic: Graph traversal"""
    """Depth-first search template for binary tree"""
    if node is None:
        "Some code"
        return
    left = dfs(node.left, state)
    right = dfs(node.right, state)
    "Some code"
    return "Some code"

def dfs(start_index, path):
    """
    Topic: Backtracking
    Backtracking template to explore all paths from start_index to leaf nodes.
    """
    def is_leaf(index):
    # Define your own leaf condition
        return 
  
    def get_edges(index):
    # Define your own edges retrieval
        return []
  
    if is_leaf(start_index):
    # report(path) #do something with the path here
        return
  
    for edge in get_edges(start_index):
        path.add(edge)
        dfs(start_index + 1, path)
        path.pop()
