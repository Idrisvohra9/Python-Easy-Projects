import cv2
import pickle
import imutils

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
    

def mouseClick(events,x, y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
                
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

cap = cv2.VideoCapture(0)

lastDigits = input("Last digits of ip address: ")
address = f"http://192.168.{lastDigits}:8080/video"
# address ="http://192.0.0.2:8080/video"
cap.open(address)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    success, img = cap.read()
    img = imutils.resize(img, width=1200)
    
    if not success:
        print("Error: Couldn't read a frame from the camera.")
        break
    
    for pos in posList:
        cv2.rectangle(img, pos,(pos[0]+width,pos[1]+height),(255,0,255),2)        
        
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image", mouseClick)
  
    # Exit loop on key press (e.g., 'q')
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    
    # Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()