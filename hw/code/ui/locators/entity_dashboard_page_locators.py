from selenium.webdriver.common.by import By


class EntityDashboardPageLocator:
    PLAN_ROW = (
        By.XPATH,
        "//*[contains(concat(' ', @class, ' '), 'Actions_wrapper__')]",
    )
    EDIT_BUTTON = (
        By.XPATH,
        "//*[contains(concat(' ', @class, ' '), 'vkuiIcon--write_outline_20')]",
    )
