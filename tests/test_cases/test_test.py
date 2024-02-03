import pytest
from selenium.webdriver.common.by import By
from conftest import authenticated_browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check(authenticated_browser):
    authenticated_browser.get("https://elvin-trials711.orangehrmlive.com/client/#/pim/employees/206/profile")

    navbar_element = WebDriverWait(authenticated_browser, 10).until(
        EC.presence_of_element_located((By.ID, "topbar"))
    )

    employer_name = "g"

    assert employer_name in navbar_element.text

    

    

