import networkx as nx
import matplotlib.pyplot as plt

G_jawa = nx.Graph()
edges_jawa = [
    ('Jakarta', 'Cirebon', 327), ('Jakarta', 'Bandung', 270),
    ('Bandung', 'Cirebon', 120), ('Bandung', 'Yogyakarta', 373),
    ('Cirebon', 'Semarang', 305), ('Cirebon', 'Yogyakarta', 210),
    ('Semarang', 'Yogyakarta', 109), ('Semarang', 'Surakarta', 97),
    ('Yogyakarta', 'Surakarta', 60), ('Semarang', 'Surabaya', 369),
    ('Surakarta', 'Malang', 370), ('Surabaya', 'Malang', 94)
]
G_jawa.add_weighted_edges_from(edges_jawa)

# Rute hasil UCS
path_jawa = ['Bandung', 'Cirebon', 'Yogyakarta', 'Surakarta', 'Malang']
path_edges_jawa = list(zip(path_jawa, path_jawa[1:]))

pos_jawa = {
    'Jakarta': (-4, 1), 'Bandung': (-3, 0), 'Cirebon': (-2, 1),
    'Semarang': (0, 1), 'Yogyakarta': (0, 0), 'Surakarta': (1, 0.2),
    'Surabaya': (2.5, 1), 'Malang': (2.5, -0.2)
}

plt.figure(figsize=(10, 6))
# Gambar semua node dan edge
nx.draw(G_jawa, pos_jawa, with_labels=True, node_color='lightgreen', node_size=2000)
# Highlight rute UCS
nx.draw_networkx_nodes(G_jawa, pos_jawa, nodelist=path_jawa, node_color='yellow')
nx.draw_networkx_edges(G_jawa, pos_jawa, edgelist=path_edges_jawa, edge_color='darkgreen', width=3)

edge_labels = nx.get_edge_attributes(G_jawa, 'weight')
nx.draw_networkx_edge_labels(G_jawa, pos_jawa, edge_labels=edge_labels)
plt.title("Rute UCS: Bandung -> Malang (Pulau Jawa)")
plt.show()