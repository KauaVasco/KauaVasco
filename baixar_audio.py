import os
import sys

import yt_dlp

url = input("URL do vídeo: ")

# Uso: python baixar_audio.py [pasta_destino]  (padrão: Downloads)
pasta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.expanduser("~"), "Downloads")

opcoes = {
    # Áudio original, sem recodificar (nenhuma perda extra de qualidade para editar)
    "format": "bestaudio[ext=m4a]/bestaudio/best",
    "outtmpl": os.path.join(pasta, "%(title)s.%(ext)s"),
}

with yt_dlp.YoutubeDL(opcoes) as ydl:
    ydl.download([url])

print(f"Áudio salvo em: {pasta}")
