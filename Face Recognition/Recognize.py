import cv2
import numpy as np
import csv
import os

def recognize():
    global tt
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    file = "Data"+os.sep+"data.csv"
    row_data = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            row_data.append(row)
    csvfile.close()
    print(row_data)

    cam = cv2.VideoCapture(0)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (255, 255, 255)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            #print(Id,conf)
            
            if(conf<100):
                for i in range(0,len(row_data),2):
                    if int(row_data[i][0]) == Id:
                        tt = str(row_data[i][1])
                        print(tt)
            else:
                tt="Unknown"
            cv2.putText(im, str(tt), (x,y+h), fontface, fontscale, fontcolor)
        cv2.imshow('im',im) 
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
