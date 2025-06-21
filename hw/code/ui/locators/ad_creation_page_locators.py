from selenium.webdriver.common.by import By


class AdCreationPageLocator:
    # Общие локаторы
    SITE_OPTION = (
        By.XPATH,
        "//span[text()='Сайт']/ancestor::div[contains(@class, 'Option_item__')]",
    )
    SITE_INPUT = (By.CSS_SELECTOR, "input[data-testid='site-select-input']")
    BUDGET_INPUT = (By.XPATH, "//input[@placeholder='Не задан' and @inputmode='decimal']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='next-step-button']")

    # Регион
    REGION_MOSCOW_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-testid='region-quick-selection-5506']",
    )

    # Заголовок генерация
    TITLE_GENERATE_ICON = (
        By.XPATH,
        "//button[contains(@class, 'ContentGeneratorButton_magicIconBtn')]",
    )
    GENERATED_TITLE_TEXTAREA = (By.CSS_SELECTOR, "textarea.vkuiTextarea__el")
    APPLY_GENERATED_TITLE_BUTTON = (By.XPATH, "//button[.//span[text()='Применить']]")

    # Редактирования объявления
    HEADER_INPUT = (
        By.XPATH,
        "//div[contains(@class, 'EditableTextField__wrapper')]"
        "/div[@contenteditable='true' and @data-testid='заголовок, макс. 40 символов']",
    )
    DESCRIPTION_INPUT = (
        By.XPATH,
        "//div[contains(@class, 'EditableTextField__wrapper')]"
        "/div[@contenteditable='true' and @data-testid='описание, макс. 90 символов']",
    )
    DESCRIPTION_BLOCK_ERROR = (
        By.XPATH,
        "//*[@data-name='textblock:::text_90']//*[@role='alert']",
    )
    TITLE_ERROR_MESSAGE = (
        By.XPATH,
        "//*[@data-name='textblock:::title_40']//*[@role='alert']",
    )

    # Превью
    PREVIEW_TITLE = (By.CSS_SELECTOR, "div[data-testid='ad-preview'] h3")
    PREVIEW_VIDEO = (By.CSS_SELECTOR, "div[data-testid='ad-preview'] video")
    PREVIEW_STREAM = (By.CSS_SELECTOR, "div[data-testid='ad-preview'] iframe")

    # Кнопка "Опубликовать"
    PUBLISH_BUTTON = (By.CSS_SELECTOR, "button[data-testid='submit-button']")

    # Кнопка выбора логотипа и изображения
    CHOOSE_LOGO_BUTTON = (By.CSS_SELECTOR, "button[data-testid='set-global-image']")
    PHOTO_STOCK_TAB = (By.CSS_SELECTOR, "div[data-id='photo_stock_and_generated']")
    GENERATED_LOGO_ITEM = (By.CSS_SELECTOR, "div[data-testid='image-media-item-loaded']")

    # Выбор изображений
    IMAGE_ITEM = (By.CSS_SELECTOR, "div[data-testid='image-item']")
    SECOND_MEDIA_OPTION_LOCATOR = (By.CSS_SELECTOR, "div[data-testid='image-item']")
    PHOTO_STOCK_IMAGE_LOCATOR = (By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc")

    # Выбор фото из генерации
    IMAGE_SELECT = (By.XPATH, "//div[contains(@class, 'ImageItem_image')]")

    # Кнопки редактирования изображений
    CHANGE_IMAGES_BUTTON = (
        By.XPATH,
        "//button[@data-testid='change-image' and contains(.//span, 'Заменить')]",
    )
    ADD_IMAGES_BUTTON = (
        By.XPATH,
        "//button[@data-testid='submit' and contains(.//span, 'Добавить')]",
    )
    SAVE_DRAFTS_BUTTON = (
        By.XPATH,
        "//button[.//span[contains(text(), 'Сохранить черновик')]]",
    )
    MEDIA_BUTTON = (
        By.XPATH,
        "//div[starts-with(@class, 'PhotoStockMediaFileSelector_section__')]",
    )



    def BUTTON_BY_TEXT(text: str):
        return By.XPATH, f"//button[.//span[text()='{text}']]"
