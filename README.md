# TCP

## Especificaciones

- Definir un tamaño para el `HEADER` que va a formar parte del protocolo.
- La comunicación entre servidor y cliente debe tener este formato:
  - Al conectarse, debe haber algún mensaje de confirmación de parte del servidor.
  - Se debe poder enviar mensajes desde el cliente por la terminal. Cada mensaje que se envié debe tener un mensaje de confirmación de parte del servidor.
  - Debe existir la posibilidad de escribir en la terminal algo como `close` y terminar la conexión entre servidor y cliente.

## Orientación

- Para tomar mensajes por la terminal, pueden usar la función `input()`.
- Antes de enviar un mensaje, deben codificarlo en algún formato con `encode(format)` y cuando reciban un mensaje, deben decodificarlo con `decode(format)`.
- Usen el `HEADER` para informar el otro endpoint de cuantos bytes van a enviar en el siguiente paquete.
- Pueden tomar asignar el IP del servidor de forma dinámica usando:
```python
socket.gethostbyname(socket.gethostname())
```

## Como entregar

Creen un `README.md` con este contenido:
```markdown
# TCP - v1

Alumno: Nombre y Apellido
Curso: Curso
Materia: Redes y Protocolos
```

Luego en la terminal corran:
```
git init
git add .
git commit -m "Initial commit"
git checkout -b ryp/2021/tcp/v1
git push https://github.com/trq20/USERNAME.git ryp/2021/tcp/v1
```
