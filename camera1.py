import cv2

# Create a video capture object for the camera
vid = cv2.VideoCapture(0)

# Loop until the user presses 'q' key
while(True):
    # Read a frame from the camera
    ret, frame = vid.read()

    # Show the frame in a window
    cv2.imshow('frame', frame)

    # Check if the user pressed 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy the window
vid.release()
cv2.destroyAllWindows()
