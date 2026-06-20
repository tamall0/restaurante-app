# Sistema de Gestión de Restaurante (POO en Python)

Mi nombre es Tayana Aracely Maldonado Loja.
Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado bajo
el paradigma de Programación Orientada a Objetos (POO) en Python. El objetivo principal
del programa es demostrar la correcta modularización de un proyecto, la separación de 
responsabilidades y la comunicación entre archivos mediante importaciones.

## Descripción del Proyecto

El sistema modela de forma básica las operaciones e interacciones principales de un restaurante
a través de tres entidades clave distribuidas en módulos independientes:

1. **Modelos (`modelos/`)**:
   * **`Producto`**: Representa los elementos disponibles en el restaurante (platos, bebidas o
   postres), almacenando información sobre su nombre, precio y categoría. Utiliza el método
   especial `__str__` para dar un formato limpio a la visualización de los productos.
   * **`Cliente`**: Modela a las personas que consumen en el establecimiento. Cada cliente posee
   una identificación única y una lista dinámica que gestiona su consumo actual (pedido), permitiendo
   calcular de forma automática el total de su cuenta.

2. **Servicios (`servicios/`)**:
   * **`Restaurante`**: Funciona como el controlador central del sistema. Se encarga de administrar
   el catálogo del menú y el registro de los comensales, centralizando los métodos necesarios para
   procesar la información y desplegarla de manera organizada en la consola.

3. **Punto de Arranque (`main.py`)**:
   * Archivo principal encargado de inicializar el entorno, instanciar los objetos correspondientes
   (productos y clientes), simular la toma de pedidos y ejecutar el flujo del programa mostrando los
   resultados estructurados en consola.

## Estructura del Proyecto

El código respeta estrictamente la siguiente arquitectura de carpetas y archivos:

```text
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
