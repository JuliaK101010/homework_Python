from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Открываем страницу gitflic.ru
    driver.get("https://gitflic.ru/")

    # 2. Устанавливаем cookie для первого пользователя (User 1)
    cookie_user1 = {
        "name": "SESSION",
        "value": "YzhhYmIxNjctNTgyOC00YTFkLTk0YjEtODVlYTQ3YmFmNWM2",
        "domain": "gitflic.ru",
    }
    driver.add_cookie(cookie_user1)

    # 3. Обновляем страницу
    driver.refresh()

    # 4. Переходим на страницу профиля пользователя 1
    driver.get("https://gitflic.ru/user/jules")

    # 5. Сохраняем текущий URL
    url_user1 = driver.current_url

    # 6. Разлогиниваемся (очищаем куки)
    driver.delete_all_cookies()

    # 7. Устанавливаем cookie для второго пользователя (User 2)
    cookie_user2 = {
        "name": "SESSION",
        "value": "NWVlZmNkNmQtZjc1OS00NmJmLThhMDItMWE3NmI5NjliOWI2",
        "domain": "gitflic.ru",
    }
    driver.add_cookie(cookie_user2)

    # 8. Обновляем страницу
    driver.refresh()

    # 9. Переходим на страницу профиля пользователя 2
    driver.get("https://gitflic.ru/user/julia101010")

    # 10. Сохраняем текущий URL
    url_user2 = driver.current_url

    # 11. Проверяем, что URL для пользователей различаются
    assert url_user1 != url_user2, (
        "URL пользователей совпадают, сессия не сменилась!"
    )

    driver.quit()
