# 💰 Sistema de Control de Gastos Modular

Sistema completo de gestión de gastos personales con interfaz gráfica desarrollado en Python usando arquitectura modular.

---

## 📋 Características

### Backend (`backend.py`)
- ✅ Gestión completa de persistencia en CSV
- 💾 Creación automática de base de datos
- 🔒 Validaciones de datos
- 📊 Cálculo de estadísticas avanzadas
- 🗑️ Sistema CRUD completo

### Frontend (`main.py`)
- 🎨 Interfaz gráfica moderna con Tkinter
- 📝 Formulario intuitivo con categorías predefinidas
- 📊 Panel de estadísticas en tiempo real
- 📋 Tabla interactiva ordenable
- 🖱️ Eliminación con doble clic y confirmación

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.7 o superior
- Tkinter (incluido por defecto en Python)

### Método 1: Ejecución Directa (Recomendado)

**Windows:**
```cmd
python main.py
```

**Linux/Mac:**
```bash
python3 main.py
```

### Método 2: Script de Ejecución (Linux/Mac)

```bash
chmod +x ejecutar.sh
./ejecutar.sh
```

---

## 📁 Estructura del Proyecto

```
sistema_gastos/
│
├── backend.py          # Lógica de negocio y persistencia
├── main.py            # Interfaz gráfica Tkinter
├── ejecutar.sh        # Script de lanzamiento (opcional)
├── README.md          # Documentación
└── gastos.csv         # Base de datos (se crea automáticamente)
```

---

## 🎯 Uso del Sistema

### 1. Registrar un Gasto
1. Selecciona una **categoría** del menú desplegable
2. Escribe una **descripción** del gasto
3. Ingresa el **monto** (solo números)
4. Haz clic en **"💾 Guardar Gasto"** o presiona **Enter**

### 2. Ver Historial
- Todos los gastos se muestran automáticamente en la tabla
- Las estadísticas se actualizan en tiempo real

### 3. Eliminar un Gasto
- **Opción 1:** Haz doble clic sobre el gasto en la tabla
- **Opción 2:** Selecciona el gasto y haz clic en **"🗑️ Eliminar Seleccionado"**
- Confirma la eliminación en el diálogo

### 4. Otras Acciones
- **🔄 Actualizar:** Refresca la tabla y estadísticas
- **🧹 Limpiar Campos:** Borra el formulario

---

## 🔧 Arquitectura Modular

### Separación de Responsabilidades

**Backend (Modelo):**
```python
from backend import GestorGastos

gestor = GestorGastos()
gestor.guardar_gasto("Comida", "Almuerzo", 25.50)
gastos = gestor.obtener_gastos()
total = gestor.calcular_total()
```

**Frontend (Vista/Controlador):**
```python
# Usa el backend sin conocer detalles de implementación
self.gestor = GestorGastos()
exito, mensaje = self.gestor.guardar_gasto(...)
```

### Ventajas de esta Arquitectura
- ✅ **Mantenibilidad:** Código organizado y fácil de modificar
- ✅ **Escalabilidad:** Puedes cambiar el backend (CSV → SQLite) sin tocar la UI
- ✅ **Testabilidad:** Backend puede probarse independientemente
- ✅ **Reutilización:** Backend puede usarse en CLI, API o web

---

## 📊 Funcionalidades Avanzadas del Backend

### Estadísticas Disponibles
```python
stats = gestor.obtener_estadisticas()
# Retorna:
# {
#     'total_gastos': 150.75,
#     'cantidad_gastos': 8,
#     'promedio': 18.84,
#     'gasto_mayor': 50.00,
#     'gasto_menor': 5.25
# }
```

### Totales por Categoría
```python
totales = gestor.calcular_total_por_categoria()
# Retorna:
# {
#     'Comida': 85.50,
#     'Transporte': 45.25,
#     'Entretenimiento': 20.00
# }
```

---

## 🧪 Pruebas del Backend

Para probar el backend de forma independiente:

```bash
python3 backend.py
```

Esto ejecuta pruebas automáticas que crean gastos de ejemplo y muestran las funcionalidades.

---

## 🎨 Categorías Predefinidas

- 🍔 Comida
- 🚗 Transporte
- 🎬 Entretenimiento
- 💊 Salud
- 📚 Educación
- 🔌 Servicios
- 🏠 Hogar
- 📦 Otros

---

## 📝 Formato del Archivo CSV

```csv
fecha,categoria,descripcion,monto
2025-11-17 14:30:45,Comida,Almuerzo en restaurante,25.50
2025-11-17 18:20:10,Transporte,Uber,12.75
```

---

## 🔐 Validaciones Implementadas

- ❌ No permite campos vacíos
- ❌ No permite montos negativos o cero
- ❌ Valida formato numérico del monto
- ✅ Manejo robusto de errores con mensajes claros

---

## 🚀 Extensiones Futuras Sugeridas

1. **Filtros por fecha y categoría**
2. **Exportación a Excel/PDF**
3. **Gráficos de torta y barras**
4. **Presupuesto mensual con alertas**
5. **Modo oscuro**
6. **Multi-usuario con contraseñas**
7. **Respaldo automático en la nube**
8. **Aplicación móvil complementaria**

---

## 📄 Licencia

Este proyecto es de código abierto y puede ser usado libremente con fines educativos y personales.

---

## 👨‍💻 Desarrollado por

Sistema diseñado siguiendo principios SOLID y mejores prácticas de arquitectura de software.

**¿Preguntas o sugerencias?** ¡Contribuciones bienvenidas!

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'backend'"
**Solución:** Asegúrate de ejecutar `main.py` desde el mismo directorio donde está `backend.py`

### Error: Tkinter no disponible
**Solución en Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

### La ventana no se muestra
**Solución:** Verifica que tengas un entorno gráfico activo (no funciona en SSH sin X11)

---

**¡Disfruta gestionando tus gastos! 💰📊**
