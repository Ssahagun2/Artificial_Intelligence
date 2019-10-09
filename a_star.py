import heapq
from py.node import Node


class Graph:

    def __init__(self):
        self.graph = {}
        self.heuristics = {}

    def add_node(self, u, edges):
        self.graph[u] = Node(u, edges)

    def add_node_heuristics(self, n, h):
        self.heuristics[n] = h

    def a_star_search(self, start, goals):
        if start in goals:
            return [start]

        nodes = (self.graph[start]).edges
        queue = []
        # Uncomment the line below once you have completed the initialize_queue function
        self.initialize_queue(nodes, queue, start)

        while queue:
            top_node = heapq.heappop(queue)
            tail = top_node[2][0]
            if tail in goals:
                return top_node[2][::-1]
            # Uncomment the line below once you have completed the update_queue function
            self.update_queue(queue, tail, top_node)
        return None

    def initialize_queue(self, nodes, queue, start):
        # Code here
        for key, value in nodes.items():
            gn = value
            fn = self.heuristics[key] + gn
            letters = [key, start]
            tup = (fn, gn, letters)
            queue.append(tup)
        heapq.heapify(queue)

    def update_queue(self, queue, tail, top_node):
        x = self.graph[tail].edges
        path_cost = top_node[1]
        for key, value in x.items():
            cost = value
            new_cost = cost + path_cost
            priority = self.heuristics[key] + new_cost
            heapq.heappush(queue, (priority, new_cost, [key] + top_node[2]))
