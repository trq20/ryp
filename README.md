# TCP - UDP

## Especificaciones

- Establecer un servidor `UDP` que al momento de recibir un mensaje especial de un cliente, le devuelta la dirección IP del servidor.
- El cliente debe iniciar una comunicación `UDP` para mandar un mensaje por `broadcast` en la red local para tratar de encontrar el servidor.
- El `broadcast` del cliente se debe continuar dando hasta que el servidor conteste.
- Cuando el cliente obtenga la dirección IP del servidor, debe iniciar una nueva conexión TCP con esa IP.

## Orientación

- Para iniciar un servidor/cliente `UDP`:

```python
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udp.bind(("", PORT))  # Esta linea no va del lado del cliente
```

- Para enviar un `broadcast` por `UDP`:

```python
client.sendto(msg, ('<broadcast>', PORT))
```

- Para recibir un mensaje por `UDP`:

```python
data, addr = udp.recvfrom(1024)
```

## Como entregar

Creen un `README.md` con este contenido:

```markdown
# TCP - UDP

Alumno: Nombre y Apellido
Curso: Curso
Materia: Redes y Protocolos
```

Luego en la terminal corran:

```
git init
git add README.md client.py server.py
git commit -m "Initial commit"
git checkout -b ryp/2021/tcp/v2
git push https://github.com/trq20/USERNAME.git ryp/2021/tcp/v2
```
