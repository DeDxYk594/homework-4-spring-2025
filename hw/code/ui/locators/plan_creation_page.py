from selenium.webdriver.common.by import By

class PlanCreationPageLocator:
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
    DAY_SELECT = (
        By.XPATH,
        "//div[contains(@class, 'vkuiCalendarDay__inner')][.//span[@aria-hidden='true' and text()='19']]"
    )
