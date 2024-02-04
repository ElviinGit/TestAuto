from conftest import authenticated_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_login_successfully_with_valid_credentials(authenticated_browser):

    # Navigate to the login page
    
    assert "Employee Management" in authenticated_browser.title
    
def test_login_with_invalid_credentials(browser):
    browser.get("https://elvin-trials711.orangehrmlive.com/client/#/dashboard")
    username_input = browser.find_element(By.ID, "txtUsername")
    password_input = browser.find_element(By.ID, "txtPassword")

    username_input.send_keys("Admin")
    password_input.send_keys("T9@wxwDN7")

    login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()

    toast_messages = WebDriverWait(browser, 20).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "toast-message"))
    )
    assert "Invalid Credentials" in toast_messages[0].text