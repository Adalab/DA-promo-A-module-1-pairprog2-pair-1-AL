import xml.etree.ElementTree as ET

#En este ejercicio tendréis que crear una función que reciba 
#el nombre del archivo xml y que devuelva lo siguiente:

# - Qué tag y atributos tiene el archivo xml. .tag/.attrib
#- La descripción de cada una de las películas que tenemos en ese archivo.
#- Los años en que fueron estrenadas las películas.

#Pistas 
#La función debe recibir un parámetro, el nombre del archivo xml.
#Tendréis que utlizar un bucle for para recorrer todo el archivo xml y extraer la información que os pedimos.
#Recordad el método .text para extraer el texto de un elemento.



def segunda_funcion(nombre_archivo):
    archivo = ET.parse(nombre_archivo)
    root = archivo.getroot()

    #for child in root.iter():
        #print(child.tag)
 
    for child in root:
        print(child.tag, child.attrib)
        for subchild in child:
            print('  ',subchild.tag, subchild.attrib)
            for subsubchild in subchild:
                print(' ', subsubchild.tag, subsubchild.attrib)
                for subsubsubchild in subsubchild:
                    print(' ', subsubsubchild.tag, subsubsubchild.attrib)

    for descripcion in root.findall('movie'):
        print(descripcion.find('description').text)

    
    
    

segunda_funcion('peliculas.xml')

