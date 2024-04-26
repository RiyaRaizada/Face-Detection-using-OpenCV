import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# To capture video from webcam.
cap = cv2.VideoCapture(0)
while True:
    # Read the frame
    ref, frame = cap.read()
    # Convert to grayscale
    frame = cv2.cvtColor(frame, 0)
    # Detect the faces
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    # Drawing the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display
    cv2.imshow('frame', frame)
    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# Release the VideoCapture object
cap.release()