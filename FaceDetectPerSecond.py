import cv2
import time

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    # Load the image file
    img = cv2.imread("data/CurrentImg.png")
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If at least one face is detected, print "yes"
    if len(faces) > 0:
        print("yes")
    else:
        print("No")
    time.sleep(1)

