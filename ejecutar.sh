#!/bin/bash
# Script para ejecutar el Sistema de Control de Gastos

cd "$(dirname "$0")"

echo "🚀 Iniciando Sistema de Control de Gastos..."
echo "----------------------------------------"
echo ""

# Verificar que Python esté instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    exit 1
fi

echo "✓ Python detectado: $(python3 --version)"
echo ""
echo "📂 Directorio actual: $(pwd)"
echo ""
echo "🎨 Lanzando interfaz gráfica..."
echo ""

# Ejecutar la aplicación
python3 main.py
