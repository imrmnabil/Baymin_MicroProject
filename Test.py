import cv2

# Create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if frame was successfully captured
    if not ret:
        break

    # Display the captured frame in a window
    cv2.imshow('frame', frame)

    # Wait for a key press and check if it was the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()