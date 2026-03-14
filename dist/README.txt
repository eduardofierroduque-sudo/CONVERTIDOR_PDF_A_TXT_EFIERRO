////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

ESPAÑOL:

CONVERTIDOR_PDF_A_TXT_EFIERRO

Esta es una herramienta robusta y ligera desarrollada en Python para la extracción masiva de texto desde archivos PDF,
optimizada con una interfaz de estilo Neón/Modo Oscuro.

Qué hace: Extrae texto de PDF a TXT de forma rápida.
Tecnologías: Python 3.14, PyPDF2, Tkinter.
Créditos: Creado por www.fierroduque.com.

La aplicación utiliza la librería PyPDF2 para procesar los documentos. El flujo de trabajo es simple:
Carga: El usuario selecciona un archivo PDF local.
Procesamiento: El script recorre cada página, detecta los caracteres y mantiene el orden secuencial del documento original.
Visualización: Se muestra una previsualización inmediata en el monitor de consola integrado (estilo terminal).
Exportación: El sistema solicita una ruta para guardar el resultado final en un formato de texto plano (.txt) con codificación UTF-8 para preservar caracteres especiales (acentos, ñ, etc.).

¿Cómo hacerlo funcionar?
Tienes dos formas de ejecutar esta aplicación:
A. Para Usuarios (Ejecutable .exe)

Si solo quieres usar la herramienta sin configurar código:

Dirígete a la sección de Releases en este repositorio.
Descarga el archivo Convertidor_Efierro.exe.
Ejecútalo directamente en Windows. No requiere instalación.

B. Para Desarrolladores (Código Fuente)
Si deseas modificar el código o ejecutarlo desde Python, sigue estos pasos:

Bash
git clone https://github.com/TU_USUARIO/CONVERTIDOR_PDF_A_TXT_EFIERRO.git
cd CONVERTIDOR_PDF_A_TXT_EFIERRO

Instalar dependencias:
Asegúrate de tener Python 3.x instalado y luego ejecuta:

Bash
python -m pip install PyPDF2

Ejecutar la aplicación:

Bash
python main.py

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
