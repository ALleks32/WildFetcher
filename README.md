# WildFetcher

WildFetcher – это Python-скрипт для выгрузки видео-отзывов с маркетплейса [Wildberries](https://www.wildberries.ru) в формате MP4. Приложение позволяет выбрать отзыв с видео, открыть его в браузере и по нажатию горячей клавиши (F4) скачать видео на локальный компьютер. Каждый раз, когда открывается новое видео, оно скачивается по той же логике.

---

## Функциональность

- **Извлечение видео**: Скрипт определяет активное видео-отзыв (на основе слайдера) и извлекает URL потока (HLS URL) из сетевых запросов.
- **Горячая клавиша**: При нажатии F4 скрипт автоматически извлекает URL видео и инициирует его скачивание.
- **Скачивание**: Используя `yt-dlp`, видео скачивается в формате MP4 в указанную директорию.

---

**Логика работы**:
1. Пользователь выбирает отзыв с видео и открывает его на странице.
2. По нажатию горячей клавиши (например, F4) скрипт:
   - Ждёт появления активного видео-элемента.
   - Инициирует воспроизведение видео.
   - Извлекает URL потока (HLS, содержащий `m3u8`).
   - Передаёт URL в `yt-dlp` для скачивания видео в формате MP4.
3. Каждое новое видео (смена активного слайда) скачивается отдельно.
