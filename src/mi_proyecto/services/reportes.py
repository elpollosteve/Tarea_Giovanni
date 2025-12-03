"""
Modulo de Servicios - Reportes
Define la logica de generación de reportes y analisis
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from ..models.producto import Producto
from ..repositories.inventario import Inventario


class GeneradorReportes:
    """
    Genera reportes del inventario.
    Responsalbe de analisis y estadisticas.
    """
    
    def __init__(self, inventario: Inventario):
        """Inicializa el generador de reportes."""
        self.inventario = inventario
        
    def valor_total_inventario(self) -> float:
        """Calcula el total de items en stock."""
        productos = self.inventario.respositorio.obtener_todos()
        return sum(p.cantidad for p in productos)
    
    def cantidad_total_productos(self) -> int:
        """Cuenta la cantidad total de productos."""
        return len(self.inventario.repositorio.obtener_todos())
    
    def total_items_stock(self) -> int:
        """Calcula el total de items en stock."""
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.cantidad for p in productos)
    
    def producto_mas_caro(self) -> Optional[Producto]:
        """Obtiene el producto mas caro."""
        productos = self.inventario.repositorio.obtener_todos()
        return max(productos, key= lambda p: p.precio) if productos else None
    
    def producto_mas_barato(self) -> Optional[Producto]:
        """Obtiene el producto más barato."""
        productos = self.inventario._repositorio.obtener_todos()
        return min(productos, key=lambda p: p.precio) if productos else None

    def reporte_completo(self) -> Dict[str, Any]:
        """Genera reporte completo del inventario."""
        fecha_generacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_productos = self.cantidad_total_productos()
        total_items = self.total_items_stock()
        valor_total = self.valor_total_inventario()
        producto_mas_caro = self.producto_mas_caro()
        producto_mas_barato = self.producto_mas_barato()
        productos_bajo_stock = self.inventario.obtener_productos_bajo_stock()

        return {
            "fecha_generacion": fecha_generacion,
            "total_productos": total_productos,
            "total_items": total_items,
            "valor_total": valor_total,
            "producto_mas_caro": producto_mas_caro,
            "producto_mas_barato": producto_mas_barato,
            "productos_bajo_stock": productos_bajo_stock
        }