from selenium.webdriver.common.by import By

class GroupCreationPageLocators:
    CONTINUE_BUTTON = (
        By.XPATH,
        "//span[@class='vkuiButton__in'][.//span[text()='Продолжить']]"
    )
    COUNTRY_SELECT = (
        By.XPATH,
        "//span[@class='vkuiButton__content' and text()='Москва']"
    )
