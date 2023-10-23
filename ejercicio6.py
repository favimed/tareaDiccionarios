persona = {}

while True:
    clave = input("Escribe un dato (nombre, edad, sexo, teléfono, correo electrónico) o 'fin' para terminar: ")
    if clave == 'fin':
        break
    valor = input(f"Dale el valor a {clave}: ")
    persona[clave] = valor
    print("Contenido del diccionario:")
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")