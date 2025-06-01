from selenium.webdriver.common.by import By


class GroupEditingPageLocators:
    EDITABLE_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'EditableTitle_container')]/*[contains(@class, 'vkuiIcon--write_outline_20')]",
    )
    SAVE_BUTTON = (
        By.XPATH,
        "//span[contains(@class, 'vkuiButton__content') and text()='Сохранить']",
    )
