def limpiar_codigo(codigo):
    """Elimina espacios y convierte el código a mayúsculas."""
    if codigo is None:
        return ""
    return codigo.strip().upper()


def validar_codigo(codigo):
    """
    Valida un código oficial de identificación animal.
    Formato válido: EC + 9 dígitos.
    Ejemplo: EC123456789
    """
    codigo_limpio = limpiar_codigo(codigo)

    if not codigo_limpio:
        return False, "El código está vacío"

    if not codigo_limpio.startswith("EC"):
        return False, "El código debe iniciar con EC"

    numeros = codigo_limpio[2:]

    if len(numeros) != 9:
        return False, "El código debe tener 9 dígitos después de EC"

    if not numeros.isdigit():
        return False, "Después de EC solo deben existir números"

    return True, "Código válido"


def procesar_codigos(lista_codigos):
    """Procesa una lista de códigos y devuelve el resultado de cada uno."""
    resultados = []

    for codigo in lista_codigos:
        es_valido, mensaje = validar_codigo(codigo)
        resultados.append({
            "codigo": limpiar_codigo(codigo),
            "valido": es_valido,
            "mensaje": mensaje
        })

    return resultados


def leer_codigos_desde_archivo(ruta_archivo):
    """Lee códigos desde un archivo de texto."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        raise FileNotFoundError("El archivo no fue encontrado")


def mostrar_resultados(resultados):
    """Muestra los resultados en consola."""
    for resultado in resultados:
        estado = "Válido" if resultado["valido"] else "Inválido"
        print(f'{resultado["codigo"]} -> {estado}: {resultado["mensaje"]}')


if __name__ == "__main__":
    codigos = leer_codigos_desde_archivo("codigos.txt")
    resultados = procesar_codigos(codigos)
    mostrar_resultados(resultados)