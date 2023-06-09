
import projet as pr
import initialisation as init
import numpy as np
import filter as ft
import hamming as Ha

#QUESTION 7: Décodage de tout les QRCode
def decodageQRCode(filename):
    QRCode = pr.loading(filename)
    QRCode = np.array(QRCode)
    QRCode = init.rotationQRCode(QRCode)
    dataType, nbrBloc = Ha.lectureSetting(QRCode)
    QRCode = ft.filtrage(QRCode)
    QRCode = Ha.lectureQRCode(QRCode, dataType, nbrBloc)


decodageQRCode(r"C:\Users\SAM\Desktop\Exemples/qr_code_damier_ascii.png")
decodageQRCode(r"C:\Users\SAM\Desktop\Exemples/qr_code_ssfiltre_ascii_corrupted.png")
decodageQRCode(r"C:\Users\SAM\Desktop\Exemples/qr_code_ssfiltre_ascii_rotation.png")
decodageQRCode(r"C:\Users\SAM\Desktop\Exemples/qr_code_ssfiltre_num.png")
decodageQRCode(r"C:\Users\SAM\Desktop\MT_KEDDAR_Anis/qr_codel.png")