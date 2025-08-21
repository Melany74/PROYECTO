import tkinter as tk
from tkinter import ttk, messagebox

class ConversorSistemasNumericos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Convertidor de Sistemas Numéricos")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg='#f0f0f0')
        
        # Variables de entrada
        self.entrada_var = tk.StringVar()
        self.sistema_origen = tk.StringVar(value="decimal")
        
        # Variables de resultado 
        self.resultado_decimal = tk.StringVar()
        self.resultado_binario = tk.StringVar()
        self.resultado_octal = tk.StringVar()
        self.resultado_hex = tk.StringVar()
        
        # Diccionario para mapear campos de resultado
        self.campos_resultado = {}
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.ventana, text="Convertidor de Sistemas Numéricos", 
                         font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=20)

        # Frame principal
        frame_principal = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_principal.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Sección de entrada
        frame_entrada = tk.LabelFrame(frame_principal, text="Número a convertir", 
                                    font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#34495e')
        frame_entrada.pack(fill='x', padx=10, pady=10)
        
        # Campo de entrada
        tk.Label(frame_entrada, text="Ingresa el número:", bg='#f0f0f0').pack(anchor='w', padx=10, pady=5)
        entrada = tk.Entry(frame_entrada, textvariable=self.entrada_var, font=("Arial", 14), width=30)
        entrada.pack(padx=10, pady=5)
        
        # Selección del sistema de origen
        tk.Label(frame_entrada, text="Sistema del número ingresado:", bg='#f0f0f0').pack(anchor='w', padx=10, pady=(10,5))
        
        frame_opciones = tk.Frame(frame_entrada, bg='#f0f0f0')
        frame_opciones.pack(padx=10, pady=5)
        
        sistemas = [("Decimal", "decimal"), ("Binario", "binario"), ("Octal", "octal"), ("Hexadecimal", "hexadecimal")]
        
        for texto, valor in sistemas:
            rb = tk.Radiobutton(frame_opciones, text=texto, variable=self.sistema_origen, 
                               value=valor, bg='#f0f0f0', font=("Arial", 10),
                               command=self.actualizar_resultados_visibles)
            rb.pack(side='left', padx=10)
        
        # Botón de conversión
        boton_convertir = tk.Button(frame_entrada, text="Convertir", command=self.convertir,
                                   bg='#3498db', fg='white', font=("Arial", 12, "bold"), 
                                   width=15, height=2)
        boton_convertir.pack(pady=15)
        
        # Sección de resultados
        self.frame_resultados = tk.LabelFrame(frame_principal, text="Resultados", 
                                       font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#34495e')
        self.frame_resultados.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear todos los campos de resultado
        self.crear_todos_los_campos_resultado()
        
        # Actualizar visibilidad inicial
        self.actualizar_resultados_visibles()
        
        # Botones adicionales
        frame_botones = tk.Frame(frame_principal, bg='#f0f0f0')
        frame_botones.pack(pady=10)
        
        boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar,
                                 bg='#95a5a6', fg='white', font=("Arial", 10), width=12)
        boton_limpiar.pack(side='left', padx=5)
        
        boton_salir = tk.Button(frame_botones, text="Salir", command=self.ventana.quit,
                               bg='#e74c3c', fg='white', font=("Arial", 10), width=12)
        boton_salir.pack(side='right', padx=5)
    
    def crear_todos_los_campos_resultado(self):
        # Crear todos los campos pero no mostrarlos aún
        campos = [
            ("decimal", "Decimal:", self.resultado_decimal, "#e74c3c"),
            ("binario", "Binario:", self.resultado_binario, "#27ae60"),
            ("octal", "Octal:", self.resultado_octal, "#f39c12"),
            ("hexadecimal", "Hexadecimal:", self.resultado_hex, "#9b59b6")
        ]
        
        for sistema, etiqueta, variable, color in campos:
            frame = tk.Frame(self.frame_resultados, bg='#f0f0f0')
            
            label = tk.Label(frame, text=etiqueta, font=("Arial", 11, "bold"), 
                            bg='#f0f0f0', fg=color, width=12, anchor='w')
            label.pack(side='left')
            
            entrada = tk.Entry(frame, textvariable=variable, font=("Arial", 11), 
                              state='readonly', readonlybackground='white')
            entrada.pack(side='right', fill='x', expand=True, padx=(10, 0))
            
            # Guardar referencia al frame para poder ocultarlo/mostrarlo
            self.campos_resultado[sistema] = frame
    
    def actualizar_resultados_visibles(self):
        sistema_seleccionado = self.sistema_origen.get()
        
        # Ocultar todos los campos primero
        for frame in self.campos_resultado.values():
            frame.pack_forget()
        
        # Mostrar solo los campos que no corresponden al sistema de origen
        for sistema, frame in self.campos_resultado.items():
            if sistema != sistema_seleccionado:
                frame.pack(fill='x', padx=10, pady=5)
        
        # Limpiar resultados cuando cambie el sistema
        self.limpiar_solo_resultados()
    
    def convertir(self):
        try:
            numero_str = self.entrada_var.get().strip()
            if not numero_str:
                messagebox.showwarning("Advertencia", "Por favor ingresa un número")
                return
            
            sistema = self.sistema_origen.get()
            
            # Convertir a decimal primero
            if sistema == "decimal":
                decimal = int(numero_str)
            elif sistema == "binario":
                if not all(c in '01' for c in numero_str):
                    raise ValueError("Número binario inválido")
                decimal = int(numero_str, 2)
            elif sistema == "octal":
                if not all(c in '01234567' for c in numero_str):
                    raise ValueError("Número octal inválido")
                decimal = int(numero_str, 8)
            elif sistema == "hexadecimal":
                decimal = int(numero_str, 16)
            
            # Verificar que el número no sea negativo
            if decimal < 0:
                raise ValueError("Este conversor solo acepta números positivos")
            
            # Realizar todas las conversiones (solo las que se van a mostrar)
            if sistema != "decimal":
                self.resultado_decimal.set(str(decimal))
            if sistema != "binario":
                self.resultado_binario.set(bin(decimal)[2:])  # [2:] para quitar el prefijo '0b'
            if sistema != "octal":
                self.resultado_octal.set(oct(decimal)[2:])    # [2:] para quitar el prefijo '0o'
            if sistema != "hexadecimal":
                self.resultado_hex.set(hex(decimal)[2:].upper())  # [2:] para quitar el prefijo '0x'
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error en la conversión: {str(e)}")
            self.limpiar_solo_resultados()
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
            self.limpiar_solo_resultados()
    
    def limpiar_solo_resultados(self):
        self.resultado_decimal.set("")
        self.resultado_binario.set("")
        self.resultado_octal.set("")
        self.resultado_hex.set("")
    
    def limpiar(self):
        self.entrada_var.set("")
        self.limpiar_solo_resultados()

def main():
    ventana = tk.Tk()
    app = ConversorSistemasNumericos(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
