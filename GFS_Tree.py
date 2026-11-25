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


def dfs_preorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    dfs_preorder(node.left, result)
    dfs_preorder(node.right, result)
    return result


def dfs_inorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    dfs_inorder(node.left, result)
    result.append(node.data)
    dfs_inorder(node.right, result)
    return result


def dfs_postorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    dfs_postorder(node.left, result)
    dfs_postorder(node.right, result)
    result.append(node.data)
    return result


def dfs_iterative(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


if __name__ == "__main__":
    print("=== DFS METHODS IN TREE (SALAZAR) ===")
    root = build_tree()
    print("Pre-order  (Root - Left - Right):", " - ".join(dfs_preorder(root)))
    print("In-order   (Left - Root - Right):", " - ".join(dfs_inorder(root)))
    print("Post-order (Left - Right - Root):", " - ".join(dfs_postorder(root)))
    print("Iterative  (using stack)        :", " - ".join(dfs_iterative(root)))