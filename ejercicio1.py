# Practica 10. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de manejo del Servo Feedback 360 de Parallax

#!/usr/bin/env python3

import sys, tty, termios, time, pigpio

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
def adelante (): # girar en un sentido a velocidad máxima
  miServo.set_servo_pulsewidth(servoPin, 1440)

def atras (): # girar en el otro sentido a velocidad máxima
  miServo.set_servo_pulsewidth(servoPin, 1460)

def parar ():
  miServo.set_servo_pulsewidth(servoPin, 1500) # 1.º lo ponemos a 0 rpm
  time.sleep(1)
  miServo.set_servo_pulsewidth(servoPin, 0) # y 2.º lo "apagamos"
  miServo.stop()

#==========================================================================

print ("Dispositivo listo. Esperando órdenes (w = adelante, s = atrás, x = parar)...")

marcha1 = 1460 #cambio setido --> 1540
marcha2 = 1440 #cambio setido --> 1560
marcha3 = 1400 #cambio setido --> 1600
marcha4 = 1360 #cambio setido --> 1640
marcha5 = 1320 #cambio setido --> 1680
marcha6 = 1280 #cambio setido --> 1720
cambio_sentido = 1580
while True:
  char = leerOrden()

  if char == "1":
    print("Primera marcha")
    miServo.set_servo_pulsewidth(servoPin, marcha1)

  elif char == "2":
    print("Segunda marcha")
    miServo.set_servo_pulsewidth(servoPin, marcha2)
  elif char == "3":
    print("Tercera marcha")
    miServo.set_servo_pulsewidth(servoPin, marcha3)
  elif char == "4":
    print("Cuarta marcha")
    miServo.set_servo_pulsewidth(servoPin, marcha4)
  elif char == "5":
    print("Quinta marcha")
    miServo.set_servo_pulsewidth(servoPin, marcha5)
  elif char == "6":
    print("Sexta marcha")
    miServo.set_servo_pulsewidth(servoPin, marcha6)
    
  elif char == "r":
    print("Cambio de sentido")
    miServo.set_servo_pulsewidth(servoPin, cambio_sentido)

  elif char == "x":
    print("Parando motor")
    parar ()
    print("Motor parado")
    break
