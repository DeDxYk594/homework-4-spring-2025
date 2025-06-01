from ..utils import Locator
from selenium.webdriver.common.by import By

class EntityDashboardPageLocator:
    PLAN_ROW=(By.XPATH, "//*[contains(concat(' ', @class, ' '), 'Actions_wrapper__')]")
