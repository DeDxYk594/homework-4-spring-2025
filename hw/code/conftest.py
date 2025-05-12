from selenium import webdriver
from pages.vk_id import VkIdPage

driver = webdriver.Chrome()


class Test1:
    def execute():
        page = VkIdPage(driver)
        page.login()

Test1.execute()

availableTests = []
