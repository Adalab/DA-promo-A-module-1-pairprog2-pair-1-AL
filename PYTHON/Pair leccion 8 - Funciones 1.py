
# Ejercicio 1
# Cread una función que reciba 2 números enteros en forma de string como entrada, 
# y dé como resultado la suma (también en forma de string). 


def funcion1(string1, string2):
    if string1 == "" and string2 == "":
        print("0")
    elif string1 == "":
        print(string2)
    elif string2 == "":
        print(string1)
    else:
        num1 = int(string1)
        num2 = int(string2)
        total_string = num1 + num2
        print("La suma de", string1, "+", string2, "es", str(total_string))


# Otros strings a probar:
funcion1("4", "5")
#funcion1("34", "5")
#funcion1("", "")
#funcion1("2", "")
#funcion1("-5", "3")


# Ejercicio 2
# Comparar cada par de enteros de 2 listas, y devolver una nueva lista de números grandes.

def comparaciones(arr1, arr2):
    resultado = []
    i = 0
    for comparacion in arr1:
        if arr1[i] >= arr2[i]:
            resultado.append(arr1[i])
        else:
            resultado.append(arr2[i])
        i = i + 1
    print('resultado:', resultado)

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
comparaciones(arr1, arr2)


# Ejercicio 3
# El objetivo de este ejercicio es convertir una string en un nuevo string en la que cada carácter 
# de la nueva string es "(" si ese carácter aparece sólo una vez en la string original, o ")" 
# si ese carácter aparece más de una vez en la string original. 


def parentesis(string):
    resultado = []

    for letra in string:
        if string.count(letra.lower()) > 1:
            resultado.append(')')
        else:
            resultado.append('(')

    resultado = "".join(resultado)
    print(resultado)


# Strings para probar:
#string = "din"
#   =>  "((("
#string = "recede"
# =>  "()()()"
string = "Success"
# =>  ")())())"
#string = "(( @"
#  =>  "))(("
#string = "Ocvl@GamFLAFkixkS"
# => "((()(()()))))(()("
parentesis(string)

# Ejercicio 4 - BONUS

# Ejercicio 5 - BONUS
