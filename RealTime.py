import mediapipe as mp
import cv2
import time
import pigpio
import pygame

pygame.mixer.init()
pygame.mixer.music.load('meerabai.mp3')

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

i = 0

start_time = time.time()
start_time2 = time.time()

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
        
def dance():
    pi = pigpio.pi()  # create a connection to the pigpio daemon

    s1 = 14
    s2 = 23
    s3 = 16
    s4 = 26

    # set the GPIO modes to PWM output
    pi.set_mode(s1, pigpio.OUTPUT)
    pi.set_mode(s2, pigpio.OUTPUT)
    pi.set_mode(s3, pigpio.OUTPUT)
    pi.set_mode(s4, pigpio.OUTPUT)

    # set the pulse width range suitable for the servos (500-2500 microseconds)
    pi.set_servo_pulsewidth(s1, 0)
    pi.set_servo_pulsewidth(s2, 0)
    pi.set_servo_pulsewidth(s3, 0)
    pi.set_servo_pulsewidth(s4, 0)

    time.sleep(1)  # wait for the servos to reach the middle position
    i = 0
    step = 20
    sleep_time = 0.02
    
    
    pygame.mixer.music.play()
    try:
        while i <3:
            
            #smoothly rotate the servos back to the middle position
            for pulse_width in range(1500, 1000, -1*step):
                pi.set_servo_pulsewidth(s1, pulse_width)
                pi.set_servo_pulsewidth(s2, pulse_width)
                pi.set_servo_pulsewidth(s3, pulse_width)
                pi.set_servo_pulsewidth(s4, pulse_width)
                time.sleep(sleep_time)
        
            # slowly rotate the servos to one side
            for pulse_width in range(1000, 1500, step):
                pi.set_servo_pulsewidth(s1, pulse_width)
                pi.set_servo_pulsewidth(s2, pulse_width)
                pi.set_servo_pulsewidth(s3, pulse_width)
                pi.set_servo_pulsewidth(s4, pulse_width)
                time.sleep(sleep_time)
            time.sleep(.3)
                
            #smoothly rotate the servos back to the middle position
            for pulse_width in range(1500, 2000, step):
                pi.set_servo_pulsewidth(s1, pulse_width)
                pi.set_servo_pulsewidth(s2, pulse_width)
                pi.set_servo_pulsewidth(s3, pulse_width)
                pi.set_servo_pulsewidth(s4, pulse_width)
                time.sleep(sleep_time)
        
            # slowly rotate the servos to one side
            for pulse_width in range(2000, 1500, -1*step):
                pi.set_servo_pulsewidth(s1, pulse_width)
                pi.set_servo_pulsewidth(s2, pulse_width)
                pi.set_servo_pulsewidth(s3, pulse_width)
                pi.set_servo_pulsewidth(s4, pulse_width)
                time.sleep(sleep_time)
            time.sleep(.3)
            
            
            i = i+1
    except:
        print("Sorry")
        
    # stop the servos at the middle position
    pi.set_servo_pulsewidth(s1, 0)
    pi.set_servo_pulsewidth(s2, 0)
    pi.set_servo_pulsewidth(s3, 0)
    pi.set_servo_pulsewidth(s4, 0)
    
    pygame.mixer.music.stop()

    # release the pigpio connection
    pi.stop()


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
        continue

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
                if i > 5:
                    print("Victory!!")
                    i = 0
                    dance()
    if time.time() - start_time2 >= 2:
        i = 0
        start_time2 = time.time()
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
