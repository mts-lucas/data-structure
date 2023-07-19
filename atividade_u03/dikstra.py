import heapq
import sys


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.edges = []

    def add_edge(self, neighbor, weight):
        self.edges.append((neighbor, weight))


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        self.nodes[node_id] = Node(node_id)

    def add_edge(self, from_node, to_node, weight):
        self.nodes[from_node].add_edge(to_node, weight)

    def get_neighbors(self, node_id):
        return self.nodes[node_id].edges

    def get_all_nodes(self):
        return list(self.nodes.keys())


def load_tgf(path_file):
    with open(path_file, 'r') as file:
        lines = file.readlines()

    G = Graph()
    read_edges = False

    for line in lines:
        line = line.strip()
        if line == '#':
            read_edges = True
            continue

        if read_edges:
            n1, n2, peso = line.split()
            G.add_edge(int(n1), int(n2), weight=int(peso))
        else:
            no, _ = line.split(' ', 1)
            G.add_node(int(no))

    return G


def dijkstra(G, start):
    dists = {node: float('inf') for node in G.get_all_nodes()}
    predecessors = {node: [] for node in G.get_all_nodes()}
    dists[start] = 0

    fila = [(0, start)]

    while fila:
        dist_atual, no_atual = heapq.heappop(fila)
        if dist_atual > dists[no_atual]:
            continue

        for neighbor, peso in G.get_neighbors(no_atual):
            dist = dists[no_atual] + peso
            if dist < dists[neighbor]:
                dists[neighbor] = dist
                predecessors[neighbor] = [no_atual]
                heapq.heappush(fila, (dist, neighbor))
            elif dist == dists[neighbor]:
                predecessors[neighbor].append(no_atual)

    return dists, predecessors


def print_paths(G, start, end):
    possible_paths = []
    pile = [(start, [start])]

    while pile:
        no, path = pile.pop()

        if no == end:
            possible_paths.append(path)
        else:
            for neighbor, _ in G.get_neighbors(no):
                if neighbor not in path:
                    pile.append((neighbor, path + [neighbor]))

    print(f"Todos os caminhos possíveis de {start} a {end}:")
    for path in possible_paths:
        sequence_path = ' -> '.join(str(n) for n in path)
        print(sequence_path)


def find_shortest_path(predecessors, start, end):
    path = [end]
    while path[-1] != start:
        path.append(predecessors[path[-1]][0])
    return path[::-1]


if __name__ == "__main__":
    # Carrega o grafo a partir do arquivo robot.tgf
    G = load_tgf('robot.tgf')

    if len(sys.argv) != 3:
        print("Uso correto: python arquivo.py <start> <end>")
        sys.exit(1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # Executar o algoritmo de Dijkstra
    dists, predecessors = dijkstra(G, start)

    # Print todos os caminhos possíveis de start a end
    print_paths(G, start, end)

    # Obter o caminho mais curto de start a end
    shortest_path = find_shortest_path(predecessors, start, end)

    # Print apenas o caminho mais curto de start a end
    shortest_path_string = ' -> '.join(str(node) for node in shortest_path)
    print(f"\nCaminho mais curto de {start} a {end}: {shortest_path_string}")
