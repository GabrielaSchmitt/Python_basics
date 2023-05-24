import cv2
video = cv2.VideoCapture(0)
l = input("Insert here your file name: ")[0].upper()
input("Ready? press any key to start...")

i = 0
while i < 1800:
    check, img = video.read()
    if check:
        cv2.imshow("Frame", img) 
        cv2.imwrite(l+str(i)+".jpg", img) 
        cv2.waitKey(1)
        print(i, "de", 1800, end="\r")
        i += 1
    else:
        print("Falha ao ler imagem")
cv2.destroyAllWindows()
