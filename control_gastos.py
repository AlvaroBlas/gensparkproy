#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Control de Gastos
Permite registrar gastos y mantener un historial persistente en CSV
"""

import csv
import os
from typing import List, Tuple


class ControlGastos:
    """Clase principal para gestionar el control de gastos"""
    
    def __init__(self, archivo_csv: str = 'gastos.csv'):
        """
        Inicializa el sistema de control de gastos
        
        Args:
            archivo_csv: Nombre del archivo CSV para almacenar los datos
        """
        self.archivo_csv = archivo_csv
        self.gastos: List[Tuple[str, float]] = []
        self._inicializar_archivo()
        self._cargar_gastos()
    
    def _inicializar_archivo(self):
        """Crea el archivo CSV con encabezados si no existe"""
        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['Nombre', 'Monto'])
            print(f"✓ Archivo '{self.archivo_csv}' creado correctamente\n")
    
    def _cargar_gastos(self):
        """Carga los gastos existentes desde el archivo CSV"""
        try:
            with open(self.archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                next(lector)  # Saltar encabezados
                
                for fila in lector:
                    if len(fila) == 2:
                        nombre = fila[0]
                        try:
                            monto = float(fila[1])
                            self.gastos.append((nombre, monto))
                        except ValueError:
                            print(f"⚠ Advertencia: Fila con monto inválido ignorada: {fila}")
        except FileNotFoundError:
            pass  # El archivo se creará en _inicializar_archivo
    
    def agregar_gasto(self, nombre: str, monto: float):
        """
        Agrega un nuevo gasto y lo guarda en el archivo CSV
        
        Args:
            nombre: Descripción del gasto
            monto: Cantidad gastada
        """
        if monto < 0:
            print("❌ Error: El monto no puede ser negativo")
            return
        
        # Agregar a la lista en memoria
        self.gastos.append((nombre, monto))
        
        # Guardar en el archivo CSV
        with open(self.archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, monto])
        
        print(f"✓ Gasto registrado: {nombre} - ${monto:.2f}\n")
    
    def calcular_total(self) -> float:
        """
        Calcula el total de todos los gastos
        
        Returns:
            Total acumulado de gastos
        """
        return sum(monto for _, monto in self.gastos)
    
    def mostrar_total(self):
        """Muestra el total de gastos con formato"""
        total = self.calcular_total()
        print("=" * 50)
        print(f"📊 RESUMEN DE GASTOS")
        print("=" * 50)
        print(f"Cantidad de gastos registrados: {len(self.gastos)}")
        print(f"Total gastado: ${total:.2f}")
        print("=" * 50 + "\n")
        
        if self.gastos:
            print("Últimos 5 gastos:")
            for nombre, monto in self.gastos[-5:]:
                print(f"  • {nombre}: ${monto:.2f}")
            print()


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("💰 SISTEMA DE CONTROL DE GASTOS")
    print("=" * 50)
    print("1) Ingresar un gasto")
    print("2) Ver total gastado")
    print("3) Salir")
    print("=" * 50)


def obtener_opcion() -> str:
    """
    Solicita y valida la opción del usuario
    
    Returns:
        Opción seleccionada como string
    """
    while True:
        opcion = input("Selecciona una opción (1-3): ").strip()
        if opcion in ['1', '2', '3']:
            return opcion
        print("❌ Opción inválida. Por favor, elige 1, 2 o 3.\n")


def ingresar_gasto(sistema: ControlGastos):
    """
    Solicita los datos de un gasto al usuario y lo registra
    
    Args:
        sistema: Instancia del sistema de control de gastos
    """
    print("\n--- INGRESAR NUEVO GASTO ---")
    
    # Solicitar nombre del gasto
    while True:
        nombre = input("Nombre del gasto: ").strip()
        if nombre:
            break
        print("❌ El nombre no puede estar vacío\n")
    
    # Solicitar monto
    while True:
        try:
            monto_str = input("Monto del gasto ($): ").strip()
            monto = float(monto_str)
            if monto >= 0:
                break
            print("❌ El monto debe ser un número positivo\n")
        except ValueError:
            print("❌ Por favor, ingresa un número válido\n")
    
    # Registrar el gasto
    sistema.agregar_gasto(nombre, monto)


def main():
    """Función principal del programa"""
    print("\n🚀 Iniciando Sistema de Control de Gastos...")
    
    # Crear instancia del sistema
    sistema = ControlGastos()
    
    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == '1':
            ingresar_gasto(sistema)
        
        elif opcion == '2':
            sistema.mostrar_total()
        
        elif opcion == '3':
            print("\n👋 ¡Gracias por usar el Sistema de Control de Gastos!")
            print(f"📁 Tus datos están guardados en: {sistema.archivo_csv}")
            print("Hasta pronto.\n")
            break


if __name__ == "__main__":
    main()
