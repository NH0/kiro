#!/home/thib/Documents/Travail/ENPC/2A_IMI/Kiro/env-kiro/bin/python3

from code import *
from kruskal import *

n=543 #pim 543, nice 68, gre 13
distances_matrix = read_distances_csv(n)
distribution_tab, terminal_tab = read_nodes_csv()
k, l = len(distribution_tab), len(terminal_tab)
print(terminal_tab)

listeDansCycle = []
tousElements = []

#minimum spanning
g = Graph(n)
for i in range(n) :
    for j in range(n) :
        g.addEdge(i, j, distances_matrix[j][i])
min_span = g.KruskalMST()


#le noeud qui boucle le chemin de longueur min

def nearest_vertice(i, listeNonVisit, distances_matrix = distances_matrix) :
    min = distances_matrix[listeNonVisit[0]][i]
    result = listeNonVisit[0]
    for j in listeNonVisit :
        if distances_matrix[j][i] <= min :
            result = j
            min = distances_matrix[j][i]
    return result

def nearest_vertice2(i, listeDansCycle, distances_matrix = distances_matrix) :
    min = distances_matrix[listeDansCycle[0][0]][i]
    result = 0
    for j in range(len(listeDansCycle)) :
        if (distances_matrix[listeDansCycle[j][0]][i] <= min and listeDansCycle[j][1]<5):
            result = j
            min = distances_matrix[listeDansCycle[j][0]][i]
    return result


def terminal_list(listeNonVisit) :
    term_list = []
    for e in listeNonVisit :
        result = nearest_vertice(e, listeDansCycle)
        term_list.append([e, result])
    return term_list


def create_cycle(idDistri, listeNonVisit):
    listebi = [idDistri]
    listeDansCycle.append(idDistri)
    i=idDistri;
    nbElements=0;
    while (len(listeNonVisit)>0 and nbElements<25):
        j = nearest_vertice(i, listeNonVisit)
        listeNonVisit.remove(j)
        listebi.append(j)
        listeDansCycle.append(j)
        i=j
        nbElements+=1
    return listebi

def calcul():
    listeNonVisit = [i for i in range(k,k+l)]
    nbDistri = k
    listeb = []
    while (len(listeNonVisit)>0 and nbDistri>0):
        listeb.append(create_cycle(k-nbDistri,listeNonVisit))
        nbDistri-=1
    if (len(listeNonVisit)==0):
        if (nbDistri==0):
            return listeb,[]
        else:
            listeb.append([i for i in range(nbDistri,k)])
            return listeb,[]
    else:
        listec = []
        listeTemp = []
        tousElements = listeDansCycle
        while (len(listeNonVisit)>0):
            compteur = 1
            while (len(listeTemp)<5 and compteur>0):
                compteur = 0
                if (len(listeNonVisit)>0):
                    init = listeNonVisit[0]
                    result = nearest_vertice(init, listeDansCycle)
                    listeTemp.append(init)
        #            listeNonVisit.remove(init)
                    print(init,"----------&&&&&&&&&&&&&&&&----------\n\n")
                    for i in listeNonVisit:
                        #print(i)
                        result = nearest_vertice(i,listeDansCycle+listeTemp)
                        if (result in listeTemp):
                            listeTemp.append(i)
                            compteur+=1
                    listeNonVisit.remove(init)
            for i in listeTemp:
                if i in listeNonVisit:
                    listeNonVisit.remove(i)
            if (len(listeTemp)>0):
                result = nearest_vertice(listeTemp[0],listeDansCycle)
                listeTemp = [result] + listeTemp
                listec.append(listeTemp)
            listeTemp = []
        return listeb,listec

listeb,listec = calcul()
print(listeb,listec)
print("main branche temp")
create_output(listeb,listec,"paris-temp")
