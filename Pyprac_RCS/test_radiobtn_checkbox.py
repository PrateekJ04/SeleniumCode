import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.rcbtn
@allure.title("Radio Button, Checkbox,Select Class")
@allure.description("Verify if radio button and check boxes are selected")
def test_radiobtn_checkbox_selectclass():
    optns = Options()
    optns.add_argument("--incognito")
    optns.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=optns)
    wait = WebDriverWait(driver, 10)
    driver.get(" https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.CSS_SELECTOR,"input[name='firstname']")
    first_name.send_keys("Brad")
    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name.send_keys("Pitt")

    # Select Gender equal to male
    male = driver.find_element(By.XPATH, ".//input[@value='Male']")
    wait.until(EC.visibility_of(male))
    male.click()
    assert male.is_selected()
    # Select years of experience equal to 3
    yoe3 = driver.find_element(By.XPATH, ".//input[@value='3']")
    wait.until(EC.visibility_of(yoe3))
    yoe3.click()
    assert yoe3.is_selected()
    # Select profession equal to Automation Tester
    professionAT = driver.find_element(By.XPATH, ".//input[@value='Automation Tester']")
    wait.until(EC.visibility_of(professionAT))
    professionAT.click()
    assert professionAT.is_selected()

    # Select continent equal to australia

    continent = driver.find_element(By.XPATH, ".//select[@id='continents']")
    wait.until(EC.visibility_of(continent))
    select = Select(continent)
    australia = select.select_by_visible_text("Australia")

    time.sleep(7)
    driver.quit()


@pytest.mark.Alert
@allure.title("Javascript Alert handle")
@allure.description("Verify if alert is handled properly")
def test_alert_functions():
    optns = Options()
    optns.add_argument("--incognito")
    optns.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=optns)
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click on JS alert
    js_alert = driver.find_element(By.XPATH, ".//li/button[contains(text(),'JS Alert')]")
    js_alert.click()
    driver.switch_to.alert.accept()
    text_validation1 = driver.find_element(By.XPATH, ".//p[contains(text(),'clicked an alert')]")
    wait.until(EC.visibility_of(text_validation1))
    assert text_validation1.text == "You successfully clicked an alert"

    # Click on JS Confirm
    js_alert1 = driver.find_element(By.XPATH, ".//li/button[contains(text(),'JS Confirm')]")
    js_alert1.click()
    driver.switch_to.alert.accept()
    text_validation2 = driver.find_element(By.XPATH, ".//p[contains(text(),'You clicked: Ok')]")
    wait.until(EC.visibility_of(text_validation2))
    assert text_validation2.text == "You clicked: Ok"

    # Click on JS Prompt
    js_alert3 = driver.find_element(By.XPATH, ".//li/button[contains(text(),'JS Prompt')]")
    js_alert3.click()
    alert = driver.switch_to.alert
    alert.send_keys("Clicked")
    alert.accept()
    text_validation3 = driver.find_element(By.XPATH, ".//p[contains(text(),'You entered:')]")
    wait.until(EC.visibility_of(text_validation3))
    assert text_validation3.text == "You entered: Clicked"

    time.sleep(7)
    driver.quit()
