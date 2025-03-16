import os

BASE_DIR = os.getcwd()
DOWNLOAD_DIR = os.path.join(BASE_DIR, "download")
START_PAGE = "https://www.wildberries.ru/catalog/192186031/feedbacks?imtId=183532775&size=31"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)