from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib

SCRIPT_DIRECTORY = pathlib.Path().absolute()

options = Options()

options.add_argument("--verbose")
options.add_argument(f"user-data-dir={SCRIPT_DIRECTORY}/user_data_dir")

driver = webdriver.Chrome(options=options)

driver.get("https://ads.vk.com")

input("click Enter to exit...")
driver.quit()
