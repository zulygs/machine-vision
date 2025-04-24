import cv2
import mediapipe as mp
import serial, time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

mano_mp = mp.solutions.hands
manos = mano_mp.Hands(max_num_hands=1)
dibujo = mp.solutions.drawing_utils

puntos_verdes  = dibujo.DrawingSpec(color=(0,255,0), thickness=3, circle_radius=4)
lineas_rojas   = dibujo.DrawingSpec(color=(0,0,255), thickness=2)

video = cv2.VideoCapture(0)
dedos_previos = -1
puntas = [8, 12, 16, 20]

def contar_dedos(puntos):
    total = 1 if puntos.landmark[4].x < puntos.landmark[3].x else 0
    total += sum(1 for p in puntas if puntos.landmark[p].y < puntos.landmark[p-2].y)
    return total

while True:
    ok, cuadro = video.read()
    if not ok:
        break
    imagen = cv2.flip(cuadro, 1)
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    resultado = manos.process(imagen_rgb)

    if resultado.multi_hand_landmarks:
        for puntos in resultado.multi_hand_landmarks:
            dedos = contar_dedos(puntos)
            
            dibujo.draw_landmarks(
                imagen,
                puntos,
                mano_mp.HAND_CONNECTIONS,
                puntos_verdes,     
                lineas_rojas       
            )
            if dedos != dedos_previos:
                arduino.write(str(dedos).encode())
                dedos_previos = dedos

    cv2.imshow("Contador de Dedos", imagen)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
arduino.close()
