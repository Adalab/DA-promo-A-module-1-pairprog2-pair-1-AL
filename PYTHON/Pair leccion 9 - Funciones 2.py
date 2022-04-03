#Ejercicios Pair Funciones 2

#Ejercicio 1 - Calculadora de puntos

def calculadora(string):
    resultado = 0
    tupla = tuple(string.split())
    a,simbolo,b = tupla
    puntos1 = len(a)
    puntos2 = len(b)
    

    if simbolo == '+':
        resultado = puntos1 + puntos2 
    elif simbolo == '-':
        if puntos1 >= puntos2:
            resultado = puntos1 - puntos2 
        else:
            print("El resultado es negativo")
    elif simbolo == '*':
        resultado = puntos1 * puntos2 
    elif simbolo == '//':
        resultado = puntos1 // puntos2
    else:
        print("esta calculadora solo admite suma, resta, multiplicacion y division entre enteros")

    total = '.'*resultado
    print((string, '->', total))
    return total
    


x = calculadora("..... + ...............")
string1 = ("..... + ...............")
string2 = ("..... - ...")
string3 = ("..... * ...")
string4 = ("..... // .." )
string5 = ". // .."
string6 = ".. - .." 

#Ejercicio 2
def reencuentro(año):
    no_reen = False
    año = año + 1
    
    while no_reen == False:
        repetido = 0 #El 0 y el 1 es como poner False y True respectivamente, el False/0 es que no tiene valor y el True/1 que hay un valor 
        lista_num = list(str(año)) #convierto el año en una lista de strings ('7','7','1','2')
        for str_num in lista_num:
            if lista_num.count(str_num) > 1:
                repetido = 1
                break
        if repetido == 1:
            año = año + 1 
        else:
            no_reen = True

    print('Tu proximo año de reecuentro es:', año)

reencuentro(7712)  
reencuentro(1001)
reencuentro(1123)
reencuentro(2001)