from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

from tst import TST


class TSTVisualizer:
    """
    takes in a TST, and creates a networkx graph of it. This graph can then be printed to a PNG file
    """
    def __init__(self, _tst):
        self.tst = _tst

    def get_edge_list(self):
        """
        Traverses the TST and adds each edge to a list
        """
        if not self.tst.root:
            return []
        edges = []
        nodes = deque([self.tst.root])
        while nodes:
            node = nodes.popleft()
            if node.left:
                edges.append((node, node.left))
                nodes.append(node.left)
            if node.middle:
                edges.append((node, node.middle))
                nodes.append(node.middle)
            if node.right:
                edges.append((node, node.right))
                nodes.append(node.right)
        return edges

    def get_custom_positions(self):
        """
        Creates custom positions for TST nodes respecting left/middle/right structure
        """
        if not self.tst.root:
            return {}
        positions = {}
        def assign_positions(node, x, y, x_spacing):
            if not node:
                return
            positions[node] = (x, y)
            next_y = y - 1
            next_spacing = x_spacing / 2
            if node.left:
                assign_positions(node.left, x - x_spacing, next_y, next_spacing)
            if node.middle:
                assign_positions(node.middle, x, next_y, next_spacing)
            if node.right:
                assign_positions(node.right, x + x_spacing, next_y, next_spacing)
        assign_positions(self.tst.root, 0, 0, 4.0)
        return positions

    def visualize(self):
        if not self.tst.root:
            return
            
        graph = nx.DiGraph()  # Use directed graph for better visualization
        edges = self.get_edge_list()
        graph.add_edges_from(edges)
        
        pos = self.get_custom_positions()
        labels = {node: str(node) for node in graph.nodes()}
        
        plt.figure(figsize=(12, 8))
        nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=800)
        nx.draw_networkx_labels(graph, pos, labels)
        nx.draw_networkx_edges(graph, pos, arrows=True, arrowsize=20)
        
        plt.title("Ternary Search Tree")
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    words = ['she', 'sells', 'sea', 'shells', 'by', 'shore', 'shell']
    tst = TST()
    for i, word in enumerate(words):
        tst.put(word, i + 1)
    visualizer = TSTVisualizer(tst)
    visualizer.visualize()