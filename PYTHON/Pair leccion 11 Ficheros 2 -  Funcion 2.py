import xml.etree.ElementTree as ET

# Qué tag y atributos tiene el archivo xml.
# La descripción de cada una de las películas que tenemos en ese archivo.
# Los años en que fueron estrenadas las películas.


def segunda_funcion(nombre_archivo):
    archivo = ET.parse(nombre_archivo)
    root = archivo.getroot()
    
    for child in root: #genre
        print(child.tag, child.attrib)
        for subchild in child: #decade
            print(' ',subchild.tag, subchild.attrib)
            for subsubchild in subchild.findall('movie'): #movie
                print('  ', subsubchild.tag, subsubchild.attrib)
                print('   year:',subsubchild.find('year').text)
                print('    description:',subsubchild.find('description').text)
                

                

segunda_funcion('peliculas.xml')

    
 
                   
    

    
    
    

segunda_funcion('peliculas.xml')

