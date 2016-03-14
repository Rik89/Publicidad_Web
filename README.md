# Publicidad_Web
Estudiantes de la Universidad de Guayaquil aplicando metodos de soluciones a las diversas problematicas en la World Wide Web, para eso hemos implementao un algoritmo que optimizaria y detectaria las falencias que ocurre por medio de la publicidad Web.

El proyecto en si trata de consultar una API de cualquier pagina en nuestro caso la API de TWITTER estamos trabajando
una vez obtenido las llaves que son obligatorias en el codigo basado en python nos ejecutara y crear un archivo con todos los datos que nosotros requerimos en este caso publicidad.

Ahora el codigo te baja esos datos para poder trabajar.
Los algoritmos que hemos estudiado son Algoritmo Online y Offline junto con Greddy y Algoritmo de Coincidencia
en el archivo se encontraran con Greddy codigo que si ejecuta y bota resultados como el de ordenar dichos datos de un archivo.

El siguiente codigo es el que nos interesa ya que este va comparando y viendo la cadena de caracteres pares, aun no esta 100% completo falta dar unos ajustes pero tratamos de pulirlo de a poco.

Para poder usar Python debemos instalar librerias deacuerdo a la version 
pip2 intall tweepy  una de las principales pongo el 2 por mi version python 2.7
y demas paquetes a utilizar.

Entre los paquetes a instalar son
numpy
matplotlib
pandas
tweepy
y libreria c++ para python version 2.7

El Algoritmo de coincidencia es el que va a comparar nuestros datos he subido en la carpete input dos diccionarios de datos directamente de la Api Twitter descargados sobre publicidad(abarca deporte,videos,imagenes) y lo que hace es comparar ambos archivos y ver donde hay similitud, en caso de encontrar similitud elimina uno de ellos y crea un nuevo archivo "new_file" con solo la informacion necesaria y ya no repetida por asi decirlo.
