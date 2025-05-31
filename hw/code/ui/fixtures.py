import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
import json
import time
import pathlib

SCRIPT_DIRECTORY = pathlib.Path().absolute()

@pytest.fixture()
def driver(config):
    browser = config["browser"]
    selenoid = config["selenoid"]
    vnc = config["vnc"]
    options = Options()
    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "version": "118.0",
        }
        if vnc:
            capabilities["enableVNC"] = True
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub",
            options=options,
            desired_capabilities=capabilities,
        )
    elif browser == "chrome":
        options.add_argument(f"user-data-dir={SCRIPT_DIRECTORY}/user_data_dir")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.maximize_window()
    driver.get("https://ads.vk.com")
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def all_drivers(config, request):
    url = config["url"]
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)
