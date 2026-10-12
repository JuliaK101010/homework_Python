from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Открываем страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Находим и нажимаем на кнопку "Start" по CSS-селектору
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    # 3. Дожидаемся появления элемента с текстом "Hello World!"
    finish_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Делаем скриншот страницы
    driver.save_screenshot("screenshot.png")

    # 5. Проверяем, что появившийся текст равен "Hello World!"
    assert finish_element.text == "Hello World!"

    driver.quit()
