"""
Assessment 3.4: Non-linear Data Structure
Name used: SALAZAR  ->  S, A, L, A, Z, A, R
Because the letter A appears 3 times, each repeat is numbered (A1, A2, A3)
so every node is unique.
"""
from collections import deque


# ------------------------------------------------------------------
# DIAGRAM 1: BINARY TREE
#
#              S                 level 0
#            /   \
#          A1      L             level 1
#         /  \    /  \
#       A2    Z  A3    R         level 2
# ------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    root = Node("S")
    root.left = Node("A1")
    root.right = Node("L")
    root.left.left = Node("A2")
    root.left.right = Node("Z")
    root.right.left = Node("A3")
    root.right.right = Node("R")
    return root


def tree_bfs(root):
    """Breadth-First: visit level by level using a queue."""
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def tree_dfs(node, result=None):
    """Depth-First (pre-order): Root -> Left -> Right using recursion."""
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    tree_dfs(node.left, result)
    tree_dfs(node.right, result)
    return result


# ------------------------------------------------------------------
# DIAGRAM 2: GRAPH
#
#            S
#         /  |  \
#       A1   Z   L
#       |    |   |
#       A2   A3--+
#       |
#       R
#
# Edges: S-A1, S-Z, S-L, A1-A2, A2-R, Z-A3, L-A3
# ------------------------------------------------------------------
def build_graph():
    graph = {
        "S":  ["A1", "Z", "L"],
        "A1": ["S", "A2"],
        "Z":  ["S", "A3"],
        "L":  ["S", "A3"],
        "A2": ["A1", "R"],
        "A3": ["Z", "L"],
        "R":  ["A2"],
    }
    return graph


def graph_bfs(graph, start):
    """Breadth-First: visit nearest vertices first using a queue."""
    visited = [start]
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


def graph_dfs(graph, vertex, visited=None):
    """Depth-First: go as deep as possible, then backtrack (recursion)."""
    if visited is None:
        visited = []
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited)
    return visited


# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=== BINARY TREE (SALAZAR) ===")
    root = build_tree()
    print("BFS:", " - ".join(tree_bfs(root)))
    print("DFS:", " - ".join(tree_dfs(root)))

    print("\n=== GRAPH (SALAZAR) ===")
    g = build_graph()
    print("BFS:", " - ".join(graph_bfs(g, "S")))
    print("DFS:", " - ".join(graph_dfs(g, "S")))