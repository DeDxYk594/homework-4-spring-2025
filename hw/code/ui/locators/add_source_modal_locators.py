from selenium.webdriver.common.by import By

class AddSourceModalLocator:
    HEADER = (By.CSS_SELECTOR, "[data-testid='modal-header']")
    ADD_EXISTING_AUDIENCE = (By.CSS_SELECTOR, "[data-testid='existsAudience']")
    ADD_USERS_LIST = (By.CSS_SELECTOR, "[data-testid='usersList']")
    ADD_VK_INTERACTIONS = (By.CSS_SELECTOR, "[data-testid='vkInteractions']")
    ADD_APP_EVENTS = (By.CSS_SELECTOR, "[data-testid='appEvents']")
    ADD_APP_CATEGORIES = (By.CSS_SELECTOR, "[data-testid='appCategories']")
    ADD_LEAD_FORM_EVENTS = (By.CSS_SELECTOR, "[data-testid='leadFormEvents']")
    ADD_PIXEL_EVENTS = (By.CSS_SELECTOR, "[data-testid='pixelEvents']")
    ADD_CONTEXT = (By.CSS_SELECTOR, "[data-testid='context']")
    ADD_APPS_AND_GROUPS = (By.CSS_SELECTOR, "[data-testid='appsAndGroups']")
    ADD_MUSICIANS = (By.CSS_SELECTOR, "[data-testid='musicians']")
    ADD_VK_APPS = (By.CSS_SELECTOR, "[data-testid='vkApps']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[data-testid='cancel']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[data-testid='submit']")
