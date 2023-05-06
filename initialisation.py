import numpy as np
from settings import TailleQR

#QUESTION 1: génération de la matrice représentant le symbole au coin du QR code
def generationSymbole():
     # dimensions de la matrice
    taille = 7

    # initialisation de la matrice
    matrice = np.zeros((taille, taille), dtype=np.uint8)

    # remplissage de la matrice
    matrice[1:6, 1:6] = 1
    matrice[0, :] = 2
    matrice[-1, :] = 2
    matrice[:, 0] = 2
    matrice[:, -1] = 2
    matrice[2, 2] = 0

    return matrice

#QUESTION 1: retation de l'image jusqu'à ce que le QR code soit bien orienté

#renvoie la matrice après rotation de 90° dans le sens horaire
def rotationMatriceHoraire(mat):
    matTemp = mat[::-1]                 #inverse l'ordre des lignes de la matrice
    return np.transpose(matTemp)        #transpose la matrice

def rotationQRCode(QRCode):

   # génération du symbole de référence
    symbole_ref = generationSymbole()

    # dimensions de l'image
    hauteur, largeur = QRCode.shape

    # position du coin inférieur droit
    x, y = largeur-8, hauteur-8

    # recherche du coin où le symbole n'apparaît pas
    for i in range(2):
        for j in range(2):
            x_test, y_test = x-7*i, y-7*j
            if np.array_equal(QRCode[y_test:y_test+7, x_test:x_test+7], symbole_ref):
                # symbole trouvé, pas besoin de rotation
                return QRCode
    # symbole non trouvé, rotation nécessaire
    image_rot = np.rot90(QRCode, 2)
    return image_rot


#QUESTION 2 : vérification que les lignes de pixels alternés apparaissent correctement
def verificationLignes(QRCode):
    for j in range(8,17):
        if j%2==0 :
            if QRCode[6][j] == 1 or QRCode[j][6]==1:
                return False
        elif QRCode[6][j] == 0 or QRCode[j][6]==0:
            return False
    return True






