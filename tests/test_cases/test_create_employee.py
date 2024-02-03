from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from conftest import authenticated_browser
import time

def test_create_employer(authenticated_browser):
    # Assuming you've already logged in using your login script
    
    # Navigate to the section to add a new employer
    employer_list = WebDriverWait(authenticated_browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "top-level-menu-item"))
    )
    employer_list.click()

    create_employer_button = authenticated_browser.find_element(By.ID, "addEmployeeButton")
    create_employer_button = WebDriverWait(authenticated_browser, 10).until(
        EC.element_to_be_clickable((By.ID, "addEmployeeButton"))
    )

    create_employer_button.click()

    time.sleep(5)

    employer_name_input = authenticated_browser.find_element(By.ID, "first-name-box")
    employer_midname_input = authenticated_browser.find_element(By.ID, "middle-name-box")
    employer_surname_input = authenticated_browser.find_element(By.ID, "last-name-box")
    
    
    employer_name_input.send_keys("Michael")
    employer_midname_input.send_keys("Joseph")
    employer_surname_input.send_keys("Jackson")
    employer_location = authenticated_browser.find_element(By.ID, "location")

    select = Select(employer_location)
    select.select_by_visible_text("German Office")

    save_button = WebDriverWait(authenticated_browser, 10).until(                           # first form
        EC.element_to_be_clickable((By.ID, "modal-save-button"))                            #  
    )
    save_button.click()
    
    time.sleep(5)

    next_button = WebDriverWait(authenticated_browser, 10).until(                               # label 1, second
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))            #   Personal Detail
        )
    next_button.click()

    time.sleep(5)
    
    
    next_button_second = WebDriverWait(authenticated_browser, 10).until(                    # label 2, third
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Next")]'))        #   Employment Detail
    )
    next_button_second.click()


    next_button_third = WebDriverWait(authenticated_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wizard-nav-button-section"]/button[2]'))
    )

    employer_city_input = WebDriverWait(authenticated_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "city"))
    )   

    employer_city_input.send_keys("Baku")

    next_button_third.click()

     
    time.sleep(6)
    
    save_last = WebDriverWait(authenticated_browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wizard-nav-button-section"]/button[3]'))
    )
    print("Time to get an error")
    save_last.click()

    toast_messages = WebDriverWait(authenticated_browser, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "toast-message"))
    )

    assert "Successfully Saved" in toast_messages[0].text
    # Logout (Optional)
    # ...

# Call the test function with your browser instance
# test_create_employer(browser)
