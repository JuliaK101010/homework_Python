from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        """
        Инициализация страницы с товарами.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def add_items_to_cart(self) -> None:
        """
        Добавляет несколько выбранных товаров в корзину.

        :return: None
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину интернет-магазина.

        :return: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
