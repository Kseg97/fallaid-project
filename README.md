# ![Fallaid](https://github.com/Kseg97/fallaid-project/blob/master/images/logo.png)
## Resumen | Abstract 📋

Fallaid es un Sistema de Detección de Caidas (SDC) que integra Raspberry Pi, OpenCV, ImageZMQ, Firebase y Flutter. Permite la detección de caidas y el envío de notificaciones push a través del servicio de mensajería de Firebase (FCM). Está orientado a personas con capacidad motriz reducida, personas mayores e interesados (familiares o encargados).

Fallaid (Fall Aid) is a Fall Detection System (FDS) intergrating Raspberry Pi, OpenCV, ImageZMQ, Firebase and Flutter. It allows fall detection and push notification alarms through Firebase Cloud Messaging.

El proyecto de flutter se encuentra en:
https://github.com/Kseg97/fallaid-flutter

Este proyecto está basado en: 
https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
Adaptando el algoritmo de detección de caidas de:
https://github.com/EikeSan/video-fall-detection
Y el cliente Fluter FCM de:
https://www.youtube.com/watch?v=xx7hemn3FY4

## Video 📢

Para  observar la puesta en funcionamiento del proyecto, se a creado un vídeo en donde se visualizan los principales detalles del sistema. Cualquier observación, retroalimentación o duda la puedes dejar en los comentarios del vídeo, si te fue de utilidad déjanos tu like.

https://youtu.be/SQcPiO0XJ9c

## ¿Por qué?

## ¿Cómo?

## ¿Qué?

Para entender qué construiremos, veamos nuestra arquitectura.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/architecture.png)

El cliente Raspberry Pi (RPi) recibe la señal de video de la webcam y la transmite por la red via ZMQ (ImageZMQ). Un servidor en Ubuntu (o windows) recibe la señal y hace un tratamiento con OpenCV y otras librerías de tratamiento numéricos y de imágenes. Si en el tratamiento (modelo de detección de personas en Caffe y algoritmo de detección de caidas) detecta una posible caida, envía un mensaje PUSH a través de Firebase Cloud Messaging (FCM). Los clientes android (desarrollados en flutter) que esté suscritos al _topic_ o tema de FCM, recibirán en su barra de notificación una alerta de caida en la habitación donde se encuentra la cámara.

## Instalación 🚀

### Utilidades

TODO: ifconfig ipconfig

### Flutter

TODO:

### Raspberry Pi

TODO

## Ejecución 🚀

### Flutter (Android)

Después de instalar Flutter e integrar con Firebase, puedes ejecutar desde Android Studio con el botón _play_.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/android_base.jpg)

### Python

#### Cliente

En el cliente (RPi) debes tener los archivos como:

>	Cliente:
- client.py

Para iniciar la transmisión, ejecuta el comando
`python3 client.py --server-ip 192.168.1.5`

Recuerda cambiar __192.168.1.5__ por la IP de tu servidor. En [Utilidades](#utilidades "Ir a las utilidades") puedes ver cómo conoces esta IP.

#### Servidor

En el servidor (Ubuntu o Windows) debes tener los archivos como:

>	Servidor:
- MobileNetSSD_deploy.caffemodel
- MobileNetSSD_deploy.prototxt
- server.py
- serviceAccountKey.json
- test_firebase.py

Recuerda tener el archivo `serviceAccountKey.json` descargado desde tu consola en Firebase en la carpeta del servidor. Y el archivo `google-services.json` descargado también desde la configuración de tu proyecto Android en Firebase Console, en la capeta _android/app_ en tu proyecto de Flutter.

Si ejecutas `python test_firebase.py` debería llegar una notificación como en el [final](#final "Ir a ejecución final")

Para iniciar la recepción, se debe correr
`python server.py --prototxt MobileNetSSD_deploy.prototxt \
	--model MobileNetSSD_deploy.caffemodel --montageW 1 --montageH 1 \
	--firebaseKey serviceAccountKey.json`

Aparecerá una ventana en pantalla con el video recibido desde el cliente. Es posible tener más clientes y mostrarlos cambiando los argumentos de `montageW` y `montageH` que corresponden a las columnas y fila, respectivamente.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/montage.jpg)

#### Final 

Cuando se detecte una caida, en Android aparecerá una notificación.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/notification.jpg)

## Caja | Chasis | Case 🚀

Este proyecto cuenta con una caja mimetizada (parecida a elementos cotidianos) con el fin de ocultarla a las personas monitoreadas. Su diseño es similar a un portaretratos y está pensado en su construcción via impresión 3D. Se recomienda plástico PLA o ABS con acabado de madera. Consta de 4 partes incluidas en la carpeta ___case_stl___, dos de las cuales necesitan dos unidades (rieles y soporte de riel para la foto).

![Picure-Frame-like Plastic Case](https://github.com/Kseg97/fallaid-project/blob/master/images/case.JPG)

## Autor ✒

* **Camilo Andrés Segura** - *Trabajo Inicial* - [Usuario Github](https://github.com/kseg97)

## Expresiones de Gratitud 🎁

* **Contribución PyImageSearch** - *Base del sistema* - [Link al proyecto](https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/)
* Comenta a otros sobre este proyecto 📢 