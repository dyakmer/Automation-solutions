from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button_exists(browser):
    # Задаем URL страницы товара
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # Открываем страницу товара
    browser.get(product_url)

    # Используем явное ожидание для поиска кнопки добавления в корзину
    add_to_cart_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )

    assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не найдена"
