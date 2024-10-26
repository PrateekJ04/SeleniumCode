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
