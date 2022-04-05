import os
import xml.etree.ElementTree as ET

#Funcion 1
#Si el fichero no existe, debe crearlo, insertar contenido y mostrar su contenido.
#Si el fichero existe pregunta al usuario si quiere sobreescribirlo. 
#En caso de Si, sobreescribe el fichero, insertad contenido y leedlo. En caso de No, no hace nada.

nombre_email = 'Contenido Pair ficheros 2.txt'
carpeta = '/home/adalaber/Escritorio'
ubi_archivo = carpeta + '/' + nombre_email

def lectura_txt(nombre, mode, encoding):

    if nombre in os.listdir():
        print('El archivo ya existe, ¿quieres sobreescribirlo?')
        respuesta = input('S/N')
        if respuesta == 'S':
            with open(ubi_archivo) as f:
                with open(nombre, mode, encoding) as g:
                    g.write(f)
        elif respuesta == 'N':
            pass
        else:
            print('Asegurate de escribir S o N')
    else:
        with open(ubi_archivo) as f:
            h = open(nombre, mode, encoding, 'x')
            h.write(f)






lectura_txt('email.txt', 'rt', 'utf-8')