from selenium.webdriver.common.by import By


class PlanEditingPageLocators:
    GROUP_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSimpleCell__before')]//svg[contains(@class, 'vkuiIcon--square_4_outline_20')]/parent::",
    )
