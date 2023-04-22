
from settings import TailleQR
import numpy as np

#QUESTION 6 : Génération du filtre nécessaire
def FiltreGenerateur(bit1, bit2):
    if bit1 == 0:
        if bit2 == 0:
            # Images de filtre 00
            filtre=np.zeros([TailleQR, TailleQR], dtype = int)
            print("Pas de filtrage nécessaire")

        else:
            filtre = np.fromfunction(lambda i, j: (i+j)%2, (TailleQR, TailleQR), dtype=int)
            print("Image filtrée")
    else:
        if bit2 == 0:
            filtre = np.fromfunction(lambda i, j: i % 2, (TailleQR, TailleQR), dtype=int)
        else:
            filtre = np.fromfunction(lambda i, j: j % 2, (TailleQR, TailleQR), dtype=int)
        print("Image filtrée")
    return filtre

#QUESTION 6 : Application du filtre sur le QRCode
def filtrage(QRCodeAFiltrer):

    #lecture des bits de contrôle et génération du filtre
    filtre = FiltreGenerateur(QRCodeAFiltrer[22][8], QRCodeAFiltrer[23][8])
    #XOR entre pixel du filtre et du QR code
    QRCodeFiltre = np.logical_xor(QRCodeAFiltrer, filtre)
    #conversion d'un tableau de booléen en tableau de bits
    QRCodeFiltre = np.array([[int(x) for x in y] for y in QRCodeFiltre])
    return QRCodeFiltre

