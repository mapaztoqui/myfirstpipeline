import pytest
from saludar import saludar


def test_saludo_correcto():
    assert saludar("Mariana") == "Hola, Mariana!"


def test_saludo_con_espacios():
    assert saludar("  Fran  ") == "Hola, Fran!"


def test_nombre_vacio():
    with pytest.raises(ValueError):
        saludar("")


def test_nombre_no_texto():
    with pytest.raises(ValueError):
        saludar(123)
