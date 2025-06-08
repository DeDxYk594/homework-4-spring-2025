from selenium.webdriver.common.by import By

class AdCreationPageLocator:
    EDIT_ICON = (By.CSS_SELECTOR, ".EditableTitle_editIcon__shXc4") 
    TITLE_INPUT = (By.CSS_SELECTOR, "input.vkuiInput__el")          
    SITE_OPTION = (By.XPATH, "//span[text()='Сайт']/ancestor::div[contains(@class, 'Option_item__')]")

    SITE_INPUT = (By.CSS_SELECTOR, "input[data-testid='site-select-input']")

    BUDGET_INPUT = (By.XPATH, "//input[@inputmode='decimal']")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='next-step-button']")

    REGION_MOSCOW_BUTTON = (By.CSS_SELECTOR, "button[data-testid='region-quick-selection-5506']")

    TITLE_GENERATE_ICON = (By.CSS_SELECTOR, "button.ContentGeneratorButton_magicIconBtn__UsRGX")

    GENERATED_TITLE_TEXTAREA = (By.CSS_SELECTOR, "textarea.vkuiTextarea__el")

    APPLY_GENERATED_TITLE_BUTTON = (By.XPATH, "//button[.//span[text()='Применить']]")
