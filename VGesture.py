import mediapipe as mp
import cv2
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
image_path = "data/CurrentImg.png"

i = 0

def is_victory(hand_landmarks):
    # Check if the hand is making the victory sign (index and middle fingers extended, other fingers curled)
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    other_fingers_closed = all(lm.y > middle_tip_y for lm in hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP:mp_hands.HandLandmark.MIDDLE_FINGER_TIP])
    return index_tip_y < middle_tip_y and other_fingers_closed


while True:
    try:
        image = cv2.imread(image_path)

        # Convert the BGR image to RGB and process it with Mediapipe
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        # Check if the hand is making the victory sign
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if is_victory(hand_landmarks):
                    i = i + 1
                    print(i)
                    if i > 1:
                        print("Victory!!")
                        i = 0
                else:
                    i = 0

        key = cv2.waitKey(1)
        if key == 27:
            break
    except:
        print("Trying Again!")
    time.sleep(1)

hands.close()
