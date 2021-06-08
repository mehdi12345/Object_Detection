# USAGE
# python chat_detection.py --image example.jpg
#    --cascade_file cascade --cascade_item "chat"
# verifiez si votre image n'est pas trop grande pour pouvoir visionner Ã  la sortie
# SI oui vous pouvez la redimensionner dans la ligne 22
# import the necessary packages
import cv2
import numpy as np
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
ap.add_argument("-c", "--cascade_file", required=True,
     help="path to haarcascade file")
ap.add_argument("-n", "--cascade_item", required=True,
     help="path to detection")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])                     # Loading the image file
# redimensionnement de l'image
image = cv2.resize(image,(400, 400))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        # Converting the image to gray
cascade = cv2.CascadeClassifier(args["cascade_file"]) # Load your cascade file
(H, W) = image.shape[:2]
a=int(H/100)
b=int(W/100)
# Detecting cascade items
rectangles = cascade.detectMultiScale(image = cv2.resize(gray,(100, 100)), scaleFactor=1.3, minNeighbors=10, minSize=(5, 5))

for (i, (x, y, w, h)) in enumerate(rectangles):        # puting rectangles around them
    cv2.rectangle(image, (a*x, b*y), (a*x+a*w, b*y+a*h), (0, 0, 255), 2)
    cv2.putText(image, args["cascade_item"] + " #{}".format(i + 1), (a*x, b*y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

# Displaying the detection
cv2.imshow(args["cascade_item"] + "s", image)
cv2.waitKey(200)

q=0
q = int(input('entrer 1 pour arreter: '))
while q!=1 :
    q = int(input('entrer 1 pour arreter: '))

cv2.destroyAllWindows()