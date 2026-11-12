import allure
from calculator_page import CalculatorPage
from selenium import webdriver


@allure.feature("Медленный калькулятор")
@allure.story("Арифметические операции")
@allure.title("Тест сложения на калькуляторе с задержкой")
@allure.description(
    "Проверка корректности сложения 7 + 8 "
    "с учетом заданной задержки ожидания результата."
)
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator():
    driver = webdriver.Chrome()

    try:
        with allure.step("Инициализация Page Object калькулятора"):
            calc_page = CalculatorPage(driver)

        with allure.step("Открываем страницу калькулятора"):
            calc_page.open()

        with allure.step("Вводим значение задержки (45 секунд)"):
            calc_page.set_delay("45")

        with allure.step("Нажимаем последовательно кнопки: 7, +, 8, ="):
            calc_page.click_button("7")
            calc_page.click_button("+")
            calc_page.click_button("8")
            calc_page.click_button("=")

        with allure.step("Получаем результат вычислений"):
            result = calc_page.get_result()

        with allure.step("Закрываем браузер перед проверкой"):
            driver.quit()

        with allure.step("Проверяем через assert, что результат равен 15"):
            assert result == "15", (
                f"Ожидался результат 15, но получено: {result}"
            )

    finally:
        try:
            driver.quit()
        except Exception:
            pass
