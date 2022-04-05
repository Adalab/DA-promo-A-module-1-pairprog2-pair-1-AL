import os

#Primera Funcion

def primera_fun():
    print(os.getcwd())
    
    if 'aprendiendo-ficheros' in os.listdir():
        print('La carpeta ya existe')
        os.chdir('./aprendiendo-ficheros')
        #print(os.getcwd())
        if 'datos' in os.listdir('aprendiendo-ficheros'):
            print('La carpeta datos ya existe')
        else:
            os.mkdir('datos')
            print('La carpeta datos ha sido creada')
    else:
        os.mkdir('aprendiendo-ficheros')
        print('La carpeta ha sido creada')
        
        os.chdir('./aprendiendo-ficheros')
        #print(os.getcwd())
        if 'datos' in 'aprendiendo-ficheros':
            print('La carpeta datos ya existe')
        else:
            os.mkdir('datos')
            print('La carpeta datos ha sido creada')

   
#os.rename('/home/adalaber/Descargas/saludo.txt', '')

primera_fun()