fecha = input("Escribe una fecha en formato dd/mm/aaaa: ")

if:
    dia, mes, anio = fecha.split('/')
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

    if mes >= 1 and mes <= 12:
        print(f"{dia} de {meses[mes - 1]} de {anio}")
    else:
        print("El mes no es válido.")
else:
    print("El formato de la fecha es incorrecto. Tiene que ser dd/mm/aaaa.")
