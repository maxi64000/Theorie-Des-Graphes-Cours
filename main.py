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

def main(matrice):
    print("Parcours en largeur : \n")

    print(getParcoursLargeur(matrice))

    print("")

    print("Parcours en profondeur : \n")

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