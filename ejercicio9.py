facturas = {}

monto_cobrado = 0.0
monto_pendiente = 0.0

while True:
    accion = input("¿Qué deseas realizar? (añadir, pagar, terminar): ")
    
    if accion == 'añadir':
        num_factura = input("Número de factura: ")
        costo = float(input("Costo de la factura: "))
        facturas[num_factura] = costo
        monto_pendiente += costo
    elif accion == 'pagar':
        num_factura = input("Número de factura a pagar: ")
        costo = facturas.get(num_factura, 0)
        if costo > 0:
            del facturas[num_factura]
            monto_cobrado += costo
            monto_pendiente -= costo
        else:
            print("La factura no existe o ya ha sido pagada.")
    elif accion == 'terminar':
        break
    else:
        print("La acción no es válida. Elige 'añadir', 'pagar' o 'terminar.")

print(f"Monto total cobrado: {monto_cobrado}")
print(f"Monto total pendiente de cobro: {monto_pendiente}")