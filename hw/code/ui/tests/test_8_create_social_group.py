import time
import pytest
import os
from pathlib import Path
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ..pages.audience_page import AudiencePage
from ..locators.audience_page_locators import AudiencePageLocator
from ..locators.audience_page_locators import AppCategoryLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from ..constants import *


# Проверка заглушки "Аудитории" если аудитоии еще не создавались
def test_audience_landing_page(driver):
    driver.get("https://ads.vk.com/hq/audience")
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    stub = wait.until(
        EC.presence_of_element_located(AudiencePageLocator.STUB_NO_AUDIENCES_TEXT)
    )
    assert stub.is_displayed()

    create_btn = driver.find_element(*AudiencePageLocator.CREATE_AUDIENCE_BUTTON)
    assert create_btn.is_displayed()

    more_menu = driver.find_element(*AudiencePageLocator.MORE_MENU_BUTTON)
    assert more_menu.is_displayed()

    help_link = driver.find_element(*AudiencePageLocator.HELP_LINK)
    assert help_link.is_displayed()


def test_create_audience_with_social_group(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    page.enter_audience_name(DEFAULT_AUDIENCE_NAME)
    page.click_add_source()

    page.click_social_group_button()
    page.search_group(DEFAULT_GROUP_NAME)
    page.click_first_group_result()
    page.select_first_group_item()
    page.click_communities_header()
    print("Нажимаем Сохранить")
    page.click_save_button()
    page.click_save_button()  # сохранение на втором экране


# Проверка появления формы создания
def test_open_create_form(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    # Поле названия
    input_field = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.AUDIENCE_NAME_INPUT)
    )
    assert input_field.is_displayed()

    # Кнопка добавления источников
    add_source_btn = driver.find_element(*AudiencePageLocator.ADD_SOURCE_BUTTON)
    assert add_source_btn.is_displayed()


# Проверка длины названия (до 255 символов)
def test_valid_name_input(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    valid_name = "A" * 255
    page.enter_audience_name(valid_name)

    input_field = driver.find_element(*AudiencePageLocator.AUDIENCE_NAME_INPUT)
    assert input_field.get_attribute("value") == valid_name


# Название пустое — кнопка "Сохранить" неактивна
def test_empty_name_disables_save(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    # Ждём появления поля
    name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.AUDIENCE_NAME_INPUT)
    )
    name_input.clear()

    # Ждём появления кнопок
    visible_buttons = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        lambda d: [
            btn
            for btn in d.find_elements(*AudiencePageLocator.SAVE_BUTTON)
            if btn.is_displayed()
        ]
    )

    assert visible_buttons, "Кнопка 'Сохранить' не найдена"

    save_btn = visible_buttons[0]

    assert (
        not save_btn.is_enabled()
    ), "Кнопка 'Сохранить' должна быть недоступна при пустом имени"


# Название длиннее 255 символов → ошибка
def test_name_too_long_shows_error(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    too_long_name = "A" * 256
    page.enter_audience_name(too_long_name)

    assert (
        page.is_name_length_error_visible()
    ), "Ошибка с максимальной длиной имени не появилась"


# Сохранение без источников → предупреждение
def test_save_without_sources_button_disabled(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Аудитория без источников")

    save_buttons = driver.find_elements(*AudiencePageLocator.SAVE_BUTTON)

    # Проверяем, что хотя бы одна из них отключена
    assert any(
        not btn.is_enabled() for btn in save_buttons
    ), "Ожидается, что кнопка 'Сохранить' будет отключена без источников"


# "Отмена" возвращает назад
def test_cancel_button_returns(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()

    cancel_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.MODAL_CANCEL_BUTTON)
    )
    cancel_button.click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.invisibility_of_element_located(AudiencePageLocator.CREATE_AUDIENCE_FORM)
    )

    WebDriverWait(driver, DEFAULT_TIMEOUT).until_not(
        EC.presence_of_element_located(AudiencePageLocator.MODAL_ROOT)
    )


