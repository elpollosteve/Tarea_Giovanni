"""
Módulo de Utilidades - Formateadores
Define funciones para formatear y presentar datos
"""
from typing import List, Dict, Any
from ..models.producto import Producto


class Formateadores:
    """Clase con métodos estáticos para formatear datos."""

    @staticmethod
    def formatear_precio(precio: float) -> str:
        """Formatea precio con símbolo de moneda."""
        return f"S/.{precio:.2f}"

    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        """Formatea producto para visualización en tabla."""
        return f"| {producto.id_producto:>6} | {producto.nombre:<28} | {Formateadores.formatear_precio(producto.precio):>10} | {producto.cantidad:>6} | {producto.calcular_valor_total():>10.2f} |"

    @staticmethod
    def formatear_lista_productos(productos: List[Producto]) -> str:
        """Formatea lista de productos para visualización."""
        if not productos:
            return "No hay productos para mostrar"

        encabezado = "| ID     | Nombre                       | Precio     | Stock  | Valor Total |"
        separador = "-" * 80
        filas = [Formateadores.formatear_producto_tabla(p) for p in productos]
        return f"{encabezado}\n{separador}\n" + "\n".join(filas) + f"\n{separador}"

    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        """Formatea reporte para visualización."""
        output = "\n" + "=" * 60 + "\n"
        output += "                REPORTE DE INVENTARIO\n"
        output += "=" * 60 + "\n"
        output += f"Fecha de Generación: {reporte['fecha_generacion']}\n"
        output += f"Total de Productos: {reporte['total_productos']}\n"
        output += f"Total Ítems en Stock: {reporte['total_items']}\n"
        output += f"Valor Total del Inventario: {Formateadores.formatear_precio(reporte['valor_total'])}\n\n"

        if reporte['producto_mas_caro']:
            output += f"Producto Más Caro: {reporte['producto_mas_caro'].nombre} - {Formateadores.formatear_precio(reporte['producto_mas_caro'].precio)}\n"
        if reporte['producto_mas_barato']:
            output += f"Producto Más Barato: {reporte['producto_mas_barato'].nombre} - {Formateadores.formatear_precio(reporte['producto_mas_barato'].precio)}\n"

        output += "\nProductos Bajo Stock: (Límite: 10)\n"
        output += "-" * 60 + "\n"
        if reporte['productos_bajo_stock']:
            for p in reporte['productos_bajo_stock']:
                output += f"{p.id_producto} | {p.nombre} | Stock: {p.cantidad}\n"
        else:
            output += "   No hay productos con bajo stock.\n"
        output += "=" * 60 + "\n"
        return output