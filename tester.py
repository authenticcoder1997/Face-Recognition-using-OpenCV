import cv2
import os
import numpy as np
import faceRecognition as fr

# test_img=cv2.imread('C:/Users/parag/OneDrive/Documents/Projects/Others/Face Recognition Neha/TestImages/test.jpg')
# faces_detected,gray_img=fr.faceDetection(test_img)
# print("faces_detected:",faces_detected)

# for(x,y,w,h) in faces_detected:
#     cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

# resized_img=cv2.resize(test_img,(1000,700))
# cv2.imshow("face detection",resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows

faces,faceID=fr.labels_for_training_data('C:/Users/parag/OneDrive/Documents/Projects/Artificial Intelligence/Face Recognition/trainingImages')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainingData.yml')
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/parag/OneDrive/Documents/Projects/Artificial Intelligence/Face Recognition/trainingData.yml')

name={0:"Priyanka",1:"Parag"}
cap=cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    faces_detected,gray_img=fr.faceDetection(test_img)



    # for (x,y,w,h) in faces_detected:
    #   cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

    # resized_img = cv2.resize(test_img, (1000, 700))
    # cv2.imshow('face detection Tutorial ',resized_img)
    # cv2.waitKey(10)


    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        if confidence < 70:#If confidence less than 70 then don't print predicted face text on screen
           fr.put_text(test_img,predicted_name,x,y)


    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face recognition tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break


cap.release()
cv2.destroyAllWindows
