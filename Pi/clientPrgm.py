import numpy as np
import io

DELIMITER = b"<END_OF_IMAGE>"
BUFFER_SIZE = 8192

def sendPhoto(client_socket, array):

    bytes_io = io.BytesIO()
    np.save(bytes_io, array)
    bytes_io.seek(0)

    array_size = bytes_io.getbuffer().nbytes
    client_socket.sendall(array_size.to_bytes(4, 'big'))

    while True:
        data = bytes_io.read(BUFFER_SIZE)
        if not data:
            break
        client_socket.sendall(data)
    
    client_socket.sendall(DELIMITER)

    print("Image sent successfully.")
