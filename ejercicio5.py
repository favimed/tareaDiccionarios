creditos_asignaturas = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos.")

total_creditos = sum(creditos_asignaturas.values())
print(f"El número de créditos del curso es: {total_creditos}")