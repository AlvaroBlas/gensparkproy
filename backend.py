"""
Backend del Sistema de Control de Gastos
Módulo que gestiona toda la lógica de negocio y persistencia de datos
"""

import csv
import os
from datetime import datetime
from typing import List, Dict, Tuple


class GestorGastos:
    """
    Clase encargada de gestionar los gastos del usuario.
    Maneja la persistencia en CSV y operaciones CRUD.
    """
    
    def __init__(self, archivo_csv: str = "gastos.csv"):
        """
        Inicializa el gestor de gastos.
        
        Args:
            archivo_csv: Nombre del archivo CSV donde se almacenarán los gastos
        """
        self.archivo_csv = archivo_csv
        self.columnas = ["fecha", "categoria", "descripcion", "monto"]
        self._inicializar_archivo()
    
    def _inicializar_archivo(self) -> None:
        """
        Crea el archivo CSV con encabezados si no existe.
        """
        if not os.path.exists(self.archivo_csv):
            try:
                with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
                    escritor = csv.DictWriter(archivo, fieldnames=self.columnas)
                    escritor.writeheader()
                print(f"✓ Archivo '{self.archivo_csv}' creado exitosamente")
            except Exception as e:
                raise Exception(f"Error al crear el archivo: {str(e)}")
    
    def guardar_gasto(self, categoria: str, descripcion: str, monto: float) -> Tuple[bool, str]:
        """
        Guarda un nuevo gasto en el archivo CSV.
        
        Args:
            categoria: Categoría del gasto (Ej: Comida, Transporte, etc.)
            descripcion: Descripción detallada del gasto
            monto: Cantidad monetaria del gasto
            
        Returns:
            Tupla (éxito: bool, mensaje: str)
        """
        # Validaciones
        if not categoria or not categoria.strip():
            return False, "La categoría no puede estar vacía"
        
        if not descripcion or not descripcion.strip():
            return False, "La descripción no puede estar vacía"
        
        try:
            monto_float = float(monto)
            if monto_float <= 0:
                return False, "El monto debe ser mayor a 0"
        except (ValueError, TypeError):
            return False, "El monto debe ser un número válido"
        
        # Guardar el gasto
        try:
            with open(self.archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=self.columnas)
                escritor.writerow({
                    'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'categoria': categoria.strip(),
                    'descripcion': descripcion.strip(),
                    'monto': f"{monto_float:.2f}"
                })
            return True, "Gasto guardado exitosamente"
        except Exception as e:
            return False, f"Error al guardar el gasto: {str(e)}"
    
    def obtener_gastos(self) -> List[Dict[str, str]]:
        """
        Lee y retorna todos los gastos del archivo CSV.
        
        Returns:
            Lista de diccionarios con los gastos
        """
        gastos = []
        try:
            if os.path.exists(self.archivo_csv):
                with open(self.archivo_csv, 'r', encoding='utf-8') as archivo:
                    lector = csv.DictReader(archivo)
                    gastos = list(lector)
        except Exception as e:
            print(f"Error al leer gastos: {str(e)}")
        
        return gastos
    
    def calcular_total(self) -> float:
        """
        Calcula el total de todos los gastos registrados.
        
        Returns:
            Suma total de los gastos
        """
        gastos = self.obtener_gastos()
        total = sum(float(gasto['monto']) for gasto in gastos if gasto.get('monto'))
        return total
    
    def calcular_total_por_categoria(self) -> Dict[str, float]:
        """
        Calcula el total de gastos agrupados por categoría.
        
        Returns:
            Diccionario con categorías y sus totales
        """
        gastos = self.obtener_gastos()
        totales = {}
        
        for gasto in gastos:
            categoria = gasto.get('categoria', 'Sin categoría')
            monto = float(gasto.get('monto', 0))
            totales[categoria] = totales.get(categoria, 0) + monto
        
        return totales
    
    def eliminar_gasto(self, indice: int) -> Tuple[bool, str]:
        """
        Elimina un gasto específico por su índice.
        
        Args:
            indice: Índice del gasto a eliminar (0-based)
            
        Returns:
            Tupla (éxito: bool, mensaje: str)
        """
        gastos = self.obtener_gastos()
        
        if indice < 0 or indice >= len(gastos):
            return False, "Índice inválido"
        
        try:
            gastos.pop(indice)
            
            # Reescribir el archivo sin el gasto eliminado
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=self.columnas)
                escritor.writeheader()
                escritor.writerows(gastos)
            
            return True, "Gasto eliminado exitosamente"
        except Exception as e:
            return False, f"Error al eliminar el gasto: {str(e)}"
    
    def obtener_estadisticas(self) -> Dict[str, any]:
        """
        Genera estadísticas generales de los gastos.
        
        Returns:
            Diccionario con estadísticas
        """
        gastos = self.obtener_gastos()
        
        if not gastos:
            return {
                'total_gastos': 0,
                'cantidad_gastos': 0,
                'promedio': 0,
                'gasto_mayor': 0,
                'gasto_menor': 0
            }
        
        montos = [float(g['monto']) for g in gastos]
        
        return {
            'total_gastos': sum(montos),
            'cantidad_gastos': len(gastos),
            'promedio': sum(montos) / len(montos),
            'gasto_mayor': max(montos),
            'gasto_menor': min(montos)
        }


# Código de prueba (solo se ejecuta si se corre este archivo directamente)
if __name__ == "__main__":
    print("=== Prueba del Backend ===\n")
    
    gestor = GestorGastos("gastos_prueba.csv")
    
    # Probar guardar gastos
    print("1. Guardando gastos de prueba...")
    gestor.guardar_gasto("Comida", "Almuerzo en restaurante", 25.50)
    gestor.guardar_gasto("Transporte", "Uber al trabajo", 12.75)
    gestor.guardar_gasto("Entretenimiento", "Cine", 15.00)
    
    # Obtener gastos
    print("\n2. Gastos registrados:")
    for i, gasto in enumerate(gestor.obtener_gastos(), 1):
        print(f"   {i}. {gasto['categoria']} - {gasto['descripcion']}: ${gasto['monto']}")
    
    # Calcular total
    print(f"\n3. Total gastado: ${gestor.calcular_total():.2f}")
    
    # Estadísticas
    print("\n4. Estadísticas:")
    stats = gestor.obtener_estadisticas()
    for clave, valor in stats.items():
        print(f"   {clave}: {valor}")
    
    print("\n✓ Pruebas completadas")
