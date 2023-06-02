import cv2
import os

# download the above doc by the link https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
cascade_path = r'haarcascade_frontalface_default.xml'
cascade_path = os.path.abspath(cascade_path)

face_cascade = cv2.CascadeClassifier(cascade_path)

try:
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()

        if not ret:
            print("Failed to capture image")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("ASL Gesture Recognition", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

except Exception as err:
    print(str(err))
