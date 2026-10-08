from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открываем главную страницу
    driver.get("https://httpbin.qa-territory.online")

    # 2. Находим и кликаем на ссылку HTML Form
    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    # 3. Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # 4. Возвращаемся назад на главную страницу
    driver.back()

    # 5. Проверяем, что вернулись на исходный URL
    expected_url = "https://httpbin.qa-territory.online"
    assert driver.current_url.rstrip("/") == expected_url

    driver.quit()
