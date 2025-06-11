import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ..pages.audience_page import AudiencePage
from ..locators.audience_page_locators import AudiencePageLocator 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#Проверка заглушки "Аудитории" если аудитоии еще не создавались
def test_audience_landing_page(driver):
    driver.get("https://ads.vk.com/hq/audience")
    wait = WebDriverWait(driver, 10)

    # Проверка заглушки: "Аудиторий пока нет"
    stub = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(), 'Аудиторий пока нет')]")
    ))
    assert stub.is_displayed()

    # Проверка кнопки "Создать аудиторию"
    create_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid='create-audience']")
    assert create_btn.is_displayed()

    # Проверка кнопки дополнительных действий (три точки)
    more_menu = driver.find_element(By.CSS_SELECTOR, "[data-testid='other-buttons']")
    assert more_menu.is_displayed()

    # Проверка справочной ссылки
    help_link = driver.find_element(By.XPATH, "//a[contains(@href, '/help/features/audiences_lists/audiences')]")
    assert help_link.is_displayed()


def test_create_audience_with_social_group(driver): 
    driver.get("https://ads.vk.com/hq/audience")  
    page = AudiencePage(driver)
    page.click_create_audience()

    page.enter_audience_name("Новая аудитория РИА")
    page.click_add_source()

    page.click_social_group_button()   
    page.search_group("РИА новости")
    page.click_first_group_result()
    page.select_first_group_item()
    page.click_communities_header()
    print("Нажимаем Сохранить")
    page.click_save_button()
    page.click_save_button()  # сохранение на втором экране

    # sleep(10)


#Проверка появления формы создания
def test_open_create_form(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    # Поле названия
    input_field = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(AudiencePageLocator.AUDIENCE_NAME_INPUT)
    )
    assert input_field.is_displayed()

    # Кнопка добавления источников
    add_source_btn = driver.find_element(*AudiencePageLocator.ADD_SOURCE_BUTTON)
    assert add_source_btn.is_displayed()

#Проверка длины названия (до 255 символов)
def test_valid_name_input(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    valid_name = "A" * 255
    page.enter_audience_name(valid_name)

    input_field = driver.find_element(*AudiencePageLocator.AUDIENCE_NAME_INPUT)
    assert input_field.get_attribute("value") == valid_name


#Название пустое — кнопка "Сохранить" неактивна
def test_empty_name_disables_save(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    # Ждём появления поля
    name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AudiencePageLocator.AUDIENCE_NAME_INPUT)
    )
    name_input.clear()

    # Ждём появления кнопок
    visible_buttons = WebDriverWait(driver, 10).until(
        lambda d: [btn for btn in d.find_elements(*AudiencePageLocator.SAVE_BUTTON) if btn.is_displayed()]
    )

    assert visible_buttons, "Кнопка 'Сохранить' не найдена"

    save_btn = visible_buttons[0]

    is_disabled = (
        not save_btn.is_enabled()
        or save_btn.get_attribute("aria-disabled") == "true"
        or "vkuiButton--state-disabled" in save_btn.get_attribute("class")
    )

    assert is_disabled, "Ожидается, что кнопка 'Сохранить' будет отключена при пустом имени"

#Название длиннее 255 символов → ошибка
def test_name_too_long_shows_error(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    too_long_name = "A" * 256
    page.enter_audience_name(too_long_name)

    try:
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'не больше 255 символов')]")
            )
        )
        assert error.is_displayed(), "Сообщение об ошибке не отображается"
    except TimeoutException:
        raise AssertionError("Ошибка с максимальной длиной имени не появилась")


# Сохранение без источников → предупреждение
def test_save_without_sources_button_disabled(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Аудитория без источников")

    # Ищем кнопку "Сохранить"
    save_buttons = driver.find_elements(*AudiencePageLocator.SAVE_BUTTON)

    # Проверяем, что хотя бы одна из них отключена
    assert any(not btn.is_enabled() for btn in save_buttons), "Ожидается, что кнопка 'Сохранить' будет отключена без источников"



#"Отмена" возвращает назад
def test_cancel_button_returns(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    # Клик по "Отмена"
    cancel_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='cancel']"))
    )
    cancel_button.click()

    # Проверяем, что форма действительно исчезла
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-testid='create-audience-form']"))
    )

    # Альтернативно: просто подождать исчезновение любой модалки
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "vkuiModalRoot"))
    )




#Диалог подтверждения при закрытии несохранённых данных
def test_unsaved_changes_confirmation_with_escape(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Черновик")

    # Отправляем Escape на активный элемент (или на <body>)
    driver.switch_to.active_element.send_keys(Keys.ESCAPE)

    # Проверяем, что появилось предупреждение
    confirm_popup = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@data-testid, 'modal-confirm')]//span[contains(text(), 'Прервать создание?')]"
        ))
    )
    assert confirm_popup.is_displayed()


#исключение источника
def test_exclude_source_menu_opens(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    # Нажать "Исключить источник"
    page.click_exclude_source()

    # Проверка наличия категорий
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Мои аудитории')]"))
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'По событиям или реакциям пользователей')]"))
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'По интересам')]"))
    )



#Обновление списка предлагаемых источников
def test_added_source_disappears_from_list(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Test исключение источника")

    page.click_add_source()
    page.click_social_group_button()
    page.search_group("РИА новости")
    page.click_first_group_result()
    page.select_first_group_item()
    page.click_communities_header()
    page.click_save_button()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AudiencePageLocator.ADD_SOURCE_BUTTON)
    )

    page.click_add_source()

    # Убеждаемся, что "Подписчики сообществ" больше нет
    WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located(AudiencePageLocator.SOCIAL_GROUP_BUTTON)
    )




#Категории мобильного приложения
def test_add_app_category_source(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Аудитория с категориями приложений")

    page.click_add_source()
    page.click_app_category_button()

    # Платформа
    platform_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='sources.app_category.platform_selector']"))
    )
    platform_input.click()
    platform_input.send_keys("iOS")
    platform_input.send_keys(Keys.ENTER)

    # Категория
    category_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='sources.app_category.category_selector']"))
    )
    driver.execute_script("arguments[0].click();", category_input)
    category_input.send_keys(Keys.ARROW_DOWN)
    category_input.send_keys(Keys.ENTER)

    install_type_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='sources.app_category.install_type_selector']"))
    )
    install_type_input.click()
    install_type_input.send_keys(Keys.ARROW_DOWN)
    install_type_input.send_keys(Keys.ENTER)


    page.click_save_button()

    page.click_save_button()


def test_add_app_category_source(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Новая аудитория РИА")
    page.click_add_source()
    page.click_social_group_button()
    page.search_group("РИА новости")
    page.click_first_group_result()
    page.select_first_group_item()
    page.click_communities_header()

    print("Нажимаем Сохранить")
    page.click_save_button()

    delete_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "svg.Header_delete__oUhre"))
    )

    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.Header_delete__oUhre"))
    )

    delete_icon.click()

    confirmation_modal = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='modal-confirm']"))
    )
    assert confirmation_modal.is_displayed(), "Модальное окно подтверждения удаления не появилось"
