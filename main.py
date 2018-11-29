import code, kruskal

distances_matrix = read_distances_csv(13)
distribution_tab, terminal_tab = read_nodes_csv()

def init_graph(n, distances_matrix=distances_matrix, nodes_tab=terminal_tab+distribution_tab) :

    g = Graph(n)
    for i in range(n) :
        for j in range(n) :
            g.addEdge(i, j, distances_matrix[i,j])
     return g

def min_spanning(g) :
    return g.KruskalMST()