# Диалог подтверждения при закрытии несохранённых данных
def test_unsaved_changes_confirmation_with_escape(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Черновик")

    driver.switch_to.active_element.send_keys(Keys.ESCAPE)

    confirm_popup = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.UNSAVED_CHANGES_MODAL)
    )
    assert confirm_popup.is_displayed()


# исключение источника
def test_exclude_source_menu_opens(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.click_exclude_source()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(
            AudiencePageLocator.EXCLUDE_CATEGORY_MY_AUDIENCES
        )
    )
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(
            AudiencePageLocator.EXCLUDE_CATEGORY_USER_REACTIONS
        )
    )
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.EXCLUDE_CATEGORY_INTERESTS)
    )


# Обновление списка предлагаемых источников
def test_added_source_disappears_from_list(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name("Test исключение источника")

    page.click_add_source()
    page.click_social_group_button()
    page.search_group(DEFAULT_GROUP_NAME)
    page.click_first_group_result()
    page.select_first_group_item()
    page.click_communities_header()
    page.click_save_button()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.ADD_SOURCE_BUTTON)
    )

    page.click_add_source()

    # Убеждаемся, что "Подписчики сообществ" больше нет
    WebDriverWait(driver, SHORT_TIMEOUT).until_not(
        EC.presence_of_element_located(AudiencePageLocator.SOCIAL_GROUP_BUTTON)
    )


# #Категории мобильного приложения
def test_add_app_category_source(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    audience_name = APP_CATEGORY_AUDIENCE_NAME
    page.enter_audience_name(audience_name)

    page.click_add_source()
    page.click_app_category_button()

    # Платформа
    platform_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AppCategoryLocators.PLATFORM_SELECTOR)
    )
    platform_input.click()
    platform = "iOS"
    platform_input.send_keys(platform)
    platform_input.send_keys(Keys.ENTER)

    # Категория
    category_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(AppCategoryLocators.CATEGORY_SELECTOR)
    )
    driver.execute_script("arguments[0].click();", category_input)
    category_input.send_keys(Keys.ARROW_DOWN)
    category_input.send_keys(Keys.ENTER)

    install_type_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AppCategoryLocators.INSTALL_TYPE_SELECTOR)
    )
    install_type_input.click()
    install_type_input.send_keys(Keys.ARROW_DOWN)
    install_type_input.send_keys(Keys.ENTER)

    page.click_save_button()
    page.click_save_button()

    added_source = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(AudiencePageLocator.ADDED_SOURCE_APP_CATEGORY)
    )
    assert (
        added_source.is_displayed()
    ), "Источник с категориями мобильного приложения не отображается"

    created_audience = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            AudiencePageLocator.CREATED_AUDIENCE_NAME_TEMPLATE(audience_name)
        )
    )
    assert created_audience.is_displayed(), "Созданная аудитория не появилась в списке"


# Добавление аудитории по подписчикам сообществ
def test_add_social_group_source(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)
    page.click_create_audience()
    page.enter_audience_name(DEFAULT_AUDIENCE_NAME)
    page.click_add_source()
    page.click_social_group_button()
    page.search_group(DEFAULT_GROUP_NAME)
    page.click_first_group_result()
    page.select_first_group_item()
    page.click_communities_header()

    page.click_save_button()

    icons = driver.find_elements(*AudiencePageLocator.DELETE_ICON)
    delete_icon = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.DELETE_ICON)
    )
    assert delete_icon.is_displayed(), "Иконка удаления не видна"

    ActionChains(driver).move_to_element(delete_icon).click().perform()

    confirmation_modal = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.DELETE_CONFIRM_MODAL)
    )
    assert (
        confirmation_modal.is_displayed()
    ), "Модальное окно подтверждения удаления не появилось"


