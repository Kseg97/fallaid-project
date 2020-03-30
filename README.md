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

Para  observar la puesta en funcionamiento del proyecto, se ha creado un vídeo en donde se visualizan los principales detalles del sistema. En el video también se explican el funcionamiento del código, la arquitectura y posibles mejoras de este sistema. Cualquier observación, retroalimentación o duda la puedes dejar en los comentarios del vídeo, si te fue de utilidad déjanos tu like.

https://youtu.be/SQcPiO0XJ9c

## ¿Por qué?

En Fallaid creemos que un mundo mejor es un mundo que cuida a los más vulnerables.

> Existen millones de personas con discapacidades y dificultades motrices que se encuentran en condiciones de movilidad vulnerables. Estas personas varían desde los adultos mayores y ancianos hasta personas en proceso de rehabilitación o con discapacidad permanente. Todos ellos con alta vulnerabilidad ante accidentes físicos; una necesidad que deben ser atendida.

## ¿Cómo?

Para lograr eso, nuevas soluciones deben estar enfocadas en:

* Monitorear caídas y otros eventos relacionados.
* Alertar a familiares, encargados o colaboradores.
* Ayudar en la prevención de accidentes.

## ¿Qué?

Por todo lo anterior nace __Fallaid__, una plataforma de monitoreo y advertencia de caídas en entornos cerrados.

Para entender qué construiremos, veamos nuestra arquitectura.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/architecture.png)

El cliente Raspberry Pi (RPi) recibe la señal de video de la webcam y la transmite por la red via ZMQ (ImageZMQ). Un servidor en Ubuntu (o windows) recibe la señal y hace un tratamiento con OpenCV y otras librerías de tratamiento numéricos y de imágenes. Si en el tratamiento (modelo de detección de personas en Caffe y algoritmo de detección de caidas) detecta una posible caida, envía un mensaje PUSH a través de Firebase Cloud Messaging (FCM). Los clientes android (desarrollados en flutter) que esté suscritos al _topic_ o tema de FCM, recibirán en su barra de notificación una alerta de caida en la habitación donde se encuentra la cámara.

## Instalación 🤬

Descarga o clona este repositorio en tu escritorio o lugar de trabajo. Para clonar ejecuta:

`git clone https://github.com/Kseg97/fallaid-project`

Para descargar solo presiona sobre el botón de descarga y descomprime el archivo.

