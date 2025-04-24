# machine-vision

El proyecto detecta y cuenta los dedos que levantas usando la cámara de la computadora y librerías de visión por computadora. Cada dedo se reconoce a partir de puntos clave en la mano. Cuando el número de dedos cambia, ese valor se envía a un circuito con un display, que actualiza la cifra mostrada en tiempo real.

# Funcionamiento:

1. OpenCV toma video
2. MediaPipe localiza los puntos de la mano
3. con esos puntos validamos la posicion de los dedos y de esta forma comparamos si la punta de los dedos esta mas arriba el dedo cuenta como levantado.
4. sumamos los dedos y si el numero cambia se envia al arduino el cual escribe en el display el numero de dedos levantado.

# Requisitos:

1. Libreria OpenCV
2. Libreria MediaPipe
3. Arduino Uno
4. Display de 7 segmentos en mi caso Anodo Comun
