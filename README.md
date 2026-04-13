CONVERTIDOR_PDF_A_TXT_EFIERRO (v2.0 - Neon Edition)

Esta es una herramienta robusta, ligera y de alto impacto visual desarrollada en Python para la extracción avanzada de texto desde archivos PDF.
Ha sido evolucionada de una interfaz básica a una experiencia de usuario moderna con estética Neon/Cyberpunk y soporte multiplataforma.
¿Qué hace?: Convierte documentos PDF a formatos editables (.txt, .md, .docx) manteniendo la integridad del texto.

Tecnologías: Python 3.12+, Kivy (UI/UX), PyMuPDF (Motor de extracción), python-docx.
Créditos: Creado por www.fierroduque.com.

Descargar .exe: [Enlace a tu Release]

Novedades de la Versión 2.0
Interfaz Kivy: Motor gráfico de alto rendimiento con soporte para animaciones.
Efecto Glow Neon: Botones dinámicos con pulsación fluorescente.
Splash Screen: Pantalla de carga nativa durante el inicio de la aplicación.
Modo Dual: Selector de tema Claro y Oscuro en tiempo real.
Exportación Versátil: Soporte para formatos Word (.docx) y Markdown (.md).

Requerimientos Técnicos
Para el correcto funcionamiento del código fuente, se requieren las siguientes dependencias:

Plaintext
kivy[base]
pymupdf
python-docx
lxml
pyinstaller

 ¿Cómo funciona?
La aplicación utiliza un flujo de procesamiento optimizado:
Carga Inteligente: Selección de archivo mediante el explorador nativo.
Motor PyMuPDF: Procesa el documento con una velocidad superior, detectando caracteres complejos y fuentes.
Monitor de Consola: Previsualización inmediata en un terminal integrado con scroll automático.
Codificación Universal: Exportación en UTF-8 para garantizar la compatibilidad total con tildes y caracteres especiales.

 Instrucciones de Uso
A. Para Usuarios Finales (Windows)
En la columna derecha de este repositorio, busca la sección Releases.

Descarga el archivo PDF_Converter_v1.exe.

Nota de Seguridad: Debido a que la app no posee firma digital comercial, Windows SmartScreen podría mostrar un aviso. Haz clic en "Más información" y luego en "Ejecutar de todas formas".

B. Para Desarrolladores (Código Fuente)
Si deseas modificar el código o contribuir a la mejora:

Clonar el proyecto:
git clone https://github.com/eduardofierroduque-sudo/CONVERTIDOR_PDF_A_TXT_EFIERRO.git

Instalar dependencias:
pip install -r requirements.txt

Ejecutar:
python main.py


Nota sobre Seguridad en Windows 11
Si trabajas con Windows 11 y el Smart App Control bloquea las librerías (ImportError: DLL load failed), asegúrate de añadir la carpeta del proyecto a las Exclusiones de tu Antivirus (incluyendo Bitdefender si lo utilizas).

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
