from selenium.webdriver.common.by import By

class AudiencePageLocator:
    STUB_NO_AUDIENCES_TEXT = (By.XPATH, "//span[contains(text(), 'Аудиторий пока нет')]")
    MORE_MENU_BUTTON = (By.CSS_SELECTOR, "[data-testid='other-buttons']")
    HELP_LINK = (By.XPATH, "//a[contains(@href, '/help/features/audiences_lists/audiences')]")


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
    MODAL_CANCEL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cancel']")
    CREATE_AUDIENCE_FORM = (By.CSS_SELECTOR, "[data-testid='create-audience-form']")
    MODAL_ROOT = (By.CSS_SELECTOR, '[data-testid="audience_modal"]')
    UNSAVED_CHANGES_MODAL = (
        By.XPATH,
        "//div[contains(@data-testid, 'modal-confirm')]//span[contains(text(), 'Прервать создание?')]"
    )
    
    EXCLUDE_CATEGORY_MY_AUDIENCES = (By.XPATH, "//span[contains(text(),'Мои аудитории')]")
    EXCLUDE_CATEGORY_USER_REACTIONS = (By.XPATH, "//span[contains(text(),'По событиям или реакциям пользователей')]")
    EXCLUDE_CATEGORY_INTERESTS = (By.XPATH, "//span[contains(text(),'По интересам')]")
    APP_CATEGORY_BUTTON = (By.CSS_SELECTOR, "[data-testid='appCategories']")
    ADDED_SOURCE_APP_CATEGORY = (By.XPATH, "//span[contains(text(), 'Категории мобильного приложения')]")
    CREATED_AUDIENCE_NAME_TEMPLATE = lambda name: (By.XPATH, f"//span[contains(text(), '{name}')]")


    USERS_LIST_BUTTON = (By.CSS_SELECTOR, "[data-testid='usersList']")
    TAB_UPLOAD_NEW = (By.ID, "tab-create-from-user-list-new")
    LIST_TYPE_COMBOBOX = (By.CSS_SELECTOR, "input[role='combobox']")
    FILE_UPLOAD_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    FILE_UPLOAD_CONTENT = (By.CSS_SELECTOR, ".FileUpload_content__yDG-3")
    VALID_USERS_BLOCK = (By.CSS_SELECTOR, "[data-testid='valid']")
    INVALID_USERS_BLOCK = (By.CSS_SELECTOR, "[data-testid='invalid']")
    LIST_TYPE_COMBOBOX = (By.CSS_SELECTOR, "input[role='combobox']")


class AppCategoryLocators:
    PLATFORM_SELECTOR = (By.CSS_SELECTOR, "input[data-testid='sources.app_category.platform_selector']")
    CATEGORY_SELECTOR = (By.CSS_SELECTOR, "input[data-testid='sources.app_category.category_selector']")
    INSTALL_TYPE_SELECTOR = (By.CSS_SELECTOR, "input[data-testid='sources.app_category.install_type_selector']")
