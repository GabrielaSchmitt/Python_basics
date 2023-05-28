import cv2
import os
from google.colab.patches import cv2_imshow

cascade_path = '/content/haarcascade_frontalface_default.xml'
cascade_path = os.path.abspath(cascade_path)

face_cascade = cv2.CascadeClassifier(cascade_path)

try:
    filename = take_photo()
    filename = os.path.abspath(filename)
    img = cv2.imread(filename)

    if img is None or img.shape[0] == 0 or img.shape[1] == 0:
        print("Failed to load image")
        exit()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2_imshow(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as err:
    print(str(err))
