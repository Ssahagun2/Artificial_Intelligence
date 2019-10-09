from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add edge from u to v here
        self.graph[u].append(v)

    def breadth_first_search(self, start, goal):
        # If start is the goal, return start as the path here
        if start == goal:
            path = start
            return path
        visited = {start}
        queue = [(start, [])]

        while queue:
            current, path = queue.pop(0)
            # Add current node to the visited set of nodes here
            visited.add(current)
            for child in self.graph[current]:
                # if child is the goal, return the path with the current node and child node appended here
                if child == goal:
                    path.append(current)
                    path.append(child)
                    return path
                if child not in visited:
                    queue.append((child, path + [current]))
                    # Add child to the visited set here
                    visited.add(child)
        return None

if __name__ == '__main__':
    g = Graph()
    g.add_edge('S', 'A')
    g.add_edge('S', 'F')
    g.add_edge('A', 'C')
    g.add_edge('F', 'G')