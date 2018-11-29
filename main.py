import code, kruskal

distances_matrix = read_distances_csv(13)

def init_graph(n) :

    g = Graph(n)
    for i in range(n) :


g.KruskalMST()