from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_checkout(self) -> None:
        """
        Ожидает кликабельности кнопки оформления
        заказа (Checkout) и нажимает её.

        :return: None
        """
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
