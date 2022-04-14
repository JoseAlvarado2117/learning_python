
def evaluacion(nota):
    valoracion = "aprobado"

    if nota < 0 or nota > 10:
        mensaje = "Nota incorrecta, la nota debe estar enter 0 y 10 puntos!"
        return mensaje
    elif nota < 5:
        valoracion = "suspenso"
        return valoracion
    elif (nota >= 5) and (nota < 7):
        return valoracion
    elif (nota >= 7) and (nota < 9):
        valoracion = "excelente"
        return valoracion
    elif nota >= 9:
        valoracion = "sobresaliente"
        return valoracion
    else:
        return "error"


nota_alumno = input("Cuál es la nota del alumno: ")
nota_alumno = float(nota_alumno)

print(evaluacion(nota_alumno))
