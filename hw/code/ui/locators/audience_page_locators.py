from selenium.webdriver.common.by import By

class AudiencePageLocator:
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//span[text()='Создать аудиторию']")
    SOCIAL_GROUP_BUTTON = (By.XPATH, "//span[contains(text(),'Сообщества ВКонтакте')]")

    AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, "input.vkuiInput__el")

    ADD_SOURCE_BUTTON = (By.XPATH, "//button[.='Добавить источник']")
    ADD_SOURCE_BUTTON_IN_LIST = (By.CSS_SELECTOR, '[data-testid="positive-sources-list"] [data-testid="add-source"]')

    SOCIAL_GROUP_BUTTON = (By.CSS_SELECTOR, "[data-testid='appsAndGroups']")

    SEARCH_INPUT = (By.CSS_SELECTOR, "input.vkuiInput__el[placeholder='Введите название сообщества']")

    VK_COMMUNITIES_HEADER = (By.XPATH, "//h2[text()='Подписчики сообществ']")

    FIRST_GROUP_RESULT = (By.CSS_SELECTOR, '[data-testid="header-title"] span')
    FIRST_RESULT_ITEM = (By.CSS_SELECTOR, "[class^='GroupContentItem_item']")

    EXIT_GROUP_SELECTION_TITLE = (
        By.XPATH,
        "//h2[text()='Подписчики сообществ']"
    )

    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="submit"]')
    EXCLUDE_SOURCE_BUTTON = (By.CSS_SELECTOR, "[data-testid='exclude-source']")
    MODAL_ROOT = (By.CSS_SELECTOR, '[data-testid="audience_modal"]')
    

    APP_CATEGORY_BUTTON = (By.CSS_SELECTOR, '[data-testid="appCategories"]')




    # AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, "input[data-testid='audience-name-input']")
    # ADD_SOURCE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='add-source']")
    # SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='submit']")

    # EMPTY_STATE_TEXT = (By.XPATH, "//span[contains(text(), 'Аудиторий пока нет')]")
    # CREATE_BUTTON = (By.CSS_SELECTOR, "[data-testid='create-audience']")
    # MORE_MENU = (By.CSS_SELECTOR, "[data-testid='other-buttons']")
    # HELP_LINK = (By.XPATH, "//a[contains(@href, '/help/features/audiences_lists/audiences')]")

    # CANCEL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cancel']")
    # CREATE_AUDIENCE_FORM = (By.CSS_SELECTOR, "[data-testid='create-audience-form']")
    # MODAL_ROOT = (By.CLASS_NAME, "vkuiModalRoot")

    # LENGTH_ERROR = (By.XPATH, "//*[contains(text(), 'не больше 255 символов')]")
    # CONFIRM_POPUP = (
    #     By.XPATH, "//div[contains(@data-testid, 'modal-confirm')]//span[contains(text(), 'Прервать создание?')]"
    # )