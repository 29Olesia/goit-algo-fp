import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal='dfs'):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}

    if traversal == 'dfs':
        dfs_traversal(tree, tree_root, pos)
    elif traversal == 'bfs':
        bfs_traversal(tree, tree_root, pos)
    else:
        raise ValueError("Invalid traversal type. Choose 'dfs' or 'bfs'.")

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=range(len(tree.nodes())), font_color='white')  # Set font_color to white
    plt.title(f"Tree Visualization ({traversal.upper()} Traversal)")
    plt.show()

def dfs_traversal(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            dfs_traversal(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            dfs_traversal(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def bfs_traversal(graph, root, pos):
    queue = [(root, 0, 0)]
    visited = set()
    level_width = {}  
    while queue:
        node, x, y = queue.pop(0)
        if node not in visited:
            visited.add(node)
            graph.add_node(node.id, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                queue.append((node.left, x - 1, y - 1))
                level_width[y - 1] = level_width.get(y - 1, 0) + 1
                pos[node.left.id] = (x - level_width[y - 1] * 0.5, y - 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                queue.append((node.right, x + 1, y - 1))
                level_width[y - 1] = level_width.get(y - 1, 0) + 1
                pos[node.right.id] = (x + level_width[y - 1] * 0.5, y - 1)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

draw_tree(root, traversal='dfs')

draw_tree(root, traversal='bfs')
