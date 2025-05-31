from selenium.webdriver.common.by import By
from .basic_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]',
    )
    EVENTS = (By.ID, "events")
    READ_MORE = (By.CSS_SELECTOR, "a.readmore")
