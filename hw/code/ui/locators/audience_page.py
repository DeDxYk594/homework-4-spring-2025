from selenium.webdriver.common.by import By

class AudiencePageLocator:
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//span[text()='Создать аудиторию']")
    SOCIAL_GROUP_BUTTON = (By.XPATH, "//span[contains(text(),'Сообщества ВКонтакте')]")

    AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, "input.vkuiInput__el")

    ADD_SOURCE_BUTTON = (By.XPATH, "//button[.='Добавить источник']")  

    SOCIAL_GROUP_BUTTON = (By.CSS_SELECTOR, "[data-testid='appsAndGroups']")

    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-testid='search-input']")

    VK_COMMUNITIES_HEADER = (By.CSS_SELECTOR, "[data-testid='header-title']")

    FIRST_GROUP_RESULT = (
        By.CSS_SELECTOR,
        ".GroupContentItem_item__6gQso"
    )



    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and .//span[contains(text(), 'Сохранить')]]")
