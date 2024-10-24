import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.signin
@allure.title("Error message validation in VWO log in page ")
@allure.description("Verify if proper error message is displayed in Vwo login page when entered invalid creds")
def test_vwo_login_with_invalid_creds():
    optns = Options()
    driver = webdriver.Chrome(options=optns)
    wait = WebDriverWait(driver, 10)
    optns.add_argument("--incognito")
    optns.add_argument('--start-maximized')

    driver.maximize_window()

    driver.get("https://app.vwo.com/")
    username = driver.find_element(By.NAME, "username")
    username.send_keys("xyzabc@test.com")
    wait.until(EC.visibility_of(username))
    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys("test123")
    wait.until(EC.visibility_of(passwd))
    signin_btn = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    signin_btn.click()

    alert_message = driver.find_element(By.ID, "js-notification-box-msg")
    wait.until(EC.visibility_of(alert_message))
    message = alert_message.text
    print(message)
    assert message.__eq__("Your email, password, IP address or location did not match")
    driver.quit()
