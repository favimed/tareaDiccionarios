divisas = {'euro': '€', 'dollar': '$', 'yen': 'Y'}

divisa = input("Escribe una divisa: ")

if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}.")
else:
    print("Esta divisa no está en el diccionario.")