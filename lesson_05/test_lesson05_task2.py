from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    # 1. Открываем страницу
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # 2 и 3. Находим поле custname и вводим имя
    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Иван")

    # 4. Находим кнопку Submit и нажимаем
    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]"
    )
    submit_button.click()

    # 5. Проверяем, что URL изменился
    target_url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url != target_url

    driver.quit()
