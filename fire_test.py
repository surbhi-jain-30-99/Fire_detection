import numpy as np
import cv2

fire_cascade = cv2.CascadeClassifier('cascade.xml')

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
'''if cap.isOpened() and cap1.isOpened() and cap2.isOpened():
    ret,frame = cap.read()
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    print("FRAME1")
    print(ret)
    print(frame)
    print("FRAME2")
    print(ret1)
    print(frame1)
    print("FRAME3")
    print(ret2)
    print(frame2)
'''
while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    #ret3, frame3 = cap3.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    fire1 = fire_cascade.detectMultiScale(frame1, 1.2, 5)
    fire2 = fire_cascade.detectMultiScale(frame2, 1.2, 5)
    #fire3 = fire_cascade.detectMultiScale(frame3, 1.2, 5)

    for (x,y,w,h) in fire1:
        abc1 = cv2.rectangle(frame1,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        cv2.putText(abc1, 'Fire', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        roi_gray1 = gray1[y:y+h, x:x+w]
        roi_color1 = frame1[y:y+h, x:x+w]
    for (x,y,w,h) in fire2:
        abc2 = cv2.rectangle(frame2,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        cv2.putText(abc2, 'Fire', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        roi_gray2 = gray2[y:y+h, x:x+w]
        roi_color2 = frame2[y:y+h, x:x+w]
    '''for (x,y,w,h) in fire3:
        abc3 = cv2.rectangle(frame3,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        cv2.putText(abc3, 'Fire', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        roi_gray3 = gray3[y:y+h, x:x+w]
        roi_color3 = frame3[y:y+h, x:x+w]'''

    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)
    #cv2.imshow('frame3', frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap1.release()
        cap2.release()
        cv2.destroyAllWindows() 
        break

