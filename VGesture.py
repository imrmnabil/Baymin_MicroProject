import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize VideoCapture object
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        # Read image from camera
        success, image = cap.read()
        if not success:
            break

        # Flip the image horizontally for a later selfie-view display
        image = cv2.flip(image, 1)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which Mediapipe uses)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and detect hands
        results = hands.process(image_rgb)

        # Check if hands are detected
        if results.multi_hand_landmarks:
            # Get the landmarks of the first (and only) detected hand
            hand_landmarks = results.multi_hand_landmarks[0]

            # Get the x, y, and z-coordinates of the landmarks
            landmarks = [[int(l.x * image.shape[1]), int(l.y * image.shape[0]), int(l.z * 1000)] for l in hand_landmarks.landmark]

            # Check if index and middle fingers are open, and other fingers are closed
            if (landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP][1] < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP][1] and
                landmarks[mp_hands.HandLandmark.RING_FINGER_TIP][1] > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP][1] and
                landmarks[mp_hands.HandLandmark.PINKY_TIP][1] > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP][1] and
                landmarks[mp_hands.HandLandmark.THUMB_TIP][0] < landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP][0] and
                landmarks[mp_hands.HandLandmark.THUMB_TIP][0] < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP][0]):
                print("Yes")

            # Visualize the hand landmarks
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the image
        cv2.imshow('MediaPipe Hands', image)

        # Exit if 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release the VideoCapture object and destroy all windows
cap.release()
cv2.destroyAllWindows()

