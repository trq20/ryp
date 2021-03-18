import socket

HEADER = 0              # Cantidad de bytes del mensaje
PORT = 0000             # Puerto para conectarse
SERVER = '0.0.0.0'      # IPV4 del servidor
FORMAT = 'utf-8'        # Formato para encode y decode

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Creo un socket TCP para el cliente
client.connect((SERVER, PORT))                                  # Intento conectar al servidor

msg = client.recv(1024)     # Recibo el mensaje del servidor
print(msg.decode(FORMAT))   # Decodifico e imprimo
