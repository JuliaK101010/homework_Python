import allure
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from selenium import webdriver


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Оформление заказа")
@allure.title("Тест покупки товаров в магазине")
@allure.description(
    "Проверка полного цикла покупки товаров "
    "с использованием паттерна Page Object."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase():
    driver = webdriver.Firefox()

    try:
        with allure.step("Открываем сайт и выполняем авторизацию"):
            auth_page = AuthPage(driver)
            auth_page.open()
            auth_page.login("standard_user", "secret_sauce")

        with allure.step("Добавляем товары в корзину"):
            products_page = ProductsPage(driver)
            products_page.add_items_to_cart()

        with allure.step("Переходим в корзину"):
            products_page.go_to_cart()

        with allure.step("Переходим к оформлению заказа (Checkout)"):
            cart_page = CartPage(driver)
            cart_page.go_to_checkout()

        with allure.step("Заполняем персональные данные и продолжаем"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_personal_info("Julia", "Coco", "123456")

        with allure.step("Получаем итоговую стоимость заказа"):
            total_text = checkout_page.get_total_cost()

        with allure.step("Закрываем браузер перед проверкой"):
            driver.quit()

        with allure.step("Проверяем, что сумма заказа равна $58.29"):
            assert "58.29" in total_text, (
                f"Ожидалась сумма $58.29, но получено: '{total_text}'"
            )

    finally:
        try:
            driver.quit()
        except Exception:
            pass
