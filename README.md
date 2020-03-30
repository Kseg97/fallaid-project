# ![Fallaid](https://github.com/Kseg97/fallaid-project/blob/master/images/logo.png)
## Resumen | Abstract 📋

Fallaid es un Sistema de Detección de Caidas (SDC) que integra Raspberry Pi, OpenCV, ImageZMQ, Firebase y Flutter. Permite la detección de caidas y el envío de notificaciones push a través del servicio de mensajería de Firebase (FCM). Está orientado a personas con capacidad motriz reducida, personas mayores e interesados (familiares o encargados).

Fallaid (Fall Aid) is a Fall Detection System (FDS) intergrating Raspberry Pi, OpenCV, ImageZMQ, Firebase and Flutter. It allows fall detection and push notification alarms through Firebase Cloud Messaging.

El proyecto de flutter se encuentra en:
https://github.com/Kseg97/fallaid-flutter

## ¿Por qué?

## ¿Cómo?

## ¿Qué?

Para entender qué construiremos, veamos nuestra arquitectura.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/architecture.png)

El cliente Raspberry Pi (RPi) recibe la señal de video de la webcam y la transmite por la red via ZMQ (ImageZMQ). Un servidor en Ubuntu (o windows) recibe la señal y hace un tratamiento con OpenCV y otras librerías de tratamiento numéricos y de imágenes. Si en el tratamiento (modelo de detección de personas en Caffe y algoritmo de detección de caidas) detecta una posible caida, envía un mensaje PUSH a través de Firebase Cloud Messaging (FCM). Los clientes android (desarrollados en flutter) que esté suscritos al _topic_ o tema de FCM, recibirán en su barra de notificación una alerta de caida en la habitación donde se encuentra la cámara.

## Instalación 🚀

TODO

## Ejecución 🚀

### Flutter (Android)

Después de instalar Flutter e integrar con Firebase, puedes ejecutar desde Android Studio con el botón _play_.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/android_base.jpg)

### Python

#### Cliente

TODO

#### Servidor

En el servido (Ubuntu o Windows) debes tener los archivos como:

>	Servidor:
>		- MobileNetSSD_deploy.caffemodel
>		- MobileNetSSD_deploy.prototxt
>		- server.py
>		- serviceAccountKey.json
>		- test_firebase.py

Si ejecutas `python test_firebase.py` debería llegar una notificación como en el [final](####final "Ir a ejecución final")



#### Final 
Cuando se detecte una caida, en Android aparecerá una notificación.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/notification.jpg)


## Caja | Chasis | Case 🚀

![Picure-Frame-like Plastic Case](https://github.com/Kseg97/fallaid-project/blob/master/images/case.JPG)

## Video 📢

Para  observar la puesta en funcionamiento de la práctica, se a creado un vídeo en donde se visualizan los principales detalles del sistema. Cualquier observación, retroalimentación o duda la puedes dejar en los comentarios del vídeo, si te fue de utilidad déjanos tu like.

https://youtu.be/SQcPiO0XJ9c

## Autor ✒

* **Camilo Andrés Segura** - *Trabajo Inicial* - [Usuario Github](https://github.com/kseg97)

## Expresiones de Gratitud 🎁

* **Contribución PyImageSearch** - *Base del sistema* - [Link al proyecto](https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/)
* Comenta a otros sobre este proyecto 📢 