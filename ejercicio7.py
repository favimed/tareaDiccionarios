cesta_compra = {}

while True:
    articulo = input("Escribe un artículo o 'fin' para terminar: ")
    if articulo == 'fin':
        break
    precio = float(input(f"Escribe el precio de {articulo}: "))
    cesta_compra[articulo] = precio

print("Lista de la compra:")
total_coste = 0.0
for articulo, precio in cesta_compra.items():
    print(f"{articulo}: {precio} euros")
    total_coste += precio

print(f"Coste de la compra en total: {total_coste} euros")