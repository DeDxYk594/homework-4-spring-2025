from selenium.webdriver.common.by import By


class GroupCreationPageLocators:
    CONTINUE_BUTTON = (
        By.XPATH,
        "//span[@class='vkuiButton__in'][.//span[text()='Продолжить']]",
    )
    PREDICTION_AUDITORY = (
        By.XPATH,
        "//div[contains(@class, 'Prediction_itemAuditoryValue')]",
    )

    @staticmethod
    def select_city(city: str):
        return (By.XPATH, f"//span[@class='vkuiButton__content' and text()='{city}']")
