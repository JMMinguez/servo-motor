# P9-Servo

## Introducción
La finalidad de esta práctica es saber utilizar un servo continuo, un motor que gira vueltas completas, en un sentido y en otro, y además dar realimentación de la posición que tiene.

Uno de los problemas más comunes a la hora de comprar servor es que no tienen una rotaciń entera de 360 grados y retroalimentación posicional. 

Es importante tener en cuenta que para poder usa el servo primero hay que poner en la terminal:
```bash
sudo pigpiod
```

## Componentes
El servo que vamos a utilizar en concreto es [Feedback 360 High, Speed Servo](https://cdn.sparkfun.com/assets/8/5/e/4/e/DS-16047.pdf), de la compañía [Parallax](https://www.parallels.com/eu/pd/general/?gclid=EAIaIQobChMIzdO9veiM_AIV0BkGAB16AAdtEAAYASAAEgI6RfD_BwE). Este modelo es un servo continuo normal que utiliza un sensor de efecto Hall sin contacto (modelo AS5600) que proporciona retroalimentación posicional como un tren de pulsos. El servo cuenta con 4 pines: el cable amarillo es el pin de retroalimentación, el rojo a 5V, el negro a tierra y el blanco a un pin GPIO. El circuito queda: 

![Dibujo circuito](https://github.com/rsanchez2021/Image/blob/main/circuito_p9_sensores.jpeg)

## Ejercicio 1 
En el primer ejercicio nos pide simular las mmarchas de un coche con el motor. Hemos decidido poner 6 marchas más la marcha atrás para que queden mejor los valores del motor. AL ser el primero se han puesto directamente los valores del motor para que gira hacia un sentido, posteriormente, en el ejercicio 2, se ha calculado en función de un rango. Destacar que en nuestro motor, los valores para que el motor gire no corresponden con los de fábrica, en nuestro caso los intervalos van de 1280-1460 y de 1540 a 1720.

Acontinuación, os adjuntamos una foto de loq euse vería en pantalla y un vídeo del funcionamiento del motor. Si no puedes ver el vídeo, por favor, pinche [aquí](https://github.com/rsanchez2021/Image/blob/main/ejercicio1_sensores_p9.mp4).


![Pantalla código]()

https://user-images.githubusercontent.com/113595025/212560070-5fae648a-d7f8-4431-97aa-5ecbf52c4ba7.mp4

## Ejercicio 2
En este segundo ejercicio nos pide encontrar la ecuación lineal que nos permita asociar una velocidad a un comando de ciclo de trabajo. En nnuestro caso, hemos cogido un rando de 0 a 9 para así que al pasar el character leído de código Ascii a uno que esté dentro de nuestro rango:
```python
(ord(char)-48)
```
Para la ecuación lineal hemos utilizado lo siguiente:
```python
velocidad = (((ord(char)-48)*((MAX_SPEED-MIN_SPEED)))/9)+MIN_SPEED
```
De esta manera, y cambiando las velocidades máximas y mínimas según sea sentido horario o antihorario hemos podido realizar el ejercicio. Tenemos que tener en cuenta que, al meter otro tipo de caracteres que no sean "a","h","0"-"6", al hacer la conversión saltará un error. A continuación, se muestra un vídeo del funcionamiento del programa:



https://user-images.githubusercontent.com/113595025/212560627-d01b3053-a950-4833-9f87-2f7915c6391f.mp4
