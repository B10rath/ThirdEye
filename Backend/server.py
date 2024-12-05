import socket
import numpy as np # type: ignore
import cv2 as cv # type: ignore
import io
import os

SERVER_IP = '192.168.43.188'
PORT = 65432
BUFFER_SIZE = 8192
DELIMITER = b"<END_OF_IMAGE>"
RECEIVED_FOLDER = 'received_arrays'  
FOLDER="C:/Users/adwai/Desktop/Third Eye/Backend/received_images"
os.chdir(FOLDER) 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, PORT))


server_socket.listen(5)

print("Server listening...")
i=1
while True:

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} established.")

    
    while True:
        
        size_bytes = client_socket.recv(4)
        if not size_bytes:
            break
        array_size = int.from_bytes(size_bytes, 'big')

        
        data = b''
        while len(data) < array_size:
            packet = client_socket.recv(min(array_size - len(data), BUFFER_SIZE))
            if not packet:
                break
            data += packet
        
       
        bytes_io = io.BytesIO(data)
        
       
        array = np.load(bytes_io)


        cv.imwrite("image"+str(i)+".jpg",array)
        i+=1
        
        
        delimiter = client_socket.recv(len(DELIMITER))
        if delimiter != DELIMITER:
            print("End of images.")
            break

    
    client_socket.close()


server_socket.close()