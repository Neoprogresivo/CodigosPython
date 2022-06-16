#Ejercicio GuíaEjerciciosFuncionesPrte1:
#Crear un menú con las siguientes opciones:
#Número Primo
#Factorial
#Palíndrome
#Salir

#Cada opción debe ser una función creada por usted.
#La opción 1, debe ingresar un número entre 1 y 15. Indicar si es Primo.
#La opción 2, debe ingresar un número positivo entre 3 y 10. Calcule su factorial.
#La opción 3, debe ingresar una frase e indicar si es o no Palíndrome (se escribe igual al revés, ejemplo OSO).
#La opción 4, salir del programa con un mensaje y su nombre como autor del programa.
#Cristián Rojas C.
#2022-06-16
#V 1.0

def esPrimo(numero):
    primo = True
    for i in range(2,numero):
        if numero%i == 0:
            primo = False
            break
    return primo

def factorial(numero):
    fact = 1
    for i in range(2, numero + 1):
        fact = fact * i
    return fact

def esPalindrome(texto):
    palindrome = False
    if texto == texto[::-1]:
        palindrome = True
    return palindrome

while True:
    print("♫MENU♫")
    print("1.- Es número primo")
    print("2.- Calcular factorial")
    print("3.- Es Palindrome")
    print("4.- Salir")
    try:
        opcion = int(input("Ingrese su opcion : "))
        if opcion >= 1 and opcion <= 4:
            if opcion == 1:
                primo = int(input("Ingrese un número para saber si es primo : "))
                if esPrimo(primo) == True:
                    print(f"El número {primo}, es primo.")
                else:
                    print(f"El número {primo}, no es primo.")
            elif opcion  == 2:
                fact = int(input("Ingrese un número para conocer su factorial : "))
                print(f"El factorial de {fact} es ", factorial(fact))
            elif opcion == 3:
                palabra = input("Ingrese un texto para saber si es palindrome : ")
                if esPalindrome(palabra) == True:
                    print(f"La palabra {palabra}, es palindrome.")
                else:
                    print(f"La palabra {palabra}, no es palindrome.")
            else:
                print("Desarrollado por Cristián Rojas C.")
                print("Adios")
                break                
        else:
            print("Opción no válida.")        
    except:
        print("Opción ingresada no es válida.")
