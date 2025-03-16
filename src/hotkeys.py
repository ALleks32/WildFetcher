import time
import keyboard
from src.video_extractor import get_video_url
from src.downloader import download_video_yt_dlp

prev_video_id = None

def on_hotkey(driver):
    """
    Обработчик горячей клавиши F4.
    Извлекает новый URL видео и инициирует скачивание через yt-dlp.
    """
    global prev_video_id
    print("Горячая клавиша нажата. Ищем URL видео...")
    video_url, video_id = get_video_url(driver, previous_video_id=prev_video_id)
    if not video_url:
        print("Не удалось получить корректный URL видео!")
        return
    print("Найден URL видео:", video_url)
    # Обновляем глобальные переменные, чтобы при следующем нажатии искать новый элемент
    prev_video_id = video_id
    output_filename = f"video_{int(time.time())}.mp4"
    download_video_yt_dlp(video_url, output_filename)

def register_hotkeys(driver):
    """
    Регистрирует горячие клавиши, передавая driver в обработчик.
    """
    keyboard.add_hotkey('F4', lambda: on_hotkey(driver))