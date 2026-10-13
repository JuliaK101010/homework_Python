from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 55)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_input = wait.until(
        EC.visibility_of_element_located((By.ID, "delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    def click_button(xpath):
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        driver.execute_script("arguments[0].click();", btn)

    click_button("//span[text()='7']")
    click_button("//span[text()='+']")
    click_button("//span[text()='8']")
    click_button("//span[text()='=']")

    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    screen_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert screen_text == "15", (
        f"Ожидался результат 15, но получено: {screen_text}"
    )

    driver.quit()
