from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import authenticated_browser

def test_create_employer(authenticated_browser):
    # Assuming you've already logged in using your login script
    
    # Navigate to the section to add a new employer
    employer_list = WebDriverWait(authenticated_browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "top-level-menu-item"))
    )
    employer_list.click()

    print("Employer list is clickable\n")

    create_employer_button = authenticated_browser.find_element(By.ID, "addEmployeeButton")
    create_employer_button = WebDriverWait(authenticated_browser, 10).until(
        EC.element_to_be_clickable((By.ID, "addEmployeeButton"))
    )

    create_employer_button.click()

    # Fill in employer details
    employer_name_input = authenticated_browser.find_element(By.ID, "first-name-box")
    employer_midname_input = authenticated_browser.find_element(By.ID, "middle-name-box")
    employer_surname_input = authenticated_browser.find_element(By.ID, "last-name-box")
    employer_location = authenticated_browser.find_element(By.CLASS_NAME, "btn dropdown-toggle")
    
    employer_name_input.send_keys("Michael")
    employer_midname_input.send_keys("Joseph")
    employer_surname_input.send_keys("Jackson")
    # Other fields...

    # Save or submit the form
    save_button = WebDriverWait(authenticated_browser, 10).until(
        EC.element_to_be_clickable((By.ID, "modal-save-button"))
    )
    save_button.click()

    # Verify success
    success_message = WebDriverWait(authenticated_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "successMessage"))
    )
    assert "Employer created successfully" in success_message.text

    # Logout (Optional)
    # ...

# Call the test function with your browser instance
# test_create_employer(browser)
