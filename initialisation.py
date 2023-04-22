import numpy as np
from settings import TailleQR

#QUESTION 1: génération de la matrice représentant le symbole au coin du QR code
def generationSymbole():
    #La symbole est au total un carré de 8 pixels sur 8
    symbole = np.ones([8, 8], dtype=int)
    #Création du carré noir de 3 pixels sur 3
    for i in range(2,5):
        for j in range(2,5):
            symbole[i][j] = 0

    #Création de la bande noire
    #Bande verticale
    for i in range(7):
        symbole[i][0]=0
        symbole[i][6]=0

    #Bande Horizontale
    for j in range(7):
        symbole[0][j]=0
        symbole[6][j]=0

    return symbole

#QUESTION 1: rotation de l'image jusqu'à ce que le QR code soit bien orienté

#renvoie la matrice après rotation de 90° dans le sens horaire
def rotationMatriceHoraire(mat):
    matTemp = mat[::-1]                 #inverse l'ordre des lignes de la matrice
    return np.transpose(matTemp)        #transpose la matrice

def rotationQRCode(QRCode):

    #On récupère le carré de 8 pixels par 8 en bas à droite du QR code
    coinBasDroite = QRCode[TailleQR-8:TailleQR, TailleQR-8:TailleQR]

    symbole = generationSymbole()
    #On retourne à 180° le symbole pour simuler son positionnement en bas à droite du QR code.
    symbole = rotationMatriceHoraire(rotationMatriceHoraire(symbole))

    #Si le symbole se trouve en bas à droite du QR code, cela signifie qu'il n'est pas orienté correctement
    #On effectue alors une rotation du QR code
    while np.array_equal(coinBasDroite, symbole):
        QRCode = rotationMatriceHoraire(QRCode)
        coinBasDroite = QRCode[TailleQR-8:TailleQR, TailleQR-8:TailleQR]

    return QRCode


#QUESTION 2 : vérification que les lignes de pixels alternés apparaissent correctement
def verificationLignes(QRCode):
    for j in range(8,17):
        if j%2==0 :
            if QRCode[6][j] == 1 or QRCode[j][6]==1:
                return False
        elif QRCode[6][j] == 0 or QRCode[j][6]==0:
            return False
    return True






