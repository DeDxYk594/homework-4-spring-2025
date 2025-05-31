import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pathlib
from typing import TypedDict, Literal

SCRIPT_DIRECTORY = pathlib.Path().absolute()


class ConfigType(TypedDict):
    browser: Literal["chrome", "firefox"]
    selenoid: bool


@pytest.fixture()
def driver(config: ConfigType):
    browser = config["browser"]
    selenoid = config["selenoid"]
    if selenoid:
        options = ChromeOptions()
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub",
            options=options,
        )
    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument(f"user-data-dir={SCRIPT_DIRECTORY}/user_data_dir")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def config() -> ConfigType:
    return {
        "browser": "chrome",
        "selenoid": False,
    }


# TODO: сделать здесь фикстуры для всех страниц
