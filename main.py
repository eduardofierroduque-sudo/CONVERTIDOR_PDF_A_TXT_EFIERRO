import fitz  # PyMuPDF
import os
import sys
import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView 
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.image import Image 
from kivy.clock import Clock 
from docx import Document
from tkinter import filedialog 

# --- SOPORTE PARA SPLASH SCREEN NATIVO (PyInstaller) ---
try:
    import pyi_splash
except ImportError:
    pyi_splash = None

# --- FUNCIÓN CLAVE PARA RUTAS ---
def resource_path(relative_path):
    """ Gestiona las rutas de archivos para que funcionen tras la compilación """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

Window.size = (380, 680)

# --- CLASE: BOTÓN VERDE NEÓN ---
class BotonFluorescente(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (0, 0, 0, 1)
        self.bold = True
        self.font_size = '18sp'
        self.t = 0 

        with self.canvas.before:
            self.glow_color = Color(0.2, 1, 0, 0.4) 
            self.glow1 = Rectangle(size=(self.width + 15, self.height + 15))
            self.core_color = Color(0.2, 1, 0, 1)
            self.rect_core = Rectangle(size=self.size)
            Color(0, 0, 0, 1) 
            self.btn_borde = Line(rectangle=(self.x, self.y, self.width, self.height), width=1.5)

        self.bind(pos=self.actualizar_ui, size=self.actualizar_ui)
        Clock.schedule_interval(self.animar_glow, 0.05)

    def actualizar_ui(self, instance, value):
        self.rect_core.pos = instance.pos
        self.rect_core.size = instance.size
        self.glow1.size = (instance.width + 20, instance.height + 20)
        self.glow1.pos = (instance.x - 10, instance.y - 10)
        self.btn_borde.rectangle = (instance.x, instance.y, instance.width, instance.height)

    def animar_glow(self, dt):
        self.t += 0.15
        self.glow_color.a = math.sin(self.t) * 0.25 + 0.45

# --- PANTALLA DE INICIO INTERNA (KIVY) ---
class SplashScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        ruta_logo = resource_path(os.path.join('media', 'logointro_PDF_CONVERTER.png'))
        
        if os.path.exists(ruta_logo):
            self.add_widget(Image(source=ruta_logo, size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        else:
            self.add_widget(Label(text="[b]PDF CONVERTER[/b]\n[size=14]fierroduque.com[/size]", markup=True, halign='center'))

    def actualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# --- INTERFAZ PRINCIPAL ---
class ConvertidorMobile(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dark_mode = True
        self.texto_extraido = ""
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        with self.canvas.before:
            self.rect_color = Color(0.05, 0.05, 0.05, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        self.bind(size=self.actualizar_rect, pos=self.actualizar_rect)

        self.btn_tema = Button(text="MODO CLARO", size_hint=(None, None), size=('120dp', '30dp'), pos_hint={'center_x': 0.5}, background_normal='', background_color=(0.2, 0.2, 0.2, 1), font_size='10sp')
        self.btn_tema.bind(on_press=self.toggle_tema)
        self.add_widget(self.btn_tema)

        self.label_titulo = Label(text="[b]PDF[/b] Converter", markup=True, font_size='34sp', size_hint_y=None, height='60dp')
        self.add_widget(self.label_titulo)

        self.btn_cargar = BotonFluorescente(text="SELECCIONAR ARCHIVO", size_hint_y=None, height='80dp')
        self.btn_cargar.bind(on_press=self.seleccionar_y_extraer)
        self.add_widget(self.btn_cargar)

        self.add_widget(Label(text="EXPORTAR A", font_size='11sp', size_hint_y=None, height='20dp', color=(0.5, 0.5, 0.5, 1)))

        grid = GridLayout(cols=3, spacing=10, size_hint_y=None, height='50dp')
        btn_style = {'background_normal': '', 'background_color': (0.15, 0.15, 0.15, 1), 'font_size': '12sp', 'bold': True}
        grid.add_widget(Button(text="TEXT", **btn_style, on_press=lambda x: self.exportar("txt")))
        grid.add_widget(Button(text="MD", **btn_style, on_press=lambda x: self.exportar("md")))
        grid.add_widget(Button(text="WORD", **btn_style, on_press=lambda x: self.exportar("docx")))
        self.add_widget(grid)

        self.scroll = ScrollView(size_hint=(1, 1))
        self.monitor = TextInput(text="Esperando archivo...", readonly=True, background_color=(0, 0, 0, 1), foreground_color=(0.2, 1, 0.2, 1), font_size='12sp', padding=[15, 15], size_hint_y=None)
        self.monitor.bind(minimum_height=self.monitor.setter('height'))
        self.scroll.add_widget(self.monitor)
        self.add_widget(self.scroll)

        self.btn_limpiar = Button(text="BORRAR DATOS", background_normal='', background_color=(0.7, 0, 0.1, 1), size_hint_y=None, height='40dp', bold=True)
        self.btn_limpiar.bind(on_press=self.limpiar)
        self.add_widget(self.btn_limpiar)

        self.add_widget(Label(text="fierroduque.com", font_size='10sp', color=(0.3, 0.3, 0.3, 1), size_hint_y=None, height='20dp'))

    def actualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def toggle_tema(self, instance):
        if self.dark_mode:
            self.rect_color.rgb = (0.95, 0.95, 0.95)
            self.label_titulo.color = (0, 0, 0, 1)
            self.btn_tema.text = "MODO OSCURO"
            self.dark_mode = False
        else:
            self.rect_color.rgb = (0.05, 0.05, 0.05)
            self.label_titulo.color = (1, 1, 1, 1)
            self.btn_tema.text = "MODO CLARO"
            self.dark_mode = True

    def seleccionar_y_extraer(self, instance):
        ruta = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if ruta:
            try:
                doc = fitz.open(ruta)
                texto = "".join([p.get_text() for p in doc])
                self.texto_extraido = texto
                self.monitor.text = texto
                self.scroll.scroll_y = 1
            except Exception as e: self.monitor.text = f"Error: {e}"

    def exportar(self, fmt):
        if not self.texto_extraido: return
        ruta = filedialog.asksaveasfilename(defaultextension=f".{fmt}")
        if ruta:
            if fmt == "docx":
                d = Document(); d.add_paragraph(self.texto_extraido); d.save(ruta)
            else:
                with open(ruta, 'w', encoding='utf-8') as f: f.write(self.texto_extraido)

    def limpiar(self, instance):
        self.texto_extraido = ""; self.monitor.text = "Esperando archivo..."

# --- APLICACIÓN ---
class MainApp(App):
    def build(self):
        self.title = "PDF Converter - fierroduque.com"
        self.root = BoxLayout(orientation='vertical')
        
        # Primero mostramos el splash interno de Kivy
        self.splash = SplashScreen()
        self.root.add_widget(self.splash)
        
        # Programamos el cambio a la app principal
        Clock.schedule_once(self.mostrar_app, 3)
        return self.root

    def mostrar_app(self, dt):
        # 1. Limpiamos el splash interno
        self.root.clear_widgets()
        # 2. Cargamos la interfaz principal
        self.root.add_widget(ConvertidorMobile())
        
        # 3. CERRAMOS EL SPLASH NATIVO DE WINDOWS (si existe)
        if pyi_splash:
            pyi_splash.close()

if __name__ == "__main__":
    MainApp().run()
