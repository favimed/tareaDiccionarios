nombre = input("Nombre: ")
edad = input("Edad: ")
direccion = input("Dirección: ")
telefono = input("Teléfono: ")

informacion_usuario = {
    'nombre': nombre,
    'edad': edad,
    'dirección': direccion,
    'teléfono': telefono
}

print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años, vive en {informacion_usuario['dirección']} y su número de teléfono es {informacion_usuario['teléfono']}.")