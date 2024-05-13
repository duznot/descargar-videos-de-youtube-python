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

