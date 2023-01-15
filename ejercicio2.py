#------------------------------
#Ejercicio: Práctica P9 --> Manejo de servocon retroalimentación posicional
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 16/1/23
#Objetivo: encontrar la ecuación lineal que asocie velocidad a un ciclo
#------------------------------

#!/usr/bin/env python3

import sys, tty, termios, time, pigpio

MAX_SPEED = 1720
MIN_SPEED = 1520
velocidad = 0
negativo = 1

servoPin = 14 # numeracion en modo BCM (que es el usado por defecto por pigpio)

miServo = pigpio.pi() # instancia de la clase pi de la libreria pigpio
                      # Usaremos el demonio pigpiod para comandar al motor por teclado
                      # Por ello, IMPORTANTE, hay que lanzar el demonio: sudo pigpiod

def leerOrden(): # para leer orden por teclado a comandar al motor
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)

  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)

  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

'''
  Según especificaciones de la compañía fabricante de estos servos, Parallax,
  la modulación PWM de estos servos tiene los siguientes rangos:
  - Girar en un sentido: [1280...1480]
  - Parar: 1500
  - Girar en el otro: [1520...1720]

  Mientras más cerca al valor 1500, más despacio; cuanto más alejado, más rápido.
'''

def parar ():
  miServo.set_servo_pulsewidth(servoPin, 1500) # 1.º lo ponemos a 0 rpm
  time.sleep(1)
  miServo.set_servo_pulsewidth(servoPin, 0) # y 2.º lo "apagamos"
  miServo.stop()

#==========================================================================

print ("Dispositivo listo. Elija un número del 0 al 9, sentido hortario (h) o antihorario (a):")

while True:
  char = leerOrden()
  if char == "0":
    print("Parando motor")
    parar ()
    print("Motor parado")
    break
    
  elif char == "a":
    print ("Sentido antihorario")
    MAX_SPEED = 1720
    MIN_SPEED = 1530

  #Cambiar maximo ymínimo
  elif char == "h":
    print ("Sentido horario")
    MAX_SPEED = 1460
    MIN_SPEED = 1280
  
  else: 
    #convertir numero de código ascii
    velocidad = (((ord(char)-48)*((MAX_SPEED-MIN_SPEED)))/9)+MIN_SPEED #calculo velocidad
    print(round(velocidad)) #Redondear para mostrar en pantalla
    miServo.set_servo_pulsewidth(servoPin, velocidad)
  
#CASOS DE USO
#si se mete un carácter diferente a los que se pide muestra un error, se introduce en código Ascii


