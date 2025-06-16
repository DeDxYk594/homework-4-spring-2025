from selenium.webdriver.common.by import By


class AdCreationPageLocator:
    TITLE_INPUT = (By.CSS_SELECTOR, "input.vkuiInput__el")
    SITE_OPTION = (
        By.XPATH,
        "//span[text()='Сайт']/ancestor::div[contains(@class, 'Option_item__')]",
    )

    SITE_INPUT = (By.CSS_SELECTOR, "input[data-testid='site-select-input']")

    BUDGET_INPUT = (By.XPATH, "//input[@inputmode='decimal']")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='next-step-button']")

    AD_PLACEMENT_BUTTONS = (
        By.CSS_SELECTOR,
        "button[data-testid='ad-placement-button']",
    )

    PREVIEW_TITLE = (By.XPATH, "//h3[contains(@class, 'Header_name')]")

    TITLE_ERROR_MESSAGE = (By.XPATH, "//ul[contains(@class, 'TextErrors_errorsList')]")

    PREVIEW_VIDEO = (
        By.XPATH,
        "//section[contains(@class, 'VerticalVideoPreview_container')]",
    )

    PREVIEW_STREAM = (
        By.XPATH,
        "//section[contains(@class, 'PreviewInStream_section')]",
    )

    REGION_MOSCOW_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-testid='region-quick-selection-5506']",
    )

    TITLE_GENERATE_ICON = (
        By.XPATH,
        "//button[contains(@class, 'ContentGeneratorButton_magicIconBtn')]",
    )

    GENERATED_TITLE_TEXTAREA = (By.CSS_SELECTOR, "textarea.vkuiTextarea__el")

    APPLY_GENERATED_TITLE_BUTTON = (By.XPATH, "//button[.//span[text()='Применить']]")

    LOGO_SELECT = (
        By.XPATH,
        "//span[@class='vkuiButton__content'][.//span[contains(@class, 'UploadMediaButton_buttonLogoTitle') and text()='Выбрать логотип']]",
    )
    IMAGE_SELECT = (
        By.XPATH,
        "//div[@data-testid='image-media-item-loaded']",
    )
    MEDIA_BUTTON = (
        By.XPATH,
        "//div[@data-testid='open-media-library-button' and contains(.//span, 'Медиатека')]",
    )
    ADD_IMAGES_BUTTON = (
        By.XPATH,
        "//button[@data-testid='submit' and contains(.//span, 'Добавить')]",
    )
    CHANGE_IMAGES_BUTTON = (
        By.XPATH,
        "//button[@data-testid='change-image' and contains(.//span, 'Заменить')]",
    )
    SAVE_DRAFTS_BUTTON = (
        By.XPATH,
        "//button[.//span[contains(text(), 'Сохранить черновик')]]",
    )
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
    IMAGES_SELECT = (
        By.XPATH,
        "div[contains(@class, 'ImageItem_image') and contains(@style, 'background-image: url')]",
    )
    TO_PUBLISH_BUTTON = (
        By.XPATH,
        "//span[@class='vkuiButton__in'][.//span[@class='vkuiButton__content' and text()='Опубликовать']]",
    )
