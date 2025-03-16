import keyboard
from seleniumwire import webdriver
from src.config import START_PAGE
from src.hotkeys import register_hotkeys

def main():
    # Настройка Chrome в headless режиме для ускорения
    options = webdriver.ChromeOptions()

    # Инициализируем Selenium Wire WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get(START_PAGE)

    print("Скрипт запущен. Откройте видео-отзыв и нажмите F4 для скачивания видео в формате mp4.")
    # Регистрируем горячие клавиши через отдельный модуль
    register_hotkeys(driver)

    try:
        keyboard.wait()  # Ожидаем нажатия клавиш
    except KeyboardInterrupt:
        print("Прерывание выполнения скрипта.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()