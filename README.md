# Proyecto-2-Sistemas-Operativos
Este es un proyecto Python que utiliza un servidor con threads para gestionar solicitudes http y almacenarlas en un log
El programa de fondo contiene un listado de palabras para consultar para una traducción o bien, su significado como si se tratase de un pequeño diccionario.

Pasos

1) Para correr este archivo se deberá correr el comando "docker build -t server_image ." en una consola que se encuentre en el directorio donde esté el archivo "dockerfile" para crear la imagen requerida.
2) Para levantar el container en docker se deberá correr el comando "docker run -p 0.0.0.0:12345:12345 server_image" en la consola para configurar los parametros necesarios para correr el servidor web.
3) Una vez creado el contenedor y que se encuentre corriendo, en el navegador se deberá enviar solicitudes htttp con el siguiente formato: http://localhost:12345/traductor?palabra=(palabra) o  bien http://localhost:12345/diccionario?palabra=(palabra).
