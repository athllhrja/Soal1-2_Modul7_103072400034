import networkx as nx
import matplotlib.pyplot as plt

# Inisialisasi graf
G_eropa = nx.Graph()
edges_eropa = [
    ('Arad', 'Zerind', 75), ('Arad', 'Timisoara', 118), ('Arad', 'Sibiu', 140),
    ('Zerind', 'Oradea', 71), ('Oradea', 'Sibiu', 151),
    ('Timisoara', 'Lugoj', 111), ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Drobeta', 75), ('Drobeta', 'Craiova', 120),
    ('Craiova', 'Pitesti', 138), ('Craiova', 'Rimnicu Vilcea', 146),
    ('Rimnicu Vilcea', 'Sibiu', 80), ('Rimnicu Vilcea', 'Pitesti', 97),
    ('Sibiu', 'Fagaras', 99), ('Fagaras', 'Bucharest', 211),
    ('Pitesti', 'Bucharest', 101), ('Bucharest', 'Giurgiu', 90), 
    ('Bucharest', 'Urziceni', 85)
]
G_eropa.add_weighted_edges_from(edges_eropa)

# Rute hasil UCS
path_eropa = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
path_edges = list(zip(path_eropa, path_eropa[1:]))

# Posisi node (menggunakan pos yang kamu berikan sebelumnya)
pos_eropa = {
    'Arad': (-4, 2), 'Zerind': (-4, 3), 'Oradea': (-3, 4),
    'Timisoara': (-5, 1), 'Lugoj': (-4, 0), 'Mehadia': (-4, -1),
    'Drobeta': (-5, -2), 'Craiova': (-3, -2),
    'Sibiu': (-2, 2), 'Rimnicu Vilcea': (-2, 1), 'Pitesti': (-1, 0),
    'Fagaras': (-1, 2), 'Bucharest': (0, -1),
    'Giurgiu': (0, -2), 'Urziceni': (1, -1)
}

plt.figure(figsize=(10, 6))
# Gambar semua node dan edge
nx.draw(G_eropa, pos_eropa, with_labels=True, node_color='lightblue', node_size=800)
# Highlight rute UCS
nx.draw_networkx_nodes(G_eropa, pos_eropa, nodelist=path_eropa, node_color='orange')
nx.draw_networkx_edges(G_eropa, pos_eropa, edgelist=path_edges, edge_color='red', width=3)

edge_labels = nx.get_edge_attributes(G_eropa, 'weight')
nx.draw_networkx_edge_labels(G_eropa, pos_eropa, edge_labels=edge_labels)
plt.title("Rute UCS: Arad -> Bucharest (Eropa)")
plt.show()