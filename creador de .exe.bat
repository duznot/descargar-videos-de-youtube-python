@echo off
echo Instalando PyInstaller...
pip install pyinstaller
echo Instalación completada.
echo.
echo Ejecutando PyInstaller...
pyinstaller --onefile --noconsole --windowed --icon=ic.ico youtube_downloader.py
echo PyInstaller ha terminado.
pause