# Источник Список пользователей из файла
def test_upload_user_list_file(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)

    audience_name = USER_LIST_AUDIENCE_NAME
    page.click_create_audience()
    page.enter_audience_name(audience_name)

    page.click_add_source()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.USERS_LIST_BUTTON)
    ).click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.TAB_UPLOAD_NEW)
    ).click()

    combobox = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.LIST_TYPE_COMBOBOX)
    )
    combobox.click()

    vk_option = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.VK_ID_OPTION)
    )
    vk_option.click()

    file_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(AudiencePageLocator.FILE_UPLOAD_INPUT)
    )
    abs_path = Path.cwd() / "extra files" / DEFAULT_VALID_USER_FILE
    file_input.send_keys(str(abs_path))

    page.click_save_button()

    source_selector = (
        By.XPATH,
        "//span[@data-testid='header' and contains(text(), 'Список пользователей')]",
    )
    source_element = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.SOURCE_USERS_LIST_HEADER)
    )
    assert (
        source_element.is_displayed()
    ), "Источник 'Список пользователей' не появился после загрузки файла"


# Проверка появления уведомления о том, что в загружаемом списке недостаточно записей
def test_upload_empty_user_list_file(driver):
    driver.get("https://ads.vk.com/hq/audience")
    page = AudiencePage(driver)

    audience_name = EMPTY_USER_LIST_AUDIENCE_NAME
    page.click_create_audience()
    page.enter_audience_name(audience_name)
    page.click_add_source()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.USERS_LIST_BUTTON)
    ).click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.TAB_UPLOAD_NEW)
    ).click()

    combobox = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.LIST_TYPE_COMBOBOX)
    )
    combobox.click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.VK_ID_OPTION)
    ).click()

    file_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(AudiencePageLocator.FILE_UPLOAD_INPUT)
    )
    abs_path = Path.cwd() / "extra files" / DEFAULT_EMPTY_USER_FILE
    file_input.send_keys(str(abs_path))

    page.click_save_button()

    error_element = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(
            AudiencePageLocator.ERROR_SNACKBAR_NOT_ENOUGH_ENTRIES
        )
    )
    assert (
        error_element.is_displayed()
    ), "Оповещение о недостаточности записей не появилось"

    WebDriverWait(driver, DEFAULT_TIMEOUT).until_not(
        EC.visibility_of_element_located(
            AudiencePageLocator.ERROR_SNACKBAR_NOT_ENOUGH_ENTRIES
        )
    )


# Существуют кнопки "Редактировать", "Настроить доступ", "Удалить"
def test_audience_list_has_rows_and_menu(driver):
    driver.get("https://ads.vk.com/hq/audience")

    first_row = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.FIRST_AUDIENCE_ROW)
    )
    ActionChains(driver).move_to_element(first_row).perform()

    menu_button = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.AUDIENCE_ROW_MENU_BUTTON)
    )
    menu_button.click()

    menu_labels = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.presence_of_all_elements_located(
            (
                By.XPATH,
                "//label//span[contains(@class, 'vkuiActionSheetItem__children')]",
            )
        )
    )
    item_texts = [item.text.strip() for item in menu_labels if item.text.strip()]

    expected_items = {"Редактировать", "Настроить доступ", "Удалить"}
    assert expected_items.issubset(
        set(item_texts)
    ), f"Не найдены все ожидаемые пункты: {item_texts}"


# Предупреждение перед удалением аудитории
def test_delete_audience_modal_appears(driver):
    driver.get("https://ads.vk.com/hq/audience")

    first_row = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.FIRST_AUDIENCE_ROW)
    )
    ActionChains(driver).move_to_element(first_row).perform()

    menu_button = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.AUDIENCE_ROW_MENU_BUTTON)
    )
    menu_button.click()

    delete_button = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.AUDIENCE_MENU_DELETE_BUTTON)
    )
    delete_button.click()

    modal_title = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.visibility_of_element_located(AudiencePageLocator.DELETE_MODAL_TITLE)
    )
    assert modal_title.is_displayed(), "Модальное окно не появилось"

    cancel_button = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.MODAL_CANCEL_BUTTON_TEXT)
    )
    delete_confirm_button = WebDriverWait(driver, SHORT_TIMEOUT).until(
        EC.element_to_be_clickable(AudiencePageLocator.MODAL_SUBMIT_BUTTON_TEXT)
    )

    assert cancel_button.is_displayed(), "Кнопка 'Отменить' не найдена"
    assert delete_confirm_button.is_displayed(), "Кнопка 'Удалить' не найдена"

    cancel_button.click()
