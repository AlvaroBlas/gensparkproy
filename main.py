"""
Interfaz Gráfica del Sistema de Control de Gastos
Aplicación de escritorio usando Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
from backend import GestorGastos
from typing import Optional


class AplicacionGastos:
    """
    Clase principal de la interfaz gráfica del sistema de gastos.
    """
    
    def __init__(self, root: tk.Tk):
        """
        Inicializa la aplicación gráfica.
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.gestor = GestorGastos()
        
        # Configuración de la ventana principal
        self.root.title("💰 Sistema de Control de Gastos")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configurar estilos
        self._configurar_estilos()
        
        # Construir la interfaz
        self._construir_interfaz()
        
        # Cargar datos iniciales
        self.actualizar_tabla()
        self.actualizar_estadisticas()
    
    def _configurar_estilos(self) -> None:
        """
        Configura los estilos y colores de la aplicación.
        """
        self.root.configure(bg='#f0f0f0')
        
        # Estilo para Treeview
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("Treeview",
                       background="#ffffff",
                       foreground="#000000",
                       rowheight=30,
                       fieldbackground="#ffffff",
                       font=('Arial', 10))
        
        style.map('Treeview', background=[('selected', '#0078d7')])
        
        style.configure("Treeview.Heading",
                       font=('Arial', 11, 'bold'),
                       background="#0078d7",
                       foreground="#ffffff")
    
    def _construir_interfaz(self) -> None:
        """
        Construye todos los elementos de la interfaz gráfica.
        """
        # Frame principal con padding
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo_font = font.Font(family='Arial', size=18, weight='bold')
        titulo = tk.Label(main_frame, 
                         text="💰 Control de Gastos Personales",
                         font=titulo_font,
                         bg='#f0f0f0',
                         fg='#0078d7')
        titulo.pack(pady=(0, 20))
        
        # Frame de entrada de datos
        self._crear_frame_entrada(main_frame)
        
        # Frame de estadísticas
        self._crear_frame_estadisticas(main_frame)
        
        # Frame de la tabla
        self._crear_frame_tabla(main_frame)
        
        # Frame de botones de acción
        self._crear_frame_acciones(main_frame)
    
    def _crear_frame_entrada(self, parent: tk.Frame) -> None:
        """
        Crea el frame para ingresar nuevos gastos.
        """
        frame = tk.LabelFrame(parent,
                             text="📝 Registrar Nuevo Gasto",
                             font=('Arial', 12, 'bold'),
                             bg='#ffffff',
                             padx=15,
                             pady=15)
        frame.pack(fill=tk.X, pady=(0, 15))
        
        # Grid para organizar los campos
        # Categoría
        tk.Label(frame, text="Categoría:", bg='#ffffff', font=('Arial', 10)).grid(
            row=0, column=0, sticky='e', padx=(0, 10), pady=5)
        
        self.categoria_var = tk.StringVar()
        categorias = ["Comida", "Transporte", "Entretenimiento", "Salud", 
                     "Educación", "Servicios", "Hogar", "Otros"]
        self.combo_categoria = ttk.Combobox(frame,
                                           textvariable=self.categoria_var,
                                           values=categorias,
                                           state='readonly',
                                           width=30,
                                           font=('Arial', 10))
        self.combo_categoria.grid(row=0, column=1, sticky='ew', pady=5)
        self.combo_categoria.current(0)
        
        # Descripción
        tk.Label(frame, text="Descripción:", bg='#ffffff', font=('Arial', 10)).grid(
            row=1, column=0, sticky='e', padx=(0, 10), pady=5)
        
        self.descripcion_entry = tk.Entry(frame, width=30, font=('Arial', 10))
        self.descripcion_entry.grid(row=1, column=1, sticky='ew', pady=5)
        
        # Monto
        tk.Label(frame, text="Monto ($):", bg='#ffffff', font=('Arial', 10)).grid(
            row=2, column=0, sticky='e', padx=(0, 10), pady=5)
        
        self.monto_entry = tk.Entry(frame, width=30, font=('Arial', 10))
        self.monto_entry.grid(row=2, column=1, sticky='ew', pady=5)
        
        # Botón de guardar
        btn_guardar = tk.Button(frame,
                               text="💾 Guardar Gasto",
                               command=self.guardar_gasto,
                               bg='#0078d7',
                               fg='white',
                               font=('Arial', 11, 'bold'),
                               padx=20,
                               pady=8,
                               cursor='hand2',
                               relief=tk.RAISED)
        btn_guardar.grid(row=3, column=0, columnspan=2, pady=(15, 5))
        
        # Configurar expansión de columnas
        frame.columnconfigure(1, weight=1)
        
        # Bind Enter key para guardar
        self.monto_entry.bind('<Return>', lambda e: self.guardar_gasto())
    
    def _crear_frame_estadisticas(self, parent: tk.Frame) -> None:
        """
        Crea el frame para mostrar estadísticas.
        """
        frame = tk.LabelFrame(parent,
                             text="📊 Estadísticas",
                             font=('Arial', 12, 'bold'),
                             bg='#ffffff',
                             padx=15,
                             pady=15)
        frame.pack(fill=tk.X, pady=(0, 15))
        
        # Grid para estadísticas
        stats_frame = tk.Frame(frame, bg='#ffffff')
        stats_frame.pack(fill=tk.X)
        
        # Labels para estadísticas
        self.label_total = tk.Label(stats_frame,
                                   text="Total Gastado: $0.00",
                                   bg='#ffffff',
                                   font=('Arial', 12, 'bold'),
                                   fg='#d32f2f')
        self.label_total.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        
        self.label_cantidad = tk.Label(stats_frame,
                                      text="Cantidad de Gastos: 0",
                                      bg='#ffffff',
                                      font=('Arial', 10))
        self.label_cantidad.grid(row=0, column=1, sticky='w', padx=10, pady=5)
        
        self.label_promedio = tk.Label(stats_frame,
                                      text="Promedio: $0.00",
                                      bg='#ffffff',
                                      font=('Arial', 10))
        self.label_promedio.grid(row=0, column=2, sticky='w', padx=10, pady=5)
        
        # Configurar expansión
        stats_frame.columnconfigure(0, weight=1)
        stats_frame.columnconfigure(1, weight=1)
        stats_frame.columnconfigure(2, weight=1)
    
    def _crear_frame_tabla(self, parent: tk.Frame) -> None:
        """
        Crea el frame con la tabla de gastos.
        """
        frame = tk.LabelFrame(parent,
                             text="📋 Historial de Gastos",
                             font=('Arial', 12, 'bold'),
                             bg='#ffffff',
                             padx=10,
                             pady=10)
        frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Crear Treeview con scrollbar
        tree_frame = tk.Frame(frame, bg='#ffffff')
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        scrollbar_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        
        # Treeview
        self.tabla = ttk.Treeview(tree_frame,
                                 columns=('fecha', 'categoria', 'descripcion', 'monto'),
                                 show='headings',
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set,
                                 selectmode='browse')
        
        scrollbar_y.config(command=self.tabla.yview)
        scrollbar_x.config(command=self.tabla.xview)
        
        # Configurar columnas
        self.tabla.heading('fecha', text='Fecha')
        self.tabla.heading('categoria', text='Categoría')
        self.tabla.heading('descripcion', text='Descripción')
        self.tabla.heading('monto', text='Monto ($)')
        
        self.tabla.column('fecha', width=150, anchor='center')
        self.tabla.column('categoria', width=120, anchor='center')
        self.tabla.column('descripcion', width=300, anchor='w')
        self.tabla.column('monto', width=100, anchor='e')
        
        # Empaquetar
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bind doble click
        self.tabla.bind('<Double-1>', self.confirmar_eliminacion)
    
    def _crear_frame_acciones(self, parent: tk.Frame) -> None:
        """
        Crea el frame con botones de acción.
        """
        frame = tk.Frame(parent, bg='#f0f0f0')
        frame.pack(fill=tk.X)
        
        btn_actualizar = tk.Button(frame,
                                  text="🔄 Actualizar",
                                  command=self.actualizar_todo,
                                  bg='#4caf50',
                                  fg='white',
                                  font=('Arial', 10, 'bold'),
                                  padx=15,
                                  pady=8,
                                  cursor='hand2')
        btn_actualizar.pack(side=tk.LEFT, padx=5)
        
        btn_eliminar = tk.Button(frame,
                                text="🗑️ Eliminar Seleccionado",
                                command=self.confirmar_eliminacion,
                                bg='#f44336',
                                fg='white',
                                font=('Arial', 10, 'bold'),
                                padx=15,
                                pady=8,
                                cursor='hand2')
        btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(frame,
                               text="🧹 Limpiar Campos",
                               command=self.limpiar_campos,
                               bg='#ff9800',
                               fg='white',
                               font=('Arial', 10, 'bold'),
                               padx=15,
                               pady=8,
                               cursor='hand2')
        btn_limpiar.pack(side=tk.LEFT, padx=5)
    
    def guardar_gasto(self) -> None:
        """
        Guarda un nuevo gasto usando el backend.
        """
        categoria = self.categoria_var.get()
        descripcion = self.descripcion_entry.get()
        monto = self.monto_entry.get()
        
        exito, mensaje = self.gestor.guardar_gasto(categoria, descripcion, monto)
        
        if exito:
            messagebox.showinfo("✓ Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_todo()
        else:
            messagebox.showerror("✗ Error", mensaje)
    
    def actualizar_tabla(self) -> None:
        """
        Actualiza la tabla con los gastos del backend.
        """
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Obtener gastos y llenar tabla
        gastos = self.gestor.obtener_gastos()
        for gasto in gastos:
            self.tabla.insert('', tk.END, values=(
                gasto['fecha'],
                gasto['categoria'],
                gasto['descripcion'],
                f"${float(gasto['monto']):.2f}"
            ))
    
    def actualizar_estadisticas(self) -> None:
        """
        Actualiza las estadísticas mostradas.
        """
        stats = self.gestor.obtener_estadisticas()
        
        self.label_total.config(text=f"Total Gastado: ${stats['total_gastos']:.2f}")
        self.label_cantidad.config(text=f"Cantidad de Gastos: {stats['cantidad_gastos']}")
        self.label_promedio.config(text=f"Promedio: ${stats['promedio']:.2f}")
    
    def actualizar_todo(self) -> None:
        """
        Actualiza tabla y estadísticas.
        """
        self.actualizar_tabla()
        self.actualizar_estadisticas()
    
    def confirmar_eliminacion(self, event=None) -> None:
        """
        Confirma y elimina el gasto seleccionado.
        """
        seleccion = self.tabla.selection()
        
        if not seleccion:
            messagebox.showwarning("⚠️ Advertencia", "Por favor, seleccione un gasto para eliminar")
            return
        
        respuesta = messagebox.askyesno("❓ Confirmar",
                                        "¿Está seguro de eliminar este gasto?")
        
        if respuesta:
            # Obtener el índice del item seleccionado
            indice = self.tabla.index(seleccion[0])
            exito, mensaje = self.gestor.eliminar_gasto(indice)
            
            if exito:
                messagebox.showinfo("✓ Éxito", mensaje)
                self.actualizar_todo()
            else:
                messagebox.showerror("✗ Error", mensaje)
    
    def limpiar_campos(self) -> None:
        """
        Limpia los campos de entrada.
        """
        self.combo_categoria.current(0)
        self.descripcion_entry.delete(0, tk.END)
        self.monto_entry.delete(0, tk.END)
        self.descripcion_entry.focus()


def main():
    """
    Función principal para iniciar la aplicación.
    """
    root = tk.Tk()
    app = AplicacionGastos(root)
    root.mainloop()


if __name__ == "__main__":
    main()
