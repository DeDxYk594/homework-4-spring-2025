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
    CREATE_BUTTON = (
    By.XPATH,
    "//*[contains(concat(' ', @class, ' '), ' vkuiButton__content ') and text()='Создать']"
    )
    SITE_SELECT = (
        By.XPATH, "//div[@data-id='site_conversions']"
    )
    SITE_URL_INPUT = (
        By.XPATH, 
        "//input[@data-testid='site-select-input']"
    )
    OFFER_DESCRIPTION_TEXTAREA = (
        By.XPATH,
        "//textarea[contains(@class, 'vkuiTextarea__el') and @placeholder='Опишите ваше предложение']"
    )
    PRICED_GOAL_INPUT = (
        By.XPATH,
        "//input[@data-testid='priced-goal']"
    )
    AUTOBIDDING_MODE_INPUT = (
        By.XPATH,
        "//input[@data-testid='autobidding-mode']"
    )
    TARGETING_INPUT = (
        By.XPATH,
        "//input[@data-testid='targeting-not-set']"
    )
    BUDGET_INPUT = (
        By.XPATH,
        "//input[@data-testid='budget']"
    )
    END_DATE_INPUT = (
        By.XPATH,
        "//span[@data-testid='end-date']"
    )
    CALENDAR_BUTTON = (
        By.XPATH,
        "//button[.//*[contains(@class, 'vkuiIcon--calendar_outline_20')]]"
    )
