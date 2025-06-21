from selenium.webdriver.common.by import By


class AudiencePageLocator:
    STUB_NO_AUDIENCES_TEXT = (
        By.XPATH,
        "//span[contains(text(), 'Аудиторий пока нет')]",
    )
    MORE_MENU_BUTTON = (By.CSS_SELECTOR, "[data-testid='other-buttons']")
    HELP_LINK = (
        By.XPATH,
        "//a[contains(@href, '/help/features/audiences_lists/audiences')]",
    )

    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//span[text()='Создать аудиторию']")
    SOCIAL_GROUP_BUTTON = (By.XPATH, "//span[contains(text(),'Сообщества ВКонтакте')]")

    AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, "input.vkuiInput__el")

    ADD_SOURCE_BUTTON = (By.XPATH, "//button[.='Добавить источник']")
    ADD_SOURCE_BUTTON_IN_LIST = (
        By.CSS_SELECTOR,
        '[data-testid="positive-sources-list"] [data-testid="add-source"]',
    )

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input.vkuiInput__el[placeholder='Введите название сообщества']",
    )

    NAME_LENGTH_ERROR = (By.XPATH, "//*[contains(text(), 'не больше 255 символов')]")

    VK_COMMUNITIES_HEADER = (By.XPATH, "//h2[text()='Подписчики сообществ']")

    FIRST_GROUP_RESULT = (By.CSS_SELECTOR, '[data-testid="header-title"] span')
    FIRST_RESULT_ITEM = (By.CSS_SELECTOR, "[class^='GroupContentItem_item']")

    EXIT_GROUP_SELECTION_TITLE = (By.XPATH, "//h2[text()='Подписчики сообществ']")

    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="submit"]')
    EXCLUDE_SOURCE_BUTTON = (By.CSS_SELECTOR, "[data-testid='exclude-source']")
    MODAL_CANCEL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cancel']")
    CREATE_AUDIENCE_FORM = (By.CSS_SELECTOR, "[data-testid='create-audience-form']")
    MODAL_ROOT = (By.CSS_SELECTOR, '[data-testid="audience_modal"]')
    UNSAVED_CHANGES_MODAL = (
        By.XPATH,
        "//div[contains(@data-testid, 'modal-confirm')]//span[contains(text(), 'Прервать создание?')]",
    )
    VK_ID_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'CustomSelectOption') and text()='ID ВКонтакте']",
    )
    SOURCE_USERS_LIST_HEADER = (
        By.XPATH,
        "//span[@data-testid='header' and contains(text(), 'Список пользователей')]",
    )
    ERROR_SNACKBAR_NOT_ENOUGH_ENTRIES = (
        By.XPATH,
        "//div[contains(@class, 'Snackbar') and contains(text(), 'В списке недостаточно записей')]",
    )

    FIRST_AUDIENCE_ROW = (
        By.XPATH,
        "//div[@role='row' and contains(@class, 'BaseTable__row')]",
    )
    AUDIENCE_ROW_MENU_BUTTON = (By.CSS_SELECTOR, "[data-testid='audience-item-menu']")

    # Кнопка "Удалить" в контекстном меню
    AUDIENCE_MENU_DELETE_BUTTON = (
        By.XPATH,
        "//label//span[contains(@class,'vkuiActionSheetItem__children') and text()='Удалить']",
    )

    # Заголовок модального окна удаления
    DELETE_MODAL_TITLE = (By.XPATH, "//span[text()='Удалить аудиторию?']")

    # Кнопки в модалке
    MODAL_CANCEL_BUTTON_TEXT = (
        By.XPATH,
        "//button[@data-testid='cancel']//span[text()='Отменить']",
    )
    MODAL_SUBMIT_BUTTON_TEXT = (
        By.XPATH,
        "//button[@data-testid='submit']//span[text()='Удалить']",
    )

    EXCLUDE_CATEGORY_MY_AUDIENCES = (
        By.XPATH,
        "//span[contains(text(),'Мои аудитории')]",
    )
    EXCLUDE_CATEGORY_USER_REACTIONS = (
        By.XPATH,
        "//span[contains(text(),'По событиям или реакциям пользователей')]",
    )
    EXCLUDE_CATEGORY_INTERESTS = (By.XPATH, "//span[contains(text(),'По интересам')]")
    APP_CATEGORY_BUTTON = (By.CSS_SELECTOR, "[data-testid='appCategories']")
    ADDED_SOURCE_APP_CATEGORY = (
        By.XPATH,
        "//span[contains(text(), 'Категории мобильного приложения')]",
    )
    CREATED_AUDIENCE_NAME_TEMPLATE = lambda name: (
        By.XPATH,
        f"//span[contains(text(), '{name}')]",
    )
    DELETE_ICON = (
        By.XPATH,
        "//div[contains(@class, 'Header_buttons')]/*[local-name()='svg' and @aria-label='Delete']",
    )

    DELETE_CONFIRM_MODAL = (By.CSS_SELECTOR, '[data-testid="modal-confirm"]')

    USERS_LIST_BUTTON = (By.CSS_SELECTOR, "[data-testid='usersList']")
    TAB_UPLOAD_NEW = (By.ID, "tab-create-from-user-list-new")
    LIST_TYPE_COMBOBOX = (By.CSS_SELECTOR, "input[role='combobox']")
    FILE_UPLOAD_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    VALID_USERS_BLOCK = (By.CSS_SELECTOR, "[data-testid='valid']")
    INVALID_USERS_BLOCK = (By.CSS_SELECTOR, "[data-testid='invalid']")
    LIST_TYPE_COMBOBOX = (By.CSS_SELECTOR, "input[role='combobox']")


class AppCategoryLocators:
    PLATFORM_SELECTOR = (
        By.CSS_SELECTOR,
        "input[data-testid='sources.app_category.platform_selector']",
    )
    CATEGORY_SELECTOR = (
        By.CSS_SELECTOR,
        "input[data-testid='sources.app_category.category_selector']",
    )
    INSTALL_TYPE_SELECTOR = (
        By.CSS_SELECTOR,
        "input[data-testid='sources.app_category.install_type_selector']",
    )
