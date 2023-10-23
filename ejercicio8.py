diccionario = {}

entrada = input("Escribe las palabras en español e inglés (ejemplo: hola:hello, adiós:goodbye): ")

pares = entrada.split(',')
for par in pares:
    palabra, traduccion = par.split(':')
    diccionario[palabra] = traduccion

frase_espanol = input("Escribe una frase en español: ")

palabras = frase_espanol.split()
frase_traducida = []
for palabra in palabras:
    traduccion = diccionario.get(palabra, palabra) 
    frase_traducida.append(traduccion)

frase_ingles = ' '.join(frase_traducida)
print(f"Frase traducida: {frase_ingles}")