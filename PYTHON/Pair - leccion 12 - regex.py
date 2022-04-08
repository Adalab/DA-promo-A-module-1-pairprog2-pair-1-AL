import os
import re

nombre_email = 'Contenido Pair ficheros 2.txt'
carpeta = '/home/adalaber/Escritorio'
ubi_archivo = carpeta + '/' + nombre_email

#1. Extraer el email del remitente

with open(ubi_archivo) as email:  
    info_remitente = re.findall('From:.*', email.read())
    #print(info_remitente)
    email_remitente = re.search('<', info_remitente[0])
    email_remitente1 = re.search('>', info_remitente[0])
    #print(email_remitente)
    #print(email_remitente1)
    print('1. El email del remitente es el siguiente:', info_remitente[0][25:53])
    
   

#2. Extraer el nombre de la persona que recibió el email.

with open(ubi_archivo) as email:  
    info_destinatario = re.findall('From:.*', email.read())
    #print(info_destinatario)

    nombre_destinatario = re.findall('\".*\"', info_destinatario[1])
    print('2. El nombre del destinatario es el siguiente:',nombre_destinatario[0])
    


#3. El día en el que se mandó el email.

with open(ubi_archivo) as email:  
    fecha = re.findall('Date:.*', email.read())
    #print(fecha)

    fecha_envio = re.findall('[^Date: ].*[^\d\d\:]', fecha[0])
    print('3. La fecha de envio es:', fecha_envio[0])
    


#4. El asunto del email.

with open(ubi_archivo) as email:  
    asunto = re.findall('Subject:.*', email.read())
    #print(asunto)

    subject = re.findall('[^Subject: ].*', asunto[0])
    print('4. El asunto del email es el siguiente:', subject[0])


#5. Guarda todos los resultados en un diccionario

diccionario_email = {'info_remitente':info_remitente[0][25:53], 'info_destinatario':nombre_destinatario[0], 'fecha': fecha_envio[0], 'asunto':subject[0]}
print(diccionario_email)
    