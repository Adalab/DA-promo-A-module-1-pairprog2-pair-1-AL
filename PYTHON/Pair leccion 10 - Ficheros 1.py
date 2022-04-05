import os

#PRIMERA FUNCION

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

def segunda_fun():
    print('Porfavor introduzca la dirección del fichero')
    #./primera-toma-contacto/datos 
    ruta_fichero = input()
    os.chdir(ruta_fichero)

    #No se como utilizar el if y el else
    
    f = open('saludo.txt')
    linea4 = f.readlines()
    f.close()

    print(linea4[3])




segunda_fun()