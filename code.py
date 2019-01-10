#!/home/thib/Documents/Travail/ENPC/2A_IMI/Kiro/env-kiro/bin/python3

import csv


def read_nodes_csv():
    with open('nice/nodes.csv', newline='') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=';')
        nodes_tab = []
        i = 0
        for row in spam_reader:
            if i == 0:
                pass
            i += 1
            nodes_tab.append(row)
    distribution_tab = []
    for e in nodes_tab:
        if e[2] == 'distribution' :
            l = []
            for i in e[:2] :
                l.append(float(i))
            distribution_tab.append(l)
    terminal_tab = []
    for e in nodes_tab:
        if e[2] == 'terminal':
            l = []
            for i in e[:2]:
                l.append(float(i))
            terminal_tab.append(l)
    return distribution_tab, terminal_tab


def read_distances_csv(n):
    with open('nice/distances.csv', newline='') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=';')
        distances_tab = []
        i = 0
        for row in spam_reader:
            if i == 0:
                pass
            i += 1
            distances_tab.append(row)
        distances_matrix = [[] for i in range(n)]
        for i in range(n) :
            for j in range(n) :
                distances_matrix[i].append(int(distances_tab[i*n+j][0]))
    return distances_matrix


def create_output(list_b, list_c, nom):
    nom = nom+".txt"
    with open(nom, 'w') as txt_file:
        for list_bi in list_b:
            txt_file.write("b")
            for i in list_bi:
                txt_file.write(" "+str(i))
            txt_file.write("\n")
        for list_ci in list_c:
            txt_file.write("c")
            for i in list_ci:
                txt_file.write(" "+str(i))
            txt_file.write("\n")


# create_output([[0,1,2],[0,3,5]],[[2,4]],"grenobletest")
