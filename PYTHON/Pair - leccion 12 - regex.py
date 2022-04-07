import os
import re

nombre_email = 'Contenido Pair ficheros 2.txt'
carpeta = '/home/adalaber/Escritorio'
ubi_archivo = carpeta + '/' + nombre_email



with open(ubi_archivo) as email:  
    info_remitente = re.findall('From:.*', email.read())
    #print(info_remitente)
    email_remitente = re.search('<', info_remitente[0])
    email_remitente1 = re.search('>', info_remitente[0])
    
    #print(email_remitente)
    #print(email_remitente1)
    #print('El email del remitente es el siguiente:', info_remitente[0][25:53])
    
    #indice = info_remitente[0].find('<')
    #print(info_remitente[0][indice +len('')]) #OPCION A buscar una forma facil 
    #OPCION B: separar las palabras por los espacios para buscar la longitud de cada uno de los elementos de From:
    #email_remitente = re.findall('\W[a-z][A-Z].*\d\W', info_remitente)


#2. Extraer el nombre de la persona que recibió el email.
#Pista Tendremos que hacer dos busquedas:
# - Podemos usar el resultado de la primera búsqueda del ejercicio anterior para sacar el nombre.
# - Otra para extraer el nombre únicamente.

with open(ubi_archivo) as email:  
    info_destinatario = re.findall('From:.*', email.read())
    print(info_destinatario)

    print(nombre_destinatario = re.findall('\".*\"', info_destinatario[1]))

    #('\".*\"')
   
    
    #print(email_remitente2)
    #print(email_remitente2a)
    #print('El email del remitente es el siguiente:', info_remitente[1][25:53])





#3. El día en el que se mandó el email.
# Pista 💡 De la misma forma que antes buscamos por From: primero, ahora lo tendremos que hacer con Date: .*
with open(ubi_archivo) as email:  
    fecha = re.findall('Date:.*', email.read())
    #print(fecha)


#4. El asunto del email.
# Pista 💡 Busca primero "Subject:.* y después busca el patrón para extraer el asunto.
#5. Guarda todos los resultados en un diccionario
    