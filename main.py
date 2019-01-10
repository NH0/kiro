#!/home/thib/Documents/Travail/ENPC/2A_IMI/Kiro/env-kiro/bin/python3

from code import *

VILLE="pim"
TAILLE_BOUCLE = 20

if VILLE=="nice":
    n=68
elif VILLE=="pim":
    n=543
elif VILLE=="grenoble":
    n=13
else:
    raise ValueError("ville doit etre une des trois villes : pim, nice ou grenoble !")
#paris 543, nice 68, gre 13
distances_matrix = read_distances_csv(n,VILLE)
distribution_tab, terminal_tab = read_nodes_csv(VILLE)
k, l = len(distribution_tab), len(terminal_tab)
print(terminal_tab)

listeDansCycle = []


#le noeud qui boucle le chemin de longueur min

def nearest_vertice(i, listeNonVisit, distances_matrix = distances_matrix) :
    min = distances_matrix[listeNonVisit[0]][i]
    result = listeNonVisit[0]
    for j in listeNonVisit :
        if distances_matrix[j][i] <= min :
            result = j
            min = distances_matrix[j][i]
    return result


def terminal_list(listeNonVisit) :
    term_list = []
    for e in listeNonVisit :
        result = nearest_vertice(e, listeDansCycle)
        term_list.append([result, e])
    return term_list


def create_cycle(idDistri, listeNonVisit):
    listebi = [idDistri]
    listeDansCycle.append(idDistri)
    i=idDistri;
    nbElements=0;
    print(listeNonVisit)
    while (len(listeNonVisit)>0 and nbElements<TAILLE_BOUCLE):
        j = nearest_vertice(i, listeNonVisit)
        listeNonVisit.remove(j)
        listebi.append(j)
        listeDansCycle.append(j)
        i=j
        nbElements+=1
    return listebi

def calcul():
    listeNonVisit = [i for i in range(k,k+l)]
    print(listeNonVisit)
    nbDistri = k
    listeb = []
    while (len(listeNonVisit)>0 and nbDistri>0):
        listeb.append(create_cycle(k-nbDistri,listeNonVisit))
        nbDistri-=1
    if (len(listeNonVisit)==0):
        if (nbDistri==0):
            print(1)
            return listeb,[]
        else:
            listeb.append([i for i in range(nbDistri,k)])
            print(2)
            return listeb,[]
    else:
        listec = terminal_list(listeNonVisit)
        print(3)
        return listeb,listec

listeb,listec = calcul()
print(listeb,listec)
create_output(listeb,listec,VILLE)
