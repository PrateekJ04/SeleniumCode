from selenium import webdriver
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.titles
@allure.title("Get title and price of the product")
@allure.description("Verify if product titles and price are fetched")
def test_ebay_product_title_and_price():
    l = []
    p = []
    # Use chrome options for running tests with specified browser requirement options
    otn = Options()
    otn.add_argument("--incognito")
    otn.add_argument("--start-maximized")
    # Invoke browser and provide the chrome options
    driver = webdriver.Chrome(options=otn)
    driver.implicitly_wait(10)
    driver.get("http://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    # Wait for browser to load URL
    driver.implicitly_wait(10)
    search_field = driver.find_element(By.XPATH, ".//input[@placeholder='Search for anything']")
    search_field.send_keys("macmini")
    search_btn = driver.find_element(By.XPATH, ".//input[@value='Search']")
    search_btn.click()
    driver.implicitly_wait(10)
    # Capture titles, price and store them in list
    list_of_products = driver.find_elements(By.XPATH, "(//span[@role='heading'])[position()>2]")

    list_of_price = driver.find_elements(By.XPATH, "(.//div/span[@class='s-item__price'] )[position()>2]")

    for i in list_of_products:
        l.append(i.text)
    for j in list_of_price:
        p.append(j.text)
    # Print titles and price
    print(l)
    print(p)
    # Convert the price values to float in order to get max and min price by list comprehention
    p_val = [val.replace('$', '').replace(' to ', ',') for val in p]
    p_val1 = [val1.split(',') for val1 in p_val]

    print(p_val1)
    new_list = [float(item) for sublist in p_val1 for item in sublist]
    print(new_list)

    max_pval = max(new_list)
    min_pval = min(new_list)

    print(f"Max value in price list is: {max_pval}")
    print(f"Min value in price list is: {min_pval}")

    print(len(l))
    print(len(new_list))
    #Use zip function to join two lists and show in dictionary format
    title_n_price=dict(zip(l,new_list))
    print(f"Title and Price of the products is : {title_n_price}")
    driver.quit()