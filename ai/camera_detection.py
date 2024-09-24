import cv2
from detect_car import detect_car

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if detect_car(frame):
        print("Carro detectado!")

    cv2.imshow("Câmera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
