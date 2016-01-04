listeSommets = ['A', 'B', 'C', 'D', 'E']

matriceNonOriente = [
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0]
]

matriceOriente = [
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

matrice = [
    [0, 2, 4, 0],
    [2, 0, 1, 0],
    [4, 1, 0, 2],
    [0, 0, 2, 0]
]

matrice2 = [
    [0, 10, 5, 0, 7],
    [0, 0, 2, 1, 0],
    [0, 3, 0, 9, 2],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 6, 0]
]

def getListeDegres(matrice):
    listeDegres = []

    for i in range(len(matrice)):
        listeDegres.append(0)

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                listeDegres[i] += 1

    return listeDegres

def getListeSuccesseurs(matrice):
    listeSuccesseurs = []

    for i in range(len(matrice)):
        listeSuccesseurs2 = []

        for j in range(len(matrice[i])):
            if (matrice[i][j] > 0):
                listeSuccesseurs2.append(listeSommets[j])

        listeSuccesseurs.append(listeSuccesseurs2)

    return listeSuccesseurs

def getListPredecesseurs(matrice):
    listePredecesseurs = []

    for i in range(len(matrice)):
        listePredecesseurs2 = []

        for j in range(len(matrice[i])):
            if (matrice[j][i] > 0):
                listePredecesseurs2.append(listeSommets[j])

        listePredecesseurs.append(listePredecesseurs2)

    return listePredecesseurs

def getParcoursLargeur(matrice):
    parcoursLargeur = []

    parcoursLargeur.append(listeSommets[0])

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] > 0:
                estMarque = False

                for k in range(len(parcoursLargeur)):
                    if parcoursLargeur[k] == listeSommets[j]:
                        estMarque = True

                if estMarque == False:
                    parcoursLargeur.append(listeSommets[j])

    return parcoursLargeur

def getParcoursProfondeur(matrice):
    parcoursProfondeur = []

    prevId = []
    prevId.append(0)
    number = 1

    parcoursProfondeur.append(listeSommets[0])

    while len(parcoursProfondeur) < len(matrice):
        for i in range(len(matrice[prevId[len(prevId) - number]])):
            if matrice[prevId[len(prevId) - number]][i] == 1:
                estMarque = False

                for k in range(len(parcoursProfondeur)):
                    if parcoursProfondeur[k] == listeSommets[i]:
                        estMarque = True

                if estMarque == False:
                    prevId.append(i)
                    parcoursProfondeur.append(listeSommets[i])
                else:
                    if i == len(matrice[prevId[len(prevId) - number]]) - 1:
                        number = number + 1
            else:
                if i == len(matrice[prevId[len(prevId) - number]]) - 1:
                    number = number + 1

    return parcoursProfondeur

def setMatrice_Algorythme_de_Floyd_Warshal(matrice):
    for n in range(len(matrice)):
        for i in range(len(matrice)):
            for k in range(len(matrice[i])):
                for j in range(len(matrice[i])):
                    if matrice[i][k] != 0 and matrice[k][j] != 0:
                        if matrice[i][j] == 0 and i != j:
                            matrice[i][j] = matrice[i][k] + matrice[k][j]
                        else:
                            if matrice[i][j] > matrice[i][k] + matrice[k][j]:
                                matrice[i][j] = matrice[i][k] + matrice[k][j]

def Alhorythme_de_Dijkstra(matrice):
    listeSommets = [0, 100, 100, 100, 100]
    listeSommetsMarques = [0, 0, 0, 0, 0]
    countSommetsMarques = 0

    i = 0
    while countSommetsMarques < len(matrice):
        listeSommetsMarques[i] = 1
        countSommetsMarques = countSommetsMarques + 1

        for j in range(len(matrice[i])):
            if matrice[i][j] > 0:
                if (matrice[i][j] + listeSommets[i]) < listeSommets[j]:
                    listeSommets[j] = matrice[i][j] + listeSommets[i]

        valueMinVoisin = 100
        minVoisin = 0

        for k in range(len(listeSommets)):
            if listeSommetsMarques[k] == 0:
                if listeSommets[k] < valueMinVoisin:
                    valueMinVoisin = listeSommets[k]
                    minVoisin = k

        i = minVoisin

    return listeSommets



def main(matrice):
    print("Parcours en largeur : \n")

    print(getParcoursLargeur(matrice))

    print("")

    print("Parcours en profondeur : \n")

    print(getParcoursProfondeur(matrice))

    print("");

    for i in range(len(matrice)):
        print(listeSommets[i] + "\n")

        print("Successeurs : \n")

        print(getListeSuccesseurs(matrice)[i])

        print("")

        print("Predecesseurs : \n")

        print(getListPredecesseurs(matrice)[i])

        print("")

        print("Degre de " + listeSommets[i] + " : " + str(getListeDegres(matrice)[i]) + "\n")

print("Dijkstra : \n")

print(matrice2)

print("")

print(Alhorythme_de_Dijkstra(matrice2))

print("")

print("Floyd Warshal : \n")

print(matrice)

print("")

setMatrice_Algorythme_de_Floyd_Warshal(matrice)
print(matrice)

print("")

print("Matrice oriente \n")

main(matriceOriente)

print("Matrice non oriente \n")

main(matriceNonOriente)