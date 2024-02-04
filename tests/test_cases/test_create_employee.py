from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def test_create_employer(authenticated_browser):
    # Step 1: Navigate to the section to add a new employer
    navigate_to_create_employer(authenticated_browser)

    # Step 2: Fill in employer details
    enter_employer_details(authenticated_browser, "Michael", "Joseph", "Jackson", "German Office")

    # Step 3: Save and proceed to the next step
    save_and_proceed(authenticated_browser)

    # Step 4: Continue with the next steps
    # ...

    # Step 5: Verify employer creation success
    verify_employer_creation_success(authenticated_browser)

def navigate_to_create_employer(browser):
    employer_list = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "top-level-menu-item"))
    )
    employer_list.click()

    create_employer_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "addEmployeeButton"))
    )
    create_employer_button.click()

    time.sleep(5)

def enter_employer_details(browser, first_name, middle_name, last_name, location):
    employer_name_input = browser.find_element(By.ID, "first-name-box")
    employer_midname_input = browser.find_element(By.ID, "middle-name-box")
    employer_surname_input = browser.find_element(By.ID, "last-name-box")

    employer_name_input.send_keys(first_name)
    employer_midname_input.send_keys(middle_name)
    employer_surname_input.send_keys(last_name)

    employer_location = browser.find_element(By.ID, "location")
    select = Select(employer_location)
    select.select_by_visible_text(location)

    save_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "modal-save-button"))
    )
    save_button.click()

    time.sleep(5)

def save_and_proceed(browser):
    next_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
    )
    next_button.click()

    time.sleep(5)

    next_button_second = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Next")]'))
    )
    next_button_second.click()

    next_button_third = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wizard-nav-button-section"]/button[2]'))
    )

    employer_city_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "city"))
    )   

    employer_city_input.send_keys("Baku")

    next_button_third.click()

    time.sleep(6)

    save_last = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wizard-nav-button-section"]/button[3]'))
    )
    print("Time to get an error")
    save_last.click()

def verify_employer_creation_success(browser):
    toast_messages = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "toast-message"))
    )

    assert "Successfully Saved" in toast_messages[0].text
