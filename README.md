# Chat

## Especificaciones

- En el `broadcast` el cliente tiene que enviar su nombre de usuario para que el servidor lo registre.
- El servidor tiene que ser capaz de guardar informacion de usuario, IP y alguna lista de sockets o conexiones.
- En el momento en que el cliente se conecta al servidor, este envia una lista de clientes conectados.
- El cliente tiene que poder elegir con que otro cliente disponible quiere comunicarse.
- La comunicacion queda cerrada entre estos dos clientes hasta que se escriba algun comando como `close`.
- Si la comunicacion con el cliente se cierra, debe aparecer una lista de clientes disponibles nuevamente o tener la posibilidad de cerrar la conexion con el servidor.
