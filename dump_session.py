from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--verbose")
options.add_argument("user-data-dir=user_data_dir")

driver = webdriver.Chrome(options=options)

input("click Enter to exit...")
driver.quit()
