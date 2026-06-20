# modelos/producto.py

class Producto:
    def __init__(self, nombre: str, precio: float, categoria: str):
        """
        Constructor de la clase Producto.
        Inicia los atributos de un plato o bebida del restaurante.
        """
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self) -> str:
        """
        Representación en texto del producto.
        """
        return f"[{self.categoria.upper()}] {self.nombre} - ${self.precio:.2f}"
