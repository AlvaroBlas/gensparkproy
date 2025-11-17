# 💰 Sistema de Control de Gastos

Sistema simple y eficiente para llevar un registro de gastos personales con persistencia en archivo CSV.

## 📋 Características

- ✅ **Interfaz intuitiva**: Menú interactivo por consola
- 💾 **Persistencia de datos**: Los gastos se guardan en `gastos.csv`
- 📊 **Resumen de gastos**: Visualiza el total y últimos registros
- 🛡️ **Validación de datos**: Verifica entradas inválidas
- 🔄 **Sin pérdida de información**: Los datos persisten entre ejecuciones

## 🚀 Uso

### Ejecutar el programa

```bash
python control_gastos.py
```

### Opciones del menú

1. **Ingresar un gasto**: Registra un nuevo gasto con nombre y monto
2. **Ver total gastado**: Muestra el total acumulado y últimos gastos
3. **Salir**: Cierra el programa (los datos quedan guardados)

## 📂 Estructura del archivo CSV

El sistema genera automáticamente un archivo `gastos.csv` con la siguiente estructura:

```csv
Nombre,Monto
Supermercado,45.50
Gasolina,30.00
Restaurante,25.75
```

## 🏗️ Arquitectura del Código

### Clase Principal: `ControlGastos`

```python
class ControlGastos:
    - __init__(): Inicializa el sistema y carga datos existentes
    - _inicializar_archivo(): Crea el CSV si no existe
    - _cargar_gastos(): Lee gastos existentes al iniciar
    - agregar_gasto(): Registra un nuevo gasto
    - calcular_total(): Suma todos los gastos
    - mostrar_total(): Muestra resumen formateado
```

### Funciones Principales

- `mostrar_menu()`: Despliega las opciones disponibles
- `obtener_opcion()`: Valida la selección del usuario
- `ingresar_gasto()`: Interfaz para registrar gastos
- `main()`: Bucle principal del programa

## 💡 Ejemplo de Uso

```
💰 SISTEMA DE CONTROL DE GASTOS
==================================================
1) Ingresar un gasto
2) Ver total gastado
3) Salir
==================================================
Selecciona una opción (1-3): 1

--- INGRESAR NUEVO GASTO ---
Nombre del gasto: Supermercado
Monto del gasto ($): 45.50
✓ Gasto registrado: Supermercado - $45.50

Selecciona una opción (1-3): 2

==================================================
📊 RESUMEN DE GASTOS
==================================================
Cantidad de gastos registrados: 1
Total gastado: $45.50
==================================================

Últimos 5 gastos:
  • Supermercado: $45.50
```

## 🔒 Validaciones Implementadas

- ✅ Nombres de gasto no vacíos
- ✅ Montos numéricos válidos
- ✅ Montos no negativos
- ✅ Opciones de menú válidas (1-3)
- ✅ Manejo de archivos CSV corruptos

## 🛠️ Requisitos

- Python 3.6 o superior
- Librería estándar `csv` (incluida en Python)

## 📝 Notas Técnicas

- **Encoding**: UTF-8 para soportar caracteres especiales
- **Separador CSV**: Coma (,)
- **Precisión decimal**: 2 decimales para montos
- **Manejo de errores**: Validación robusta de entradas

## 🔧 Personalización

Puedes cambiar el nombre del archivo CSV al crear la instancia:

```python
sistema = ControlGastos(archivo_csv='mis_gastos.csv')
```

## 📄 Licencia

Código libre para uso educativo y personal.
