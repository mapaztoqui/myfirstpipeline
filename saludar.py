def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado.

    Si el nombre está vacío o no es texto, lanza ValueError.
    """
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("Nombre inválido")
    return f"Hola, {nombre.strip()}!"


if __name__ == "__main__":
    persona = input("¿Cómo te llamas? ")
    print(saludar(persona))
