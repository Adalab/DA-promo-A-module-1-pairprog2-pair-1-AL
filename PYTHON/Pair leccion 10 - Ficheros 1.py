import os

#PRIMERA FUNCION
#1. Mostrar en que carpeta estamos trabajando.
#2. Crear carpeta que se llame "aprendiendo-ficheros". 
#3. Cree otra carpeta que se llame "datos" dentro de la carpeta "aprendiendo-ficheros". Dentro de esta
#se encuentra el fichero saludos.txt
#4. Cambiar el directorio de trabajo a la carpeta "datos". 
#5. Cambiar el nombre de la carpeta creada en el punto 2 a "primera-toma-contacto"

def primera_fun(nombre_carpeta, nombre_subcarpeta, cambio_nombre):
    print(os.getcwd())
    ruta_carpeta = ('./' + nombre_carpeta)
    
    if nombre_carpeta in os.listdir():
        print('La carpeta', nombre_carpeta, 'ya existe')
        os.chdir(ruta_carpeta)
        #print(os.getcwd())
        if nombre_subcarpeta in os.listdir():
            print('La carpeta', nombre_subcarpeta, 'ya existe')
        else:
            os.mkdir(nombre_subcarpeta)
            print('La carpeta', nombre_subcarpeta, 'ha sido creada')
    else:
        os.mkdir(nombre_carpeta)
        print('La carpeta ha sido creada')
        
        os.chdir(ruta_carpeta)
        #print(os.getcwd())
        if nombre_subcarpeta in nombre_carpeta:
            print('La carpeta', nombre_subcarpeta, 'ya existe')
        else:
            os.mkdir(nombre_subcarpeta)
            print('La carpeta', nombre_subcarpeta, 'ha sido creada')
    os.chdir('..')
    os.rename(nombre_carpeta, cambio_nombre)

#primera_fun('aprendiendo-ficheros', 'datos', 'primera-toma-contacto')


#SEGUNDA FUNCION
#1. Lea el fichero que se llame "saludo.txt y muestre su contenido completo.
#2. Muestra la línea 4 del fichero

def segunda_fun():
    #print(os.getcwd())
    if 'saludo.txt' in os.listdir():
        ruta_fichero = './saludo.txt'
        print('EL fichero esta en esta carpeta')
    else:
        print('Por favor introduzca la dirección del fichero')
        #./primera-toma-contacto/datos 
        ruta_fichero = input()
        os.chdir(ruta_fichero)
    
    f = open(ruta_fichero)
    print('Mostramos el fichero entero', f.read())
    f.close

    f1 = open(ruta_fichero)
    linea4 = f1.readlines()
    f1.close()

    print('Esta es la cuarta linea del texto:', linea4[3])



segunda_fun()