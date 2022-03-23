listadopeliculas = open("listadopeliculas.txt", "r")  # En primer lugar abrimos el archivo .txt en el que tenemos todas las películas.
                                                      # Este es el primer paso.


## Contador de películas ##


Contador = 0                                          # Creamos las variables que vamos a utilizar para el contador.
LecturaLineas = 0

for LecturaLineas in listadopeliculas:                # Mediante el bucle for vamos a decirle al contador que nos cuente uno por uno
    Contador += 1                                     # para que nos cuente línea por línea.

print("El numero de peliculas es:", Contador)

listadopeliculas.close()


## Visualizador de Películas en pantalla ##


Archivo = 'listadopeliculas.txt'                      # Creamos una variable donde definimos el archivo que queremos utilizar para leer, en este caso es el de Disney.
Visualizar = open(Archivo, "r")                       # A su vez vamos a crear otra variable en la que vamos a abrir el archivo, para próximamente leerlo para imprimirlo por pantalla.

print(Visualizar.read())                              # Ahora imprimiremos por la terminal dicho archivo, para ello utilizaremos el método read, que es el que nos va a permitir
                                                      # Mostrar el repertorio de películas.
listadopeliculas.close()


## Visualizar sin los "." en los Nombres ##


Filtrar = Archivo.split(".")

print(Filtrar)

