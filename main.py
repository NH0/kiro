import code, kruskal

distances_matrix = code.read_distances_csv(13)
distribution_tab, terminal_tab = code.read_nodes_csv()

#minimum spanning
g = kruskal.Graph(n)
for i in range(n) :
    for j in range(n) :
        g.addEdge(i, j, distances_matrix[i][j])
min_span = g.KruskalMST()

print(min_span)
