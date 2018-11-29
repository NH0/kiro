import code, kruskal

distances_matrix = code.read_distances_csv(13)
distribution_tab, terminal_tab = code.read_nodes_csv()

#minimum spanning
g = kruskal.Graph(n)
for i in range(n) :
    for j in range(n) :
<<<<<<< HEAD
        g.addEdge(i, j, distances_matrix[i][j])
=======
        g.addEdge(i, j, distances_matrix[j][i])
>>>>>>> 51aaafc9bb4e8c718f9d90305312cbc86c3e3adc
min_span = g.KruskalMST()

print(min_span)
