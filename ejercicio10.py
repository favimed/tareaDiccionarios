base_de_datos = {}

def agregar_cliente():
    nif = input("NIF del cliente: ")
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    correo = input("Correo del cliente: ")
    preferente = input("¿Es un cliente preferente? (Sí/No): ").lower()
    if preferente == "sí":
        preferente = True
    else:
        preferente = False
    base_de_datos[nif] = {'nombre': nombre, 'dirección': direccion, 'teléfono': telefono, 'correo': correo, 'preferente': preferente}

def eliminar_cliente():
    nif = input("Di el NIF del cliente que quieres eliminar: ")
    if nif in base_de_datos:
        del base_de_datos[nif]
        print("Cliente eliminado.")
    else:
        print("El cliente no existe.")

def mostrar_cliente():
    nif = input("Di el NIF del cliente que quieres mostrar: ")
    if nif in base_de_datos:
        cliente = base_de_datos[nif]
        print("Datos del cliente:")
        print(f"NIF: {nif}")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("El cliente no existe.")

def listar_clientes():
    print("Lista de todos los clientes:")
    for nif, datos_cliente in base_de_datos.items():
        nombre = datos_cliente['nombre']
        print(f"NIF: {nif}, Nombre: {nombre}")

def listar_clientes_preferentes():
    print("Lista de clientes preferentes:")
    for nif, datos_cliente in base_de_datos.items():
        if datos_cliente['preferente']:
            nombre = datos_cliente['nombre']
            print(f"NIF: {nif}, Nombre: {nombre}")

while True:
    print("\nMenú de opciones:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion = input("Elige una opción (1/2/3/4/5/6): ")

    if opcion == '1':
        agregar_cliente()
    elif opcion == '2':
        eliminar_cliente()
    elif opcion == '3':
        mostrar_cliente()
    elif opcion == '4':
        listar_clientes()
    elif opcion == '5':
        listar_clientes_preferentes()
    elif opcion == '6':
        break
    else:
        print("No valida, elige una opción del menú.")