from clientPrgm import sendPhoto
import numpy as np # type: ignore
import cv2 as cv # type: ignore
import os
import socket

SERVER_IP = '192.168.43.188'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

#direct = "D:Opsis/openCV/resultImages"
#os.chdir(direct)

count = 1

captr = cv.VideoCapture("D:/Opsis/openCV/assets/flagTest.mp4")
ret1, frame1 = captr.read()
filename = "image_"+str(count)+".jpg"
#cv.imwrite(filename,frame1)
sendPhoto(client_socket, frame1)
count += 1

while ret1:

    ret1, frame2 = captr.read()
    if ret1:
        a = np.full_like(frame1,0)
        cv.absdiff(frame1,frame2,a)

        prcntDiff = (np.count_nonzero(a)/a.size)*100
        #print("Percentage difference is : ",prcntDiff,"Count: ",count)

        if (prcntDiff>96):
            filename = "image_"+str(count)+".jpg"
            #cv.imwrite(filename,frame2)
            frame1 = frame2
            print("Image is extracted")
            sendPhoto(client_socket, frame2)
            count += 1

client_socket.close()