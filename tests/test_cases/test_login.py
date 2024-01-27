from conftest import authenticated_browser

def test_login_successfully_with_valid_credentials(authenticated_browser):

    # Navigate to the login page
    print("After assert\n")
    assert "Employee Management" in authenticated_browser.title
    print("Test Passed!\n")
