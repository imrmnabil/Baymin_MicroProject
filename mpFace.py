import cv2
import time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

# Load image file
image_path = "data/CurrentImg.png"

# Initialize Face Detection model
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:

    while True:
        try:
            image = cv2.imread(image_path)

            # Convert image to RGB format
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Perform face detection on the image
            results = face_detection.process(image_rgb)

            # If a face is detected, print "Yes"
            if results.detections:
                print("Yes")
            else:
                print("No")
        except:
            print("Try Again!")

        # Wait for 1 second before detecting faces in the next frame
        time.sleep(1)
