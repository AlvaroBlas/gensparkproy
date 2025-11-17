"""
Script de demostración visual del sistema
Crea gastos de ejemplo para mostrar el sistema en acción
"""

from backend import GestorGastos
import time

def crear_datos_demo():
    """Crea datos de demostración en gastos.csv"""
    print("🎬 Creando datos de demostración...")
    print("=" * 60)
    
    gestor = GestorGastos("gastos.csv")
    
    # Datos de ejemplo realistas
    gastos_demo = [
        ("Comida", "Desayuno en cafetería", 8.50),
        ("Transporte", "Gasolina", 45.00),
        ("Entretenimiento", "Netflix mensual", 12.99),
        ("Salud", "Farmacia - Vitaminas", 22.50),
        ("Comida", "Supermercado semanal", 85.30),
        ("Transporte", "Uber al aeropuerto", 28.75),
        ("Educación", "Libro de Python", 35.00),
        ("Hogar", "Bombillas LED", 15.80),
        ("Comida", "Cena restaurante", 42.00),
        ("Servicios", "Internet mensual", 50.00),
        ("Entretenimiento", "Cine con palomitas", 18.50),
        ("Transporte", "Estacionamiento", 12.00),
    ]
    
    print("\n📝 Registrando gastos de ejemplo:\n")
    
    for i, (categoria, descripcion, monto) in enumerate(gastos_demo, 1):
        exito, mensaje = gestor.guardar_gasto(categoria, descripcion, monto)
        if exito:
            print(f"✓ {i:2d}. [{categoria:15s}] {descripcion:30s} ${monto:6.2f}")
        else:
            print(f"✗ {i:2d}. Error: {mensaje}")
        time.sleep(0.1)  # Pequeña pausa para efecto visual
    
    print("\n" + "=" * 60)
    print("\n📊 ESTADÍSTICAS GENERADAS:\n")
    
    stats = gestor.obtener_estadisticas()
    print(f"   💰 Total gastado:     ${stats['total_gastos']:8.2f}")
    print(f"   📝 Número de gastos:  {stats['cantidad_gastos']:8d}")
    print(f"   📊 Promedio:          ${stats['promedio']:8.2f}")
    print(f"   ⬆️  Gasto mayor:       ${stats['gasto_mayor']:8.2f}")
    print(f"   ⬇️  Gasto menor:       ${stats['gasto_menor']:8.2f}")
    
    print("\n📁 TOTALES POR CATEGORÍA:\n")
    totales_cat = gestor.calcular_total_por_categoria()
    for categoria, total in sorted(totales_cat.items(), key=lambda x: x[1], reverse=True):
        porcentaje = (total / stats['total_gastos']) * 100
        barra = "█" * int(porcentaje / 2)
        print(f"   {categoria:15s} ${total:7.2f}  {barra} {porcentaje:.1f}%")
    
    print("\n" + "=" * 60)
    print("\n✅ ¡Datos de demostración creados exitosamente!")
    print("\n🚀 Ahora ejecuta: python3 main.py")
    print("   para ver los gastos en la interfaz gráfica\n")

if __name__ == "__main__":
    crear_datos_demo()
