# servicios/restaurante.py
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre: str):
        """
        Constructor de la clase Restaurante.
        Administra el menú (productos) y los clientes registrados.
        """
        self.nombre = nombre
        self.menu_productos = []
        self.clientes_registrados = []

    def registrar_producto(self, producto: Producto):
        """
        Agrega un producto nuevo al menú del restaurante.
        """
        self.menu_productos.append(producto)
        print(f"✔ Producto registrado en el menú: {producto.nombre}")

    def registrar_cliente(self, cliente: Cliente):
        """
        Registra a un cliente en el sistema del restaurante.
        """
        self.clientes_registrados.append(cliente)
        print(f"✔ Cliente registrado en el sistema: {cliente.nombre}")

    def mostrar_menu(self):
        """
        Muestra en consola todos los productos disponibles de forma organizada.
        """
        print(f"\n--- MENÚ DE {self.nombre.upper()} ---")
        if not self.menu_productos:
            print("El menú está vacío.")
        for producto in self.menu_productos:
            print(producto)
        print("-" * 30)

    def mostrar_estado_clientes(self):
        """
        Muestra la información de todos los clientes y sus cuentas actuales.
        """
        print(f"\n--- ESTADO DE CLIENTES EN {self.nombre.upper()} ---")
        if not self.clientes_registrados:
            print("No hay clientes registrados.")
        for cliente in self.clientes_registrados:
            print(cliente)
            if cliente.pedido_actual:
                print("  Detalle del pedido:")
                for prod in cliente.pedido_actual:
                    print(f"    - {prod.nombre}: ${prod.precio:.2f}")
        print("-" * 30)
