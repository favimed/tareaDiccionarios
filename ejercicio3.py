precios_frutas = {
    'manzana': 0.80,
    'platano': 1.35,
    'pera': 0.85,
    'naranja': 0.70
}

fruta = input("¿Que fruta va a querer?: ").lower() 
if fruta in precios_frutas:
    try:
        cantidad_kilos = float(input("¿Cuantos kilos ha cogido?: "))
        precio_total = precios_frutas[fruta] * cantidad_kilos
        print(f"El precio de {cantidad_kilos} kilos de {fruta} es: {precio_total:.2f} euros")
    except ValueError:
        print("Por favor, escribe una cantidad válida en kilos")
else:
    print("Esta fruta no está en la lista")