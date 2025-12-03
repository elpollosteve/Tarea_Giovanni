"""
Módulo de Modelos - Producto
Define las entidades principales del sistema
"""
from datetime import datetime
from enum import Enum

class Categoria(Enum):
    """Enumeración de categorías de productos."""
    ELECTRONICA = "Electrónica"
    ALIMENTOS = "Alimentos"
    ROPA = "Ropa"
    LIBROS = "Libros"
    OTROS = "Otros"


class Producto:
    """Representa un producto en el inventario.

    Atributos:
        id_producto (int): Identificador único
        nombre (str): Nombre del producto
        descripcion (str): Descripción del producto
        precio (float): Precio unitario
        cantidad (int): Cantidad en stock
        categoria (Categoria): Categoría del producto
        fecha_creacion (str): Fecha de creación
    """
    _contador = 1000

    def __init__(self, nombre: str, descripcion: str, precio: float,
                 cantidad: int, categoria: Categoria):
        """Inicializa un producto.

        Args:
            nombre (str): Nombre del producto
            descripcion (str): Descripción del producto
            precio (float): Precio unitario
            cantidad (int): Cantidad en stock
            categoria (Categoria): Categoría del producto
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        Producto._contador += 1
        self.id_producto = Producto._contador
        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def actualizar_cantidad(self, cantidad: int) -> bool:
        """Actualiza la cantidad de producto."""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = cantidad
        return True

    def actualizar_precio(self, precio: float) -> bool:
        """Actualiza el precio del producto."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio
        return True

    def calcular_valor_total(self) -> float:
        """Calcula el valor total del producto en stock."""
        return self.precio * self.cantidad

    def __str__(self) -> str:
        """Representación string del producto."""
        return f"{self.id_producto} | {self.nombre} | {self.precio} | {self.cantidad}"

    def __repr__(self) -> str:
        """Representación técnica del producto."""
        return f"Producto(id={self.id_producto}, nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"