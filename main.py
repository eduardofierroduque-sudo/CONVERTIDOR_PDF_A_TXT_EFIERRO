import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class ConvertidorPDF:
    def __init__(self, root):
        self.root = root
        self.root.title("CONVERTIDOR_PDF_A_TXT_EFIERRO")
        self.root.geometry("600x550")
        
        # Color de fondo principal (Negro)
        self.root.configure(bg="#000000")
        
        self.texto_extraido = ""

        # Título
        self.label = tk.Label(root, text="CONVERTIDOR PDF A TEXTO", 
                              font=("Arial", 16, "bold"), bg="#000000", fg="#FFFFFF")
        self.label.pack(pady=15)

        # Botón Cargar (Verde Neón / Flúor)
        self.btn_cargar = tk.Button(root, text="1. CARGAR Y EXTRAER PDF", 
                                   command=self.extraer_texto, 
                                   bg="#39FF14", fg="#000000", 
                                   font=("Arial", 10, "bold"), 
                                   width=30, height=2, activebackground="#2ECC71")
        self.btn_cargar.pack(pady=10)

        # Botón Limpiar (Rosa/Magenta Neón)
        self.btn_limpiar = tk.Button(root, text="2. BORRAR / NUEVA CARGA", 
                                    command=self.limpiar_datos, 
                                    bg="#FF007F", fg="#FFFFFF", 
                                    font=("Arial", 10, "bold"), 
                                    width=30, height=2, activebackground="#C71585")
        self.btn_limpiar.pack(pady=10)

        # Área de visualización (Fondo gris muy oscuro)
        self.monitor = scrolledtext.ScrolledText(root, width=65, height=15, 
                                                bg="#1A1A1A", fg="#39FF14", 
                                                insertbackground="white", font=("Consolas", 10))
        self.monitor.pack(pady=15)
        self.monitor.insert(tk.END, "Esperando archivo...")
        self.monitor.config(state=tk.DISABLED)

        # Disclaimer
        self.disclaimer = tk.Label(root, text="Aplicación creada por www.fierroduque.com", 
                                  font=("Arial", 9, "italic"), bg="#000000", fg="#555555")
        self.disclaimer.pack(side=tk.BOTTOM, pady=10)

    def extraer_texto(self):
        ruta_archivo = filedialog.askopenfilename(title="Seleccionar PDF", filetypes=[("Archivos PDF", "*.pdf")])
        if ruta_archivo:
            try:
                with open(ruta_archivo, 'rb') as archivo:
                    lector = PyPDF2.PdfReader(archivo)
                    contenido = ""
                    for i in range(len(lector.pages)):
                        contenido += f"--- PÁGINA {i+1} ---\n"
                        contenido += lector.pages[i].extract_text() + "\n\n"
                
                self.texto_extraido = contenido
                self.monitor.config(state=tk.NORMAL)
                self.monitor.delete(1.0, tk.END)
                self.monitor.insert(tk.END, self.texto_extraido)
                self.monitor.config(state=tk.DISABLED)
                self.guardar_txt()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el PDF: {e}")

    def guardar_txt(self):
        if not self.texto_extraido: return
        ruta_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if ruta_guardado:
            with open(ruta_guardado, 'w', encoding='utf-8') as f:
                f.write(self.texto_extraido)
            messagebox.showinfo("Éxito", "Archivo .txt generado correctamente.")

    def limpiar_datos(self):
        self.texto_extraido = ""
        self.monitor.config(state=tk.NORMAL)
        self.monitor.delete(1.0, tk.END)
        self.monitor.insert(tk.END, "Esperando archivo...")
        self.monitor.config(state=tk.DISABLED)
        messagebox.showinfo("Limpieza", "Datos borrados. Listo para cargar otro PDF.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertidorPDF(root)
    root.mainloop()