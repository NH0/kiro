from code import *
from kruskal import *

n=13
distances_matrix = read_distances_csv(n)
distribution_tab, terminal_tab = read_nodes_csv()

#minimum spanning
g = Graph(n)
for i in range(n) :
    for j in range(n) :
        g.addEdge(i, j, distances_matrix[j][i])
min_span = g.KruskalMST()

print(min_span)
