# tests/test_example.py
from selenium import webdriver

def test_example():
    print("Starting the test...")
    
    # Create a Chrome webdriver instance
    driver = webdriver.Chrome()

    # Navigate to a website
    print("Navigating to the website...")
    driver.get("https://elvin-trials711.orangehrmlive.com/client/#/dashboard")

    # Perform some actions (e.g., interact with elements, make assertions)

    # Close the browser
    driver.quit()

    print("Test completed.")


