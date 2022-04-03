
#Ejercicio 1
def funcion1(string1, string2):
    if string1 == "" and string2 == "":
        print("0") 
    elif string1 == "":
        print(string2) 
    elif  string2 == "":
        print(string1)
    else:
        num1 = int(string1)
        num2 = int(string2)
        total_string = num1 + num2
        print("La suma de", string1, "+", string2, "es", str(total_string))

#funcion1("4", "5")
#funcion1("34", "5")
#funcion1("", "")
#funcion1("2", "")
#funcion1("-5", "3")

#Ejercicio 2
def comparaciones(arr1, arr2):
    resultado = []
    i = 0
    for comparacion in arr1:
        if arr1[i] >= arr2[i]:
            resultado.append(arr1[i])
        else:
            resultado.append(arr2[i])
        i = i + 1   
    #print('resultado:', resultado)

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
comparaciones(arr1, arr2)

#Ejercicio 3

def parentesis(string):
    resultado = []
    
    for letra in string:
        if string.count(letra.lower()) > 1:
            resultado.append(')')
        else:
            resultado.append('(')

    resultado = "".join(resultado)
    #print(resultado)  


parentesis("Success")
# "din"      =>  "((("
#"recede"   =>  "()()()"
#"Success"  =>  ")())())"
#"(( @"     =>  "))((" 
#"Ocvl@GamFLAFkixkS" => "((()(()()))))(()("



