from selenium.webdriver.common.by import By


class GroupEditingPageLocators:
    EDITABLE_TITLE_EDIT_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'EditableTitle_container')]/*[contains(@class, 'vkuiIcon--write_outline_20')]",
    )
    EDITABLE_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'EditableTitle_container')]/*[contains(@class, 'vkuiIcon--write_outline_20')]/parent::*/span[1]",
    )
    SAVE_BUTTON = (
        By.XPATH,
        "//span[contains(@class, 'vkuiButton__content') and text()='Сохранить']",
    )
