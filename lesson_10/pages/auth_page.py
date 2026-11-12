from selenium.webdriver.common.by import By


class AuthPage:
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """
        Открывает страницу авторизации в браузере.

        :return: None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Вводит имя пользователя и пароль, затем нажимает кнопку входа.

        :param username: Имя пользователя (str).
        :param password: Пароль (str).
        :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