![Descarga](https://github.com/Kseg97/fallaid-project/blob/master/images/download.jpg)

### Utilidades

Recuerda actualizar los repositorios del sistema (solo Ubuntu) en cada sesión de programación en la que vayas a instalar paquetes. Usa `sudo apt-get update
`. 

Para conocer la IP del dispositivo en Windows usa `ipconfig` desde CMD.
Para conocer la IP del dispositivo en Ubuntu usa `ifconfig` desde el terminal (Ctrl+Shift+T).

Si deseas conocer los dispositivos conectados a tu red.

* En windows, usa WNetWatcher: https://www.nirsoft.net/utils/wnetwatcher.zip
* En Ubuntu, usa NMAP: `sudo apt-get install nmap` 

### Firebase

0. Crea o define la cuenta de google a usar.
1. Abre la consola de Firebase: https://console.firebase.google.com/u/0/.
2. Presiona en agregar proyecto.
3. Configura a gusto el nombre del mismo y otros detalles de locación.
4. Debes poder ver un panel como el siguiente: 

![Dashboard](https://github.com/Kseg97/fallaid-project/blob/master/images/firebase_panel.jpg)

5. En la esquina superior izquierda verás un botón de configuración. Presiónalo y ve a _Configuración del Proyecto_.
6. Dirígete a la sección de _cuentas de servicio_. En ella verás distintas formas de trabajar con __Firebase Admin__ a través de su soporte a distintos lenguajes de programación.
7. Ve hasta el fondo de esta sección y oprime sobre _generar nueva clave privada_.
8. Acepta y al archivo descargado (que se llama como tu proyecto más otros detalles aleatorios) nómbralo como __serviceAccountKey.json__. Recuerda este archivo para más adelante, es tu llave a los servicios de Firebase desde el servidor.
9. Regresa a la sección _General_ de la configuración de Firebase Console.
10. Dirígete al fondo y crea una nueva aplicación de Android.
11. Llena el campo de nombre con el mismo nombre con el que creaste la de Flutter. Si descargaste nuestro código, introduce `com.fallaid.fallaid`.
12. El certificado debes generarlo en tu computadora: https://developers.google.com/android/guides/client-auth.
	i. En Linux (Ubuntu) no suele haber problemas.
	ii. En Windows, dirígete a tu instalación de Java. Si no tienes instalado, instala el SDK (https://www.oracle.com/java/technologies/javase-jdk8-downloads.html).
		a. Para dirigirte usa `cd %JAVA_HOME%/bin` o `cd C:\\"Program Files"\Java\jdk1.8.xxxxx\bin`, en caso de que no funcione el primero y completando _xxxxx_ por la versión que hayas instalado. Verifica que existe en esa locación con el explorador.
		b. Si tu consola CMD se encuentra así, ya puedes usar el comando _keytool_ como indica en la URL de este paso.

![Generación de SHA-1](https://github.com/Kseg97/fallaid-project/blob/master/images/sha.png)

### Flutter

Puedes hacer esta parte en Windows (recomendado), pero también es posible en Ubuntu (junto a nuestro server).

Si decides hacer esta app desde cero, te recomendamos: https://www.youtube.com/watch?v=xx7hemn3FY4. Aunque existen otros tutoriales en español. Importante es la creación del proyecto en Firebase y en Flutter y que cuando integres la aplicación a Firebase (Android) tengas en cuenta el dominio o "url" de la app (_e.g._ com.fallaid.fallaid o com.mi_app.mi_nombre).

1. Instala Android Studio:
2. Instala Flutter:
3. Descarga o clona (si usas git) el proyecto de:
4. Copia el archivo _google-services.json_ de la sección anterior en la carpeta _android/app_ como se ve en la imagen

![Google Services Firebase Flutter](https://github.com/Kseg97/fallaid-project/blob/master/images/gservices.png)

5. Dile a Flutter y Gradle que actualicen las dependencias cuando te lo permitan.

![Google Services Firebase Flutter](https://github.com/Kseg97/fallaid-project/blob/master/images/update_flutter.png)

### Raspberry Pi

Te recomendamos este [tutorial](https://geekland.eu/instalar-raspbian-con-raspberry-pi-imager/) para instalar el último (verifica en https://www.raspberrypi.org/downloads/raspbian/, recomendamos la versión Lite).

1. Si sigues el tutorial recomendado, evita la parte del ethernet si no conoces tu router. En su lugar sigue:
	i. Ya tienes el archivo _ssh_ creado en el _boot_ de la tarjeta SD. Ahora crea otro archivo llamado ___wpa_supplicant.conf___. Este método está descrito en https://www.raspberrypi.org/documentation/configuration/wireless/headless.md.
	ii. Dentro de _wpa_supplicant.conf_ copia lo de la imágen. Esto hará que no necesites de una pantalla para configurar tu Raspberry Pi. El método se llama Headless

![Headless Raspberry](https://github.com/Kseg97/fallaid-project/blob/master/images/wpasupplicant.png)

	iii. Inserta la SD en la raspberry y espera un rato. Ya puedes conectarte a ella por SSH. Revisa el tutorial para comprender más.

2. Conectate a la RPi por SSH: `ssh pi@192.168.1.xx`. recuerda que en [Utilidades](#utilidades "Ver cómo conseguir la IP") puedes encontrar la IP.
3. Ejecuta `raspi-config` en el terminal SSH. El terminal debe decir algo como `pi@raspberrypi:~ $`.
4. Ve a _Advanced options_ y presiona sobre expandir la memoria del sistema. Esto nos permite que la RPi pueda tomar más espacio de la SD dónde se instaló. Al salir de este menú te pedirá reiniciar, hazlo.
![Expand Memory](https://github.com/Kseg97/fallaid-project/blob/master/images/wpasupplicant.png)
5. Una vez reiniciado, instala las librerías.
	i. `pip3 install imutils`
	ii. `pip3 install zmq`
	iii. `pip3 install imagezmq`
6. Copia el código de `client.py` desde donde lo descargaste al principio de la instalación hacia la RPi. Para hacer esto, ejecuta desde tu compu (Ubuntu o Windows) los comandos:
	i. Terminal o CMD: `cd Desktop/fallaid-project/client`, o dónde hayas descargado el código del proyecto.
	ii. En la RPi (SSH): `cd ~` y luego `mkdir fallaid`
	iii. Terminal o CMD: `scp client.py pi@192.168.1.xx:~/fallaid`
7. Con todo esto deberías tener lista tu Raspberry Pi para ejecutar el script.

### Ubuntu

0. Actualiza los repositorios en tu sistema e instala librerías básicas.
	i. `sudo apt update`
	ii. `sudo apt install software-properties-common`

1. Instala Python 3.
	i. 	`sudo add-apt-repository ppa:deadsnakes/ppa
` y presiona ENTER.
	ii. `sudo apt-get install python3.5 python3.5-dev`
	iii. Prueba la instalación con `python3 --version`
	iv. Instala pip. 
	`sudo apt install python3-pip`
	v. Prueba la instalación con `pip3 --version`

2. Instala OpenCV.
	i. `sudo apt-get install python-opencv`
	ii. `pip3 install opencv-contrib-python`
	iii Para probar la instalación ejecuta `python3 -c "import cv2; print(cv2.__version__)"`

3. Instala las librerías necesarias.
	i. `pip3 install numpy`
	ii. `pip3 install imutils`
	iii. `pip3 install zmq`
	iv. `pip3 install imagezmq`
	v. `pip3 install firebase-admin`	
4. Mueve el archivo _serviceAccountKey.json_ del paso [Firebase](#firebase "Configuración de firebase") a la carpeta __server__ de este proyecto.

### Windows

Aún sin probar.

1. Instala Python 3: https://www.python.org/downloads/windows/.
2. Instala OpenCV (primera parte recomendada): https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html.
3. Instala las librerías necesarias a través de pip como en [Ubuntu](#ubuntu "Configuración de ubuntu").
4. Mueve el archivo _serviceAccountKey.json_ del paso [Firebase](#firebase "Configuración de firebase") a la carpeta __server__ de este proyecto.

## Ejecución 🚀

### Flutter (Android)

Después de instalar Flutter e integrar con Firebase, conecta el celular y ejecuta desde Android Studio con el botón _play_. Verás una interfaz en tu celular como la siguiente.

![Android](https://github.com/Kseg97/fallaid-project/blob/master/images/android_base.jpg)

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

Si ejecutas `python3 test_firebase.py` debería llegar una notificación como en el [final](#final "Ir a ejecución final")

Para iniciar la recepción, se debe correr
`python server.py --prototxt MobileNetSSD_deploy.prototxt \
	--model MobileNetSSD_deploy.caffemodel --montageW 1 --montageH 1 \
	--firebaseKey serviceAccountKey.json`

Aparecerá una ventana en pantalla con el video recibido desde el cliente. Es posible tener más clientes y mostrarlos cambiando los argumentos de `montageW` y `montageH` que corresponden a las columnas y fila, respectivamente.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/montage.jpg)

#### Final 

Cuando se detecte una caida aparecerá una notificación en Android.

![Arquitectura](https://github.com/Kseg97/fallaid-project/blob/master/images/notification.jpg)

## Caja | Chasis | Case 🚀

Este proyecto cuenta con una caja mimetizada (parecida a elementos cotidianos) con el fin de ocultarla a las personas monitoreadas. Su diseño es similar a un portaretratos y está pensado en su construcción via impresión 3D. Se recomienda plástico PLA o ABS con acabado de madera. Consta de 4 partes incluidas en la carpeta ___case_stl___, dos de las cuales necesitan dos unidades (rieles y soporte de riel para la foto).

![Picure-Frame-like Plastic Case](https://github.com/Kseg97/fallaid-project/blob/master/images/case.JPG)

## Autor ✒

* **Camilo Andrés Segura** - *Trabajo Inicial* - [Usuario Github](https://github.com/kseg97)

## Expresiones de Gratitud 🎁

* **Contribución PyImageSearch** - *Base del sistema* - [Link al proyecto](https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/)
* Comenta a otros sobre este proyecto 📢 