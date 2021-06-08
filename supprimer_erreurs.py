#importation de librairie nécessaires
import urllib.request
import cv2
import numpy as np
import os

#fonction qui trouve les images non utilisables
def supprimer_erreurs():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for erreur in os.listdir('images_erreurs'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    erreur = cv2.imread('images_erreurs/'+str(erreur))
                    question = cv2.imread(current_image_path)
                    if erreur.shape == question.shape and not (np.bitwise_xor(erreur,question).any()):
                        print('une image erreur, on suprime!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                     print(str(e))

supprimer_erreurs()