import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pytube import YouTube
import os
from threading import Thread
import requests
from io import BytesIO

def get_available_resolutions(youtube_link):
    try:
        yt = YouTube(youtube_link)
        streams = yt.streams
        streams_with_resolution = [stream for stream in streams if stream.resolution is not None]
        resolutions = set(stream.resolution for stream in streams_with_resolution if stream.resolution in ["720p", "1080p"])
        return sorted(list(resolutions))
    except Exception as e:
        print(f"Error al obtener resoluciones: {str(e)}")
        return []

def search_video(event=None):
    display_video_info(youtube_link_entry.get())
    update_resolution_combobox()

def download_video():
    youtube_link = youtube_link_entry.get()
    resolution = resolution_combobox.get()

    def download():
        try:
            yt = YouTube(youtube_link)
            video = yt.streams.filter(res=resolution, progressive=True).first()
            if video:
                video.download(output_path='videos/')
                video_name = f"{yt.title}.mp4"
                completion_label.config(text=f'Descarga completada: {video_name}')
            else:
                completion_label.config(text="Error: Video no disponible en la resolución especificada.")
        except Exception as e:
            completion_label.config(text=f"Error: {str(e)}")
        finally:
            download_button.config(state="normal")

    download_button.config(state="disabled")
    download_thread = Thread(target=download)
    download_thread.start()

def update_resolution_combobox(event=None):
    resolutions = get_available_resolutions(youtube_link_entry.get())
    resolution_combobox['values'] = resolutions
    if resolutions:
        resolution_combobox.current(0)
    else:
        resolution_combobox.set('')
        completion_label.config(text="Error: No se encontraron resoluciones disponibles para este video.")

def display_video_info(youtube_link):
    try:
        yt = YouTube(youtube_link)
        video_title = yt.title
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_image = Image.open(BytesIO(response.content))
        thumbnail_image = thumbnail_image.resize((120, 90))
        thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)
        
        video_info_label.config(text=video_title)
        thumbnail_label.config(image=thumbnail_photo)
        thumbnail_label.image = thumbnail_photo
        
    except Exception as e:
        print(f"Error al mostrar información del video: {str(e)}")

root = tk.Tk()
root.title("Descargador de YouTube")
root.geometry("460x300")

main_frame = ttk.Frame(root)
main_frame.pack(pady=20)

title_label = ttk.Label(main_frame, text="Descargador de YouTube")
title_label.grid(row=0, column=0, columnspan=3)

youtube_link_label = ttk.Label(main_frame, text="Enlace de YouTube:")
youtube_link_label.grid(row=1, column=0, sticky="w")
youtube_link_entry = ttk.Entry(main_frame, width=40)
youtube_link_entry.grid(row=1, column=1, columnspan=2)
youtube_link_entry.bind("<Return>", search_video)

search_button = ttk.Button(main_frame, text="Buscar Video", command=search_video)
search_button.grid(row=1, column=3)

video_info_frame = ttk.Frame(main_frame)
video_info_frame.grid(row=2, column=0, columnspan=4, pady=10)

thumbnail_label = ttk.Label(video_info_frame)
thumbnail_label.grid(row=0, column=0, padx=5)

video_info_label = ttk.Label(video_info_frame, text="", wraplength=200)
video_info_label.grid(row=0, column=1, padx=5)

resolution_label = ttk.Label(video_info_frame, text="Resoluciones disponibles:")
resolution_label.grid(row=1, column=0, columnspan=2, pady=5)

resolution_combobox = ttk.Combobox(video_info_frame, state="readonly")
resolution_combobox.grid(row=2, column=0, columnspan=2)

download_button = ttk.Button(main_frame, text="Descargar", command=download_video)
download_button.grid(row=3, column=0, columnspan=4)

completion_label = ttk.Label(main_frame, text="")
completion_label.grid(row=4, column=0, columnspan=4)

# Marca de agua
watermark_label = ttk.Label(root, text="Desarrollado por duznot: https://github.com/duznot", font=("Helvetica", 8), background="white")
watermark_label.place(relx=1, rely=1, anchor='se')

if not os.path.exists('videos'):
    os.makedirs('videos')

root.mainloop()





