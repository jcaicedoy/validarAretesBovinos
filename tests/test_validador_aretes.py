from src.validador_aretes import (
    limpiar_codigo,
    validar_codigo,
    procesar_codigos
)


def test_limpiar_codigo():
    assert limpiar_codigo(" ec123456789 ") == "EC123456789"


def test_codigo_valido():
    valido, mensaje = validar_codigo("EC123456789")
    assert valido is True
    assert mensaje == "Código válido"


def test_codigo_vacio():
    valido, mensaje = validar_codigo("")
    assert valido is False
    assert mensaje == "El código está vacío"


def test_codigo_sin_prefijo_ec():
    valido, mensaje = validar_codigo("AB123456789")
    assert valido is False
    assert mensaje == "El código debe iniciar con EC"


def test_codigo_con_longitud_incorrecta():
    valido, mensaje = validar_codigo("EC12345")
    assert valido is False
    assert mensaje == "El código debe tener 9 dígitos después de EC"


def test_codigo_con_letras_en_numeracion():
    valido, mensaje = validar_codigo("EC12345A789")
    assert valido is False
    assert mensaje == "Después de EC solo deben existir números"


def test_procesar_codigos():
    codigos = ["EC123456789", "AB123456789"]
    resultados = procesar_codigos(codigos)

    assert len(resultados) == 2
    assert resultados[0]["valido"] is True
    assert resultados[1]["valido"] is False
    from src.validador_aretes import (
    limpiar_codigo,
    validar_codigo,
    procesar_codigos
)


def test_limpiar_codigo():
    assert limpiar_codigo(" ec123456789 ") == "EC123456789"


def test_codigo_valido():
    valido, mensaje = validar_codigo("EC123456789")
    assert valido is True
    assert mensaje == "Código válido"


def test_codigo_vacio():
    valido, mensaje = validar_codigo("")
    assert valido is False
    assert mensaje == "El código está vacío"


def test_codigo_sin_prefijo_ec():
    valido, mensaje = validar_codigo("AB123456789")
    assert valido is False
    assert mensaje == "El código debe iniciar con EC"


def test_codigo_con_longitud_incorrecta():
    valido, mensaje = validar_codigo("EC12345")
    assert valido is False
    assert mensaje == "El código debe tener 9 dígitos después de EC"


def test_codigo_con_letras_en_numeracion():
    valido, mensaje = validar_codigo("EC12345A789")
    assert valido is False
    assert mensaje == "Después de EC solo deben existir números"


def test_procesar_codigos():
    codigos = ["EC123456789", "AB123456789"]
    resultados = procesar_codigos(codigos)

    assert len(resultados) == 2
    assert resultados[0]["valido"] is True
    assert resultados[1]["valido"] is False