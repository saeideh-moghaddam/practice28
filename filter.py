import cv2

cap = cv2.VideoCapture(0)
pixel = []
row=1
while True:
    ret,frame = cap.read()
    width , height, _ = frame.shape
    
    if not ret:
        break
    if cv2.waitKey(1) == ord("q"):
        break
    
    cv2.line(frame,(0,row),(height,row),(0,255,0))
    
    pixel.append(frame[row-1])
    frame[:row] = pixel
    row += 1
    if row>width:
        cv2.imwrite("filter.jpg",frame)
        row=1
        pixel.clear()
    cv2.imshow("Filter fun",frame)

cap.release()
cv2.destroyAllWindows()