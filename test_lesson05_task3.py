from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    # 1. Открываем страницу
    driver.get("https://httpbin.qa-territory.online/links/10")

    # 2. Находим все ссылки по тегу <a>
    links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверяем, что количество ссылок равно 9
    assert len(links) == 9

    # 4. Проверяем, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed()

    # 5. Проверяем, что текст первой ссылки содержит "1"
    assert "1" in links[0].text

    driver.quit()
