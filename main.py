# main.py
# Punto de arranque del programa. Aquí se importan las clases y se ejecuta la simulación.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    print("=== INICIANDO SISTEMA DE GESTIÓN DE RESTAURANTE ===\n")
    
    # 1. Crear el servicio principal (Restaurante)
    mi_restaurante = Restaurante("Sabores Gourmet")
    
    # 2. Crear objetos de la clase Producto (Platos y Bebidas)
    prod1 = Producto("Hamburguesa Artesanal", 12.50, "Comida")
    prod2 = Producto("Pizza Pepperoni", 15.00, "Comida")
    prod3 = Producto("Limonada Imperial", 3.50, "Bebida")
    prod4 = Producto("Flan de la Casa", 4.50, "Postre")
    
    # 3. Agregar los productos al servicio principal
    print("--- Registrando Productos en el Menú ---")
    mi_restaurante.registrar_producto(prod1)
    mi_restaurante.registrar_producto(prod2)
    mi_restaurante.registrar_producto(prod3)
    mi_restaurante.registrar_producto(prod4)
    
    # 4. Crear objetos de la clase Cliente
    cliente1 = Cliente("Didier Moncayo", 101)
    cliente2 = Cliente("Tayana Maldonado", 102)
    
    # 5. Agregar los clientes al servicio principal
    print("\n--- Registrando Clientes ---")
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)
    
    # 6. Simular que los clientes realizan pedidos
    cliente1.agregar_al_pedido(prod1)  # Didier pide una Hamburguesa
    cliente1.agregar_al_pedido(prod3)  # Didier pide una Limonada
    
    cliente2.agregar_al_pedido(prod2)  # Tayana pide una Pizza
    cliente2.agregar_al_pedido(prod4)  # Tayana pide un Flan
    
    # 7. Mostrar la información registrada de forma organizada en la consola
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_estado_clientes()

if __name__ == "__main__":
    main()
