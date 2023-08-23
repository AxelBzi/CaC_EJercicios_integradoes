#Ejercicio 1(maximo comun divisor)
def mcd(x,y):
    num = 0
    while y !=0:
        num = y
        y = x % y
        x = num
    return x

#Ejercicio 2(minimo comun multiplo)
def mcm(x,y):
    return (x * y)// mcd(x,y)

#Ejercicio 3
def palabras_Repetidas(cadena):
    lista = cadena.split()
    return {palabra: lista.count(palabra) for palabra in lista}

#Ejercicio 4
def palabra_Mas_Usada(cadena):
    dicc = palabras_Repetidas(cadena)
    palabra = max(dicc,key=dicc.get)
    return palabra,dicc[palabra]

#Ejercicio 5
def get_int():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error: Ingrese un numero entero")

def get_int_recursivo():
    try:
        numero = int(input("Ingrese un numero: "))
        return numero
    except ValueError:
        print("Error: Ingrese un numero entero")
        get_int_recursivo()




