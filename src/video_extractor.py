import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_hls_url(driver, expected_substring=None, timeout=20):
    """
    Ждёт до timeout секунд появления запроса с "m3u8".
    Если expected_substring задан, возвращает только URL, содержащий его.
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        for request in driver.requests:
            if request.response and "m3u8" in request.url:
                if expected_substring is None or expected_substring in request.url:
                    print("Найден HLS URL:", request.url)
                    return request.url
        time.sleep(1)
    print("HLS URL не найден за отведенное время.")
    return None


def get_video_url(driver, previous_video_id=None):
    try:
        # Ждём, пока в активном слайде появится элемент <video>
        video = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.swiper-slide-active video"))
        )
        current_video_id = video.get_attribute("id")
        if previous_video_id is not None and current_video_id == previous_video_id:
            print("Активное видео не изменилось, id:", current_video_id)
            return None, current_video_id
        print("Найден активный элемент <video> с id:", current_video_id)

        # Прокручиваем к видео
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", video
        )

        # Очищаем предыдущие сетевые запросы
        driver.requests.clear()

        # Пытаемся кликнуть по кнопке большого воспроизведения, если она есть
        try:
            play_btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".vjs-big-play-button"))
            )
            play_btn.click()
            print("Клик по кнопке воспроизведения выполнен.")
        except Exception as e:
            print("Кнопка воспроизведения не найдена или не кликается:", e)

        # Принудительно запускаем воспроизведение и делаем видео без звука
        driver.execute_script("arguments[0].muted = true;", video)
        driver.execute_script("arguments[0].play();", video)
        print("Вызван video.play(), ждем инициализацию потока...")


        src = video.get_attribute("src")
        print("Атрибут src видео:", src)

        # Если src пуст или начинается с "blob:" – ищем HLS URL
        if not src or src.startswith("blob:"):
            poster_url = video.get_attribute("poster")
            expected_base = None
            if poster_url:
                # Из poster получаем базовую часть URL, убираем "preview.webp"
                expected_base = poster_url.replace("preview.webp", "")
                print("Ожидаем, что HLS URL содержит:", expected_base)
            hls_url = extract_hls_url(driver, expected_substring=expected_base, timeout=20)
            if hls_url:
                return hls_url, current_video_id
            else:
                print("HLS URL не найден в сетевых запросах.")
                return None, current_video_id
        else:
            return src, current_video_id
    except Exception as e:
        print("Ошибка при получении URL видео:", e)
        return None, None