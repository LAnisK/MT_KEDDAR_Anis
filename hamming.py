import numpy as np
from settings import TailleQR

#PRELIMINAIRES : convertir un entier en base2 (sous forme d'une liste de bits) en entier décimal.
def bin2int(base2nbr):
    longueur = len(base2nbr)
    entier = 0
    for i in range(longueur):
        entier += base2nbr[i] * 2**i
    return entier
#PRELIMINAIRES : convertir un entier en base2 (sous forme d'une liste de bits) en hexadécimal.
def bin2hex(base2nbr):
    #conversion en hexadecimal
    hexa=hex(bin2int(base2nbr))
    #on récupère uniquement les caractères héxadécimal
    caractere = hexa[2:len(hexa)]
    caractere = caractere.upper()
    return caractere
#PRELIMINAIRES : convertir un entier en base2 (sous forme d'une liste de bits) en hexadécimal.
def bin2hex(base2nbr):
    #conversion en hexadecimal
    hexa=hex(bin2int(base2nbr))
    #on récupère uniquement les caractères héxadécimal
    caractere = hexa[2:len(hexa)]
    caractere = caractere.upper()
    return caractere

#PRELIMINAIRE : transforme un bit en son complémentaire
def modifierBit(bit):
    if bit == 1:
        return 0
    else:
        return 1

# QUESTION 3 : Codage de Hamming avec en premier les 4 bits de message, puis les 3 bits de contrôle de parité.
def decodeurHamming(message):

    #on considèrera qu'il y a au plus une seule erreur.
    #on ne cherche à detecter que les erreurs sur les 4 bits de message,
    #on ne s'intéressera pas au cas où l'erreur porte sur un seul bit de contrôle

    m1, m2, m3, m4, c1, c2, c3 = message
    c1Th = (m1 + m2 + m4)%2
    c2Th = (m1 + m3 + m4)%2
    c3Th = (m2 + m3 + m4)%2

    if c1 != c1Th and c2 != c2Th and c3!= c3Th:
        m4 = modifierBit(m4)
    elif c1 != c1Th and c2 != c2Th:
        m1 = modifierBit(m1)
    elif c1 != c1Th and c3 != c3Th:
        m2 = modifierBit(m2)
    elif c2 != c1Th and c3 != c3Th:
        m3 = modifierBit(m3)

    return [m1,m2,m3,m4]

def codeurHamming(information):
    m1, m2, m3, m4 = information
    c1 = (m1 + m2 + m4) % 2
    c2 = (m1 + m3 + m4) % 2
    c3 = (m2 + m3 + m4) % 2

    return [m1,m2,m3,m4,c1,c2,c3]


#QUESTION 4-5 : Récupération du type de données et du nombre de blocs à lire par lecture des bits de contrôles

def lectureSetting(QRCode):
    dataType = QRCode[24][8]
    nbrBlocs = bin2int([QRCode[i][0] for i in range(16,11,-1)])
    return dataType, nbrBlocs

#QUESTION 4 : parcours du QRCode pour renvoyer l'information sous la forme d'un liste de 14bits.
def decompositionBloc(QRCode, nbrBloc):
    QRCode = np.array(QRCode)

    #Initialisation de la position du pixel à lire en se positionnant en bas à droite du QR code
    positionLig = TailleQR - 1
    positionCol = TailleQR - 1
    #donne le nombre de bloc déjà lu
    compteur = 0

    #donne le sens de lecture : vaut -1 pour une lecture de droite à gauche
    #                           vaut 1 pour une lecture de gauche à droite
    direction = -1

    #initialisation de la liste de liste de 14bits
    informationLue = []

    while compteur<nbrBloc:
        #initialisation de la liste de bits
        liste14bits=[]
        for i in range(7):
            liste14bits.append(QRCode[positionLig][positionCol])
            liste14bits.append(QRCode[positionLig-1][positionCol])

            #on déplace le curseur d'un pixel dans la direction souhaitée
            positionCol += direction

        #ajout de la liste de 14 bits à la lecture globale
        informationLue.append(liste14bits)

        compteur += 1

        # tous les deux blocs, on change la direction de lecture
        if compteur%2 == 0:
            direction *= -1
            positionLig -= 2

        #repositionnement du pixel de lecture
            positionCol += direction

    return np.array(informationLue)

#QUESTION 5 : Lecture d'une liste de 14 bits en fonction du type de données souhaités.
#Entrèe :   liste de 14 bits
#           type de données
#sortie :   chaine de caractère

def lectureContenuBloc(bloc, dataType):
    # séparation du blocs en deux fois 7 bits afin de les décoder
    data1 = bloc[0:7]
    data1 = decodeurHamming(data1)
    data2 = bloc[7:14]
    data2 = decodeurHamming(data2)

    chaine = []

    #si il s'agit de données numériques, les deux symboles héxadécimaux doivent être calculés séparement
    if dataType == 0:
        chaine.append(bin2hex(data1))
        chaine.append(bin2hex(data2))
    #si il s'agit de donnéesbrutes,il faut concaténer les deux messages de 4 bits pour obtenir un code ASCII en  bits
    if dataType == 1:
        chaine.append(chr(bin2int(data1+data2)))

    return chaine

#QUESTION 5 : lecture du QR code complet
def lectureQRCode(QRCode, dataType, nbrBloc):

    blocs = decompositionBloc(QRCode, nbrBloc)
    chaine = []

    for i in range(nbrBloc):

        chaine = chaine + lectureContenuBloc(blocs[i], dataType)

    print("".join(chaine))
