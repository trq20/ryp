import socket

HEADER = 0              # Cantidad de bytes del mensaje
PORT = 0000             # Puerto para conectarse
SERVER = '0.0.0.0'      # IPV4   
FORMAT = 'utf-8'        # Formato para encode y decode

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creo un socket TCP para el servidor
server.bind((SERVER, PORT))                                 # Conecto el socket a una direccion 

print("[STARTING] Server is starting")
server.listen()                                             # Dejo el servidor escuchando por conexiones
print(f"[LISTENING] Server is listening on {SERVER}.")

while True:                                                 # Dejo el servidor corriendo
    conn, addr = server.accept()                            # Si hay clientes, los acepto
    print(f"[NEW CONNECTION] {addr} connected.")    
    msg = "Welcome to the server!".encode(FORMAT)           # Envio al cliente nuevo un mensaje
    conn.send(msg)