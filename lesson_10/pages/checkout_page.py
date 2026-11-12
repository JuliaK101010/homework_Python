from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет персональные данные покупателя и нажимает кнопку продолжения.

        :param first_name: Имя покупателя (str).
        :param last_name: Фамилия покупателя (str).
        :param postal_code: Почтовый индекс (str).
        :return: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_cost(self) -> str:
        """
        Получает и возвращает итоговую сумму заказа со страницы подтверждения.

        :return: Текст с итоговой стоимостью (str).
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text
