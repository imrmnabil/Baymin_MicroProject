import os

import cv2
import time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

# Load image file
image_path = "data/CurrentImg.png"
file_path = "data/isFace.txt"

# Initialize Face Detection model
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:

    while True:
        try:
            image = cv2.imread(image_path)

            # Convert image to RGB format
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Perform face detection on the image
            results = face_detection.process(image_rgb)

            with open(file_path, "w") as f:
                if results.detections:
                    f.write("True")
                    print("True")
                else:
                    f.write("False")
                    print("False")
        except:
            print("Try Again!")

        # Wait for 1 second before detecting faces in the next frame
        time.sleep(5)
