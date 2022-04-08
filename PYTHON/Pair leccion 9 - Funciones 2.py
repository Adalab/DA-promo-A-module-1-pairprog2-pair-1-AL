from email.headerregistry import ContentDispositionHeader

# Ejercicios Pair Funciones 2

# Ejercicio 1 - Calculadora de puntos 


def calculadora(string):
    resultado = 0
    tupla = tuple(string.split())
    a, simbolo, b = tupla
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
        print("Esta calculadora solo admite suma, resta, multiplicación y división entre enteros. Vuelve a intentarlo con una operación que podamos resolver :)")

    total = '.'*resultado
    print((string, '->', total))
    return total


string = ("..... + ...............")
# string = ("..... - ...")
# string = ("..... * ...")
# string = ("..... // ..")
# string = ". // .."
# string = ".. - .."
calculadora(string)


# Ejercicio 2
# Te despides de tu mejor amigo, "Nos vemos el próximo año". 
#El siguiente año que le felicites a tu mejor amigo no puede tener ningún dígito repetido.

def reencuentro(año):
    no_reen = False
    año = año + 1

    while no_reen == False:
        repetido = 0  
        # convierto el año en una lista de strings ('7','7','1','2')
        lista_num = list(str(año))
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
#reencuentro(1001)
#reencuentro(1123)
#reencuentro(2001)

# Ejercicio 3
# Tenéis que crear un función que chequee la vida de un evaporador que contiene un gas. 
# Conocemos el contenido del evaporador (contenido en ml), el porcentaje de gas que se pierde cada día 
# y el umbral en porcentaje a partir del cual el evaporador deja de ser útil.


def vida_evaporador(contenido, porcentaje, umbral):
    contenido = int(contenido)
    porcentaje = int(porcentaje) / 100
    umbral = int(umbral) / 100
    utilidad = contenido * umbral
    #print(contenido, porcentaje, umbral, utilidad)

    dias = 0
    while contenido > utilidad:
        contenido = contenido - (contenido * porcentaje)
        dias = dias + 1

    print(dias)
    return(dias)


vida_evaporador(10, 10, 5)
# = > 29
#vida_evaporador(10, 10, 10) 
# = > 22


# Ejercicio 4
# Definid una función que tome como argumento un entero y devuelva True o False 
# dependiendo de si el número es primo o no. 


def soy_primo(num):
    primo = False
    if num > 1:
        if num % 2 == 0:
            return(primo)
        else:
            if num % 3 == 0:
                return(primo)
            elif num / 3 < 3:
                primo = True
                return(primo)
            else:
                if num % 5 == 0:
                    return(primo)
                elif num / 5 < 5:
                    primo = True
                    return(primo)
                else:
                    if num % 7 == 0:
                        return(primo)
                    elif num / 7 < 7:
                        primo = True
                        return(primo)
                    else:
                        if num % 11 == 0:
                            return(primo)
                        elif num / 11 < 11:
                            primo = True
                            return(primo)
                        else:
                            primo = True
                            return (primo)
    else:
        return(primo)


print(soy_primo(-1))

# 0 => False
# 2 => True
# 73 => True
# -1 => False
# 5099 => True


# Ejercicio 5 
# Cread una función que toma una lista que contiene los nombres de las personas a las que les gusta 
# un artículo.

def lista_likes(lista):

    if len(lista) > 1:
        if len(lista) == 1:
            print("A", lista[0], "le gusta esto.")
        elif len(lista) == 2:
            print("A", lista[0], "y", lista[1], "les gusta esto.")
        elif len(lista) == 3:
            print("A", lista[0], ",", lista[1],
                  "y", lista[2], "les gusta esto.")
        else:
            print("A", lista[0], ",", lista[1], "y otros",
                  (len(lista) - 2), " más les gusta esto.")
    else:
        print("A nadie le gusta esto")


lista = ["Jacoba", "Alex", "María", "Antonio", "Fernando"]
# [] - -> "A nadie le gusta esto"
# ["Paola"] - -> "A Peter le gusta esto"
# ["Jacoba", "Alex"] - -> "A Jacob y Alex les gusta esto"
# ["Maria", "Juana", "Lola"] - -> "A Max, John y Mark les gusta esto"
# ["Alex", "Jacoba", "Lola", "Carmen"]--> "A Alex, Jacob y 2 más les gusta esto"
# ["Alex", "Jacoba", "Lola", "Carmen", "Mariana"]--> "A Alex, Jacoba y 3 más les gusta esto"

lista_likes(lista)
