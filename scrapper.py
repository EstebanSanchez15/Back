from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import requests

driver = webdriver.Firefox()

async def Scrapp(url):
    checks = []
    driver.get(url)
    actions = ActionChains(driver)
    dropdown = driver.find_element(By.CLASS_NAME, "main-nav-dropdown")
    dropdown_parent = dropdown.find_element(By.XPATH, "..")
    actions.move_to_element(dropdown_parent).perform()

    check_1 = dropdown.get_attribute("class") == "main-nav-dropdown js-main-nav-dropdown is-open"

    if not(check_1):
        checks.append("Java dropdown not working propertly");

    image1 = driver.find_element(By.XPATH, "//img[@alt='Never stop learning.']")
    image1content = requests.get(image1.get_attribute("src")).content

    check_2 = not(len(image1content) < 239742)

    if not(check_2):
        checks.append("Images not high resolution")

    return checks