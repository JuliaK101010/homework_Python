from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from selenium import webdriver


def test_shop_purchase():
    driver = webdriver.Firefox()

    try:
        # 1 & 2. Открываем сайт и авторизуемся
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.login("standard_user", "secret_sauce")

        # 3. Добавляем товары в корзину
        products_page = ProductsPage(driver)
        products_page.add_items_to_cart()

        # 4. Переходим в корзину
        products_page.go_to_cart()

        # 5. Нажимаем Checkout
        cart_page = CartPage(driver)
        cart_page.go_to_checkout()

        # 6 & 7. Заполняем форму и нажимаем Continue
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_personal_info("Julia", "Coco", "123456")

        # 8. Читаем итоговую стоимость
        total_text = checkout_page.get_total_cost()

        # 9. Закрываем браузер перед проверкой
        driver.quit()

        # 10. Проверяем через assert, что сумма равна $58.29
        assert "58.29" in total_text, (
            f"Ожидалась сумма $58.29, но получено: '{total_text}'"
        )

    finally:
        # закрытие драйвера
        try:
            driver.quit()
        except Exception:
            pass
