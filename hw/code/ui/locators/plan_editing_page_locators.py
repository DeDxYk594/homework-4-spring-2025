from selenium.webdriver.common.by import By


class PlanEditingPageLocators:
    GROUP_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'vkuiSimpleCell__before')]//*[contains(@class, 'vkuiIcon--square_4_outline_20')]",
    )
