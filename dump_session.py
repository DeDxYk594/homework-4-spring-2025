from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_argument("--verbose")
options.add_argument("user-data-dir=vkads-userdata")
options.add_argument("profile-directory=vkads-profile")


driver = webdriver.Chrome(options=options)

input("click Enter to exit...")
driver.quit()
