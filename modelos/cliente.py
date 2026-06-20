# modelos/cliente.py

class Cliente:
    def __init__(self, nombre: str, id_cliente: int):
        """
        Constructor de la clase Cliente.
        Inicia los atributos de un cliente con su nombre e identificación.
        """
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.pedido_actual = []  # Lista de productos que el cliente consume

    def agregar_al_pedido(self, producto):
        """
        Agrega un producto a la lista de consumo del cliente.
        """
        self.pedido_actual.append(producto)

    def calcular_total_pedido(self) -> float:
        """
        Calcula el costo total de los productos en el pedido del cliente.
        """
        return sum(producto.precio for producto in self.pedido_actual)

    def __str__(self) -> str:
        """
        Representación en texto del cliente y el estado de su pedido.
        """
        total = self.calcular_total_pedido()
        return f"Cliente: {self.nombre} (ID: {self.id_cliente}) | Productos pedidos: {len(self.pedido_actual)} | Total a pagar: ${total:.2f}"
