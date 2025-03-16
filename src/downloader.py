import os
import yt_dlp
from src.config import DOWNLOAD_DIR

def download_video_yt_dlp(video_url, output_filename):
    """
    Скачивает видео через yt-dlp, сохраняя итоговый файл в папку download,
    а временные файлы в download/temp.
    """
    output_path = os.path.join(DOWNLOAD_DIR, output_filename)
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best',
        'paths': {
            'home': DOWNLOAD_DIR
        },
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Видео успешно сохранено: {output_path}")
    except Exception as e:
        print("Ошибка при скачивании видео через yt-dlp:", e)
