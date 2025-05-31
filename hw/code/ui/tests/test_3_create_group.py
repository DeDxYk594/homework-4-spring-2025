# TODO: @zhugeo
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.main_page import MainPage


def test_should_return_2_plus_2_is_4_when_called(driver: WebDriver):
    assert 2 + 2 == 4
    driver.get("https://vk.com")
    MainPage(driver).is_opened()
