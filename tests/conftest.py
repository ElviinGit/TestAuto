import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    options = Options()
    # Add any additional options you need
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture
def login(browser):
    browser.get("https://elvin-trials711.orangehrmlive.com/client/#/dashboard")
    username_input = browser.find_element(By.ID, "txtUsername")
    password_input = browser.find_element(By.ID, "txtPassword")

    username_input.send_keys("Admin")
    password_input.send_keys("T9@wxwADN7")

    login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()

    yield browser
   

@pytest.fixture
def authenticated_browser(browser, login):    

    yield browser
# You can define other fixtures, configuration, or hooks here
