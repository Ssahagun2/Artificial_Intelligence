from py.a_star import Graph


def add_nodes(g):
    g.add_node('S', {'A': 3, 'B': 7})
    g.add_node('A', {'C': 1, 'D': 6})
    g.add_node('B', {'E': 1, 'G2': 9})
    g.add_node('C', {'D': 4, 'S': 2})
    g.add_node('D', {'G1': 6, 'B': 3})
    g.add_node('E', {'G2': 5})
    g.add_node('G1', {'C': 2})
    g.add_node('G2', {'B', 8})


def add_heuristics(g):
    g.add_node_heuristics('S', 10)
    g.add_node_heuristics('A', 5)
    g.add_node_heuristics('B', 4)
    g.add_node_heuristics('C', 3)
    g.add_node_heuristics('D', 2)
    g.add_node_heuristics('E', 4)
    g.add_node_heuristics('G1', 0)
    g.add_node_heuristics('G2', 0)


def main():
    g = Graph()
    add_nodes(g)
    add_heuristics(g)
    path = g.a_star_search('S', ['G1', 'G2'])
    if path:
        print(path)
    else:
        print('no path found')


if __name__ == '__main__':
    main()