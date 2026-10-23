from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()

    try:
        # Инициализируем Page Object
        calc_page = CalculatorPage(driver)

        # 1. Открываем страницу
        calc_page.open()

        # 2. Вводим значение 45 в поле задержки
        calc_page.set_delay("45")

        # 3. Нажимаем кнопки: 7, +, 8, =
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

        # 4. Получаем результат и проверяем через assert
        result = calc_page.get_result()
        assert result == "15", f"Ожидался результат 15, но получено: {result}"

    finally:
        driver.quit()
