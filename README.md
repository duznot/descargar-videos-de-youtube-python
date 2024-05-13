# Descargador de YouTube

Este es un programa de descarga de videos de YouTube con una interfaz gráfica simple construida en Python utilizando Tkinter.

### Librerías necesarias:
- `tkinter`: Para la creación de la interfaz gráfica.
- `PIL` (Python Imaging Library): Para manipulación de imágenes.
- `pytube`: Para descargar videos de YouTube.
- `os`: Para manipulación de archivos y directorios.
- `threading`: Para ejecutar la descarga en un hilo separado.
- `requests`: Para realizar solicitudes HTTP.
- `io`: Para trabajar con datos binarios en memoria.

### Instalación de librerías:
Puedes instalar estas librerías utilizando pip. Ejecuta los siguientes comandos en tu terminal:

```bash
pip install pillow
pip install pytube
```

### Funcionamiento del código:
1. El usuario ingresa el enlace de YouTube en el cuadro de entrada.
2. Al presionar el botón "Buscar Video", se muestra la información del video, incluido su título y una miniatura.
3. Se actualiza el menú desplegable con las resoluciones disponibles para el video.
4. El usuario selecciona una resolución y presiona el botón "Descargar" para iniciar la descarga.
5. Mientras se descarga el video, se desactiva el botón de descarga para evitar descargas múltiples simultáneas.
6. Una vez completada la descarga, se muestra un mensaje de éxito o error.

### Uso en el código:
- `get_available_resolutions(youtube_link)`: Obtiene las resoluciones disponibles para un video de YouTube dado.
- `search_video(event=None)`: Busca y muestra la información del video cuando se presiona el botón "Buscar Video".
- `download_video()`: Descarga el video seleccionado en la resolución especificada.
- `update_resolution_combobox(event=None)`: Actualiza el menú desplegable de resoluciones disponibles.
- `display_video_info(youtube_link)`: Muestra el título y la miniatura del video.

### Ejecución del programa:
- El programa comienza creando una ventana principal (`root`) con la interfaz de usuario.
- Se crean varios widgets como etiquetas, cuadros de entrada, botones y menús desplegables para la interacción del usuario.
- El bucle principal (`root.mainloop()`) mantiene la ventana abierta y receptiva a la interacción del usuario.


## Ejecución rápida

También proporciono un archivo ejecutable (.exe) que contiene el programa. Este archivo es útil si no deseas instalar las librerías manualmente y prefieres una ejecución rápida.

Puedes encontrar el archivo ejecutable en la sección de "Releases" en este repositorio.

¡Disfruta del descargador de YouTube!

¡Espero que esta explicación te ayude a comprender el funcionamiento del código! Si tienes alguna pregunta adicional o necesitas más detalles sobre alguna parte específica, no dudes en preguntar.


# Automatización de instalación y creación de ejecutable con PyInstaller

Este archivo de lote (.bat) es un script de Windows que automatiza la instalación de PyInstaller y la creación de un ejecutable de un script de Python llamado `youtube_downloader.py`. A continuación se presenta una descripción línea por línea del script:

- `@echo off`: Desactiva la visualización de los comandos del archivo por la consola de Windows. Es común usarlo al inicio de un script de lote para hacer que el script sea más limpio.

- `echo Instalando PyInstaller...`: Imprime en la consola el mensaje "Instalando PyInstaller...".

- `pip install pyinstaller`: Utiliza pip (el administrador de paquetes de Python) para instalar PyInstaller en el sistema.

- `echo Instalación completada.`: Imprime en la consola el mensaje "Instalación completada." para indicar que la instalación ha finalizado.

- `echo.`: Imprime una línea en blanco en la consola para mejorar la legibilidad.

- `echo Ejecutando PyInstaller...`: Imprime en la consola el mensaje "Ejecutando PyInstaller..." para indicar que se está ejecutando el proceso de creación del ejecutable.

- `pyinstaller --onefile --noconsole --windowed --icon=ic.ico youtube_downloader.py`: Llama a PyInstaller con una serie de opciones para generar un ejecutable único (--onefile) sin una ventana de consola visible (--noconsole y --windowed) y con un ícono personalizado (--icon=ic.ico). El script de Python que se está convirtiendo en un ejecutable es `youtube_downloader.py`.

- `echo PyInstaller ha terminado.`: Imprime en la consola el mensaje "PyInstaller ha terminado." para indicar que el proceso de creación del ejecutable ha finalizado.

- `pause`: Pausa la ejecución del script hasta que el usuario presione una tecla. Esto es útil para que el usuario pueda leer los mensajes de la consola antes de que esta se cierre automáticamente.


