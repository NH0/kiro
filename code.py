import csv

def read_nodes_csv() :
    with open('nodes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        nodes_tab = []

        i = 0
        for row in spamreader:
            if i == 0 :
                pass
            i += 1

            nodes_tab.append(row)

    distribution_tab = []
    for e in nodes_tab :
        if e[2] == 'distribution' :
            l = []
            for i in e[:2] :
                l.append(int(i))
            distribution_tab.append(l)

    distribution_tab = []
    for e in nodes_tab:
        if e[2] == 'distribution':
            l = []
            for i in e[:2]:
                l.append(int(i))
            distribution_tab.append(l)
    return nodes_tab


def read_distances_csv(n) :
    with open('distances.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        distances_tab = []

        i = 0
        for row in spamreader:
            if i == 0 :
                pass
            i += 1

            distances_tab.append(row)

        distances_matrix = [[] for i in range(n)]
        for i in range(n) :
            for j in range(n) :
                distances_matrix[i].append(int(distances_tab[i*n+j][0]))

    return distances_matrix


