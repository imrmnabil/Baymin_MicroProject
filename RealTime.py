import mediapipe as mp
import cv2
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

i = 0

start_time = time.time()

# Open the default camera
cap = cv2.VideoCapture(0)

def my_function():
    try:
        # reading the input using the camera
        result, image = cap.read()

        print("Image Captured!");

        # If image will detected without any error,
        # show result
        if result:
            # saving image in local storage
            cv2.imwrite("data/CurrentImg.png", image)

            # showing result, it take frame name and image
            # output
            cv2.imshow("data/CurrentImg", image)

            # If keyboard interrupt occurs, destroy image
            cv2.destroyWindow("data/CurrentImg")

        # If captured image is corrupted, moving to else part
        else:
            print("No image detected. Please! try again")
    except:
        print("Trying Again")


def is_victory(hand_landmarks):
    # Check if the hand is making the victory sign (index and middle fingers extended, other fingers curled)
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    other_fingers_closed = all(lm.y > middle_tip_y for lm in hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP:mp_hands.HandLandmark.MIDDLE_FINGER_TIP])
    return index_tip_y < middle_tip_y and other_fingers_closed

while True:
    # Read a frame from the camera
    success, image = cap.read()
    if not success:
        print("Failed to read frame")
        break

    # Flip the image horizontally for a mirror effect
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB and process it with Mediapipe
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Check if the hand is making the victory sign
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if is_victory(hand_landmarks):
                i = i + 1
                print(i)
                if i > 8:
                    print("Victory!!")
                    i = -1000
    elapsed_time = time.time() - start_time
    if elapsed_time >= 5:
        # Call my_function() and reset the start time
        my_function()
        start_time = time.time()

    # Display the image with the detected hand landmarks
    #cv2.imshow("Hand Detection", image)

# Release the camera and close all windows
cap.release()
#cv2.destroyAllWindows()

hands.close()
