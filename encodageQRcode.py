import numpy as np
from PIL import Image

# Fonction pour convertir le texte en binaire
def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

# Fonction pour ajouter les bits de parité de Hamming
def add_hamming_parity_bits(binary):
    # Calcul de la taille du code de Hamming
    m = len(binary)
    r = 2
    while 2 ** r <= m + r:
        r += 1

    # Calcul du nombre de bits de données
    k = m + r

    # Calcul du nombre de bits de parité
    n = k + r

    # Création de la matrice de contrôle de parité de Hamming
    H = np.zeros((r, n), dtype=int)
    for i in range(r):
        H[i, i:i + r] = 1

    # Conversion de la chaîne binaire en tableau numpy
    binary_array = np.array(list(binary), dtype=int)

    # Multiplication de la matrice de contrôle de parité avec les données binaires
    parity_bits = np.dot(H, binary_array) % 2

    # Ajout des bits de parité au message binaire
    encoded_message = np.concatenate((binary_array, parity_bits))

    return encoded_message.astype(str)

# Message à convertir en QR code
message = "Ceci est un QR code"

# Conversion du message en binaire
binary_message = text_to_binary(message)

# Ajout des bits de parité de Hamming
encoded_message = add_hamming_parity_bits(binary_message)

# Création d'une liste de 0 et 1 à partir du message encodé
binary_list = list(encoded_message)

# Création d'une matrice 2D avec des zéros
size = int(np.sqrt(len(binary_list)))
matrix = np.zeros((size, size), dtype=int)

# Remplissage de la matrice avec les données binaires
for i in range(size):
    for j in range(size):
        matrix[i, j] = int(binary_list[i * size + j])

# Création de l'image du QR code en utilisant PIL
image = Image.fromarray(np.uint8(matrix * 255))

# Enregistrement de l'image du QR code
image.save("qr_code.png")