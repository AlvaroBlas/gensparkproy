# 💰 SISTEMA DE CONTROL DE GASTOS - RESUMEN DEL PROYECTO

---

## 📦 CONTENIDO DEL PAQUETE

### **Archivos Principales (Obligatorios)**
1. **`backend.py`** (7.1 KB)
   - Clase `GestorGastos` con toda la lógica de negocio
   - Gestión de persistencia en CSV
   - Validaciones y cálculos

2. **`main.py`** (15 KB)
   - Interfaz gráfica Tkinter completa
   - Formularios, tablas y estadísticas
   - Importa y usa `backend.py`

### **Archivos Opcionales (Útiles)**
3. **`README.md`** - Documentación completa
4. **`INSTRUCCIONES_RAPIDAS.txt`** - Guía rápida de uso
5. **`demo_visual.py`** - Script para crear datos de ejemplo
6. **`ejecutar.sh`** - Script de lanzamiento (Linux/Mac)
7. **`gastos.csv`** - Archivo de datos (se genera automáticamente)

---

## 🚀 EJECUCIÓN RÁPIDA (2 COMANDOS)

### Windows (CMD/PowerShell)
```cmd
cd ruta\a\la\carpeta
python main.py
```

### Linux/Mac (Terminal)
```bash
cd /ruta/a/la/carpeta
python3 main.py
```

**IMPORTANTE:** `backend.py` y `main.py` deben estar en la **misma carpeta**.

---

## 🏗️ ARQUITECTURA DEL SISTEMA

```
┌─────────────────────────────────────────────────────────┐
│                      MAIN.PY                            │
│              (Interfaz Gráfica - Vista)                 │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Formulario  │  │    Tabla     │  │ Estadísticas │ │
│  │  de Entrada  │  │ Interactiva  │  │   en Vivo    │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│           │                │                 │          │
│           └────────────────┴─────────────────┘          │
│                          │                               │
│                          ▼                               │
│                   import backend                         │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    BACKEND.PY                            │
│           (Lógica de Negocio - Modelo)                  │
│                                                          │
│              Clase: GestorGastos                        │
│  ┌────────────────────────────────────────────────┐    │
│  │  • guardar_gasto()                             │    │
│  │  • obtener_gastos()                            │    │
│  │  • calcular_total()                            │    │
│  │  • calcular_total_por_categoria()              │    │
│  │  • eliminar_gasto()                            │    │
│  │  • obtener_estadisticas()                      │    │
│  └────────────────────────────────────────────────┘    │
│                          │                               │
│                          ▼                               │
│                    gastos.csv                            │
│              (Persistencia de Datos)                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🔑 FUNCIONALIDADES CLAVE

### Backend (`backend.py`)

#### **Métodos Principales:**

```python
gestor = GestorGastos()

# 1. Guardar gasto
exito, mensaje = gestor.guardar_gasto(
    categoria="Comida",
    descripcion="Almuerzo",
    monto=25.50
)

# 2. Obtener todos los gastos
gastos = gestor.obtener_gastos()
# Retorna: [{'fecha': '...', 'categoria': '...', 'descripcion': '...', 'monto': '...'}]

# 3. Calcular total general
total = gestor.calcular_total()
# Retorna: 376.34

# 4. Totales por categoría
totales = gestor.calcular_total_por_categoria()
# Retorna: {'Comida': 135.80, 'Transporte': 85.75, ...}

# 5. Estadísticas completas
stats = gestor.obtener_estadisticas()
# Retorna: {'total_gastos': 376.34, 'cantidad_gastos': 12, ...}

# 6. Eliminar gasto
exito, mensaje = gestor.eliminar_gasto(indice=0)
```

#### **Validaciones Automáticas:**
✅ Categoría no vacía  
✅ Descripción no vacía  
✅ Monto numérico válido  
✅ Monto mayor a 0  
✅ Manejo robusto de errores  

---

### Frontend (`main.py`)

#### **Componentes Visuales:**

1. **Panel de Registro**
   - ComboBox con 8 categorías predefinidas
   - Campo de descripción
   - Campo de monto numérico
   - Botón "Guardar Gasto"
   - Atajo de teclado: Enter

2. **Panel de Estadísticas**
   - Total gastado (actualización en tiempo real)
   - Cantidad de gastos
   - Promedio de gastos

3. **Tabla Interactiva**
   - Columnas: Fecha, Categoría, Descripción, Monto
   - Scrollbars vertical y horizontal
   - Ordenable por columnas
   - Doble clic para eliminar

4. **Botones de Acción**
   - 🔄 Actualizar
   - 🗑️ Eliminar Seleccionado
   - 🧹 Limpiar Campos

---

## 📊 FORMATO DE DATOS (CSV)

```csv
fecha,categoria,descripcion,monto
2025-11-17 14:30:45,Comida,Desayuno en cafetería,8.50
2025-11-17 15:20:10,Transporte,Gasolina,45.00
2025-11-17 18:45:30,Entretenimiento,Netflix mensual,12.99
```

**Codificación:** UTF-8  
**Separador:** Coma (`,`)  
**Formato de fecha:** `YYYY-MM-DD HH:MM:SS`  

---

## 🎯 VENTAJAS DE LA ARQUITECTURA MODULAR

### ✅ **Separación de Responsabilidades**
- **Backend:** Solo lógica y datos
- **Frontend:** Solo interfaz y presentación

### ✅ **Reutilización del Backend**
Puedes usar `backend.py` en:
- Scripts de consola (CLI)
- APIs REST (Flask/FastAPI)
- Aplicaciones web (Django)
- Notebooks Jupyter
- Otros proyectos Python

### ✅ **Mantenibilidad**
- Cambios en UI → Solo editar `main.py`
- Cambios en lógica → Solo editar `backend.py`

### ✅ **Escalabilidad**
Migrar de CSV a SQLite:
```python
# Solo modificas backend.py
# main.py no necesita cambios
class GestorGastos:
    def __init__(self):
        self.conn = sqlite3.connect('gastos.db')
        # Resto del código...
