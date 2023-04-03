import cv2
import time

cam = cv2.VideoCapture(0)

while True:
    try:
        # reading the input using the camera
        result, image = cam.read()

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

    time.sleep(1)
cam.release()