```

### ✅ **Testabilidad**
```python
# Pruebas unitarias fáciles
def test_guardar_gasto():
    gestor = GestorGastos("test.csv")
    exito, _ = gestor.guardar_gasto("Comida", "Test", 10.0)
    assert exito == True
```

---

## 🧪 PROBAR EL SISTEMA

### **Opción 1: Datos Manuales**
1. Ejecuta `python3 main.py`
2. Ingresa gastos manualmente

### **Opción 2: Datos de Demostración**
```bash
# Crear 12 gastos de ejemplo
python3 demo_visual.py

# Luego abrir la interfaz
python3 main.py
```

### **Opción 3: Probar Solo el Backend**
```bash
python3 backend.py
# Ejecuta pruebas automáticas
```

---

## 📚 EJEMPLOS DE USO DEL BACKEND

### **Ejemplo 1: Script Simple**
```python
from backend import GestorGastos

gestor = GestorGastos()
gestor.guardar_gasto("Comida", "Pizza", 18.50)
print(f"Total: ${gestor.calcular_total():.2f}")
```

### **Ejemplo 2: Análisis de Gastos**
```python
from backend import GestorGastos

gestor = GestorGastos()
totales = gestor.calcular_total_por_categoria()

print("Análisis por categoría:")
for cat, total in totales.items():
    print(f"{cat}: ${total:.2f}")
```

### **Ejemplo 3: Reporte Mensual**
```python
from backend import GestorGastos

gestor = GestorGastos()
stats = gestor.obtener_estadisticas()

print(f"""
REPORTE MENSUAL
===============
Total gastado: ${stats['total_gastos']:.2f}
Promedio diario: ${stats['promedio']:.2f}
Gasto mayor: ${stats['gasto_mayor']:.2f}
""")
```

---

## 🛠️ PERSONALIZACIÓN

### **Agregar Nuevas Categorías**
Edita `main.py`, línea ~250:
```python
categorias = ["Comida", "Transporte", "TU_CATEGORIA"]
```

### **Cambiar Colores**
Edita `main.py`, método `_configurar_estilos()`:
```python
style.configure("Treeview.Heading",
               background="#TU_COLOR")
```

### **Agregar Validaciones**
Edita `backend.py`, método `guardar_gasto()`:
```python
if monto_float > 1000:
    return False, "Monto muy alto, verifica"
```

---

## 🔐 SEGURIDAD Y PRIVACIDAD

- ✅ Todos los datos se guardan **localmente**
- ✅ No hay conexiones a internet
- ✅ No se recopila información personal
- ✅ Archivo CSV protegido por permisos del SO

---

## 🚀 PRÓXIMOS PASOS SUGERIDOS

### **Nivel Principiante**
1. Cambiar los colores de la interfaz
2. Agregar más categorías
3. Modificar el tamaño de la ventana

### **Nivel Intermedio**
4. Agregar filtros por fecha
5. Implementar búsqueda de gastos
6. Exportar a Excel

### **Nivel Avanzado**
7. Migrar a base de datos SQLite
8. Crear gráficos con matplotlib
9. Implementar presupuestos mensuales
10. Agregar autenticación de usuario

---

## 📖 RECURSOS ADICIONALES

### **Documentación Python**
- Tkinter: https://docs.python.org/3/library/tkinter.html
- CSV: https://docs.python.org/3/library/csv.html

### **Tutoriales Recomendados**
- Real Python Tkinter: https://realpython.com/python-gui-tkinter/
- Arquitectura MVC en Python

---

## 🐛 TROUBLESHOOTING

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: backend` | Ejecuta desde la carpeta correcta |
| `ModuleNotFoundError: tkinter` | `sudo apt-get install python3-tk` |
| Ventana no aparece | Verifica entorno gráfico activo |
| CSV corrupto | Elimina `gastos.csv` y reinicia |
| Caracteres raros en CSV | Abre con editor UTF-8 |

---

## 📞 SOPORTE

Este es un proyecto educativo de código abierto.  
Siéntete libre de modificarlo y mejorarlo según tus necesidades.

---

## ✨ CARACTERÍSTICAS DESTACADAS

- ✅ **100% Python puro** (sin dependencias externas)
- ✅ **Arquitectura modular profesional**
- ✅ **Interfaz gráfica intuitiva**
- ✅ **Código bien documentado**
- ✅ **Manejo robusto de errores**
- ✅ **Validaciones exhaustivas**
- ✅ **Estadísticas en tiempo real**
- ✅ **Fácil de extender y mantener**

---

## 📄 LICENCIA

Proyecto de código abierto para fines educativos y personales.  
Siéntete libre de usar, modificar y compartir.

---

**Desarrollado siguiendo principios SOLID y mejores prácticas de Python** 🐍

**¡Disfruta gestionando tus gastos de manera profesional! 💰📊**
