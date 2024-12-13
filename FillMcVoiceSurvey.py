import time
from icecream import ic  # type: ignore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from webdriver_manager.firefox import GeckoDriverManager  # type: ignore


txt_file = "survey_code_11627-13401-11424-15226-00000-0.txt"


def openChromeBrowser():
    # Setup Chrome WebDriver
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open McDVoice website in Chrome
    chrome_driver.get("https://www.mcdvoice.com")

    return chrome_driver


def openFirefoxBrowser():
    # Setup Firefox WebDriver
    firefox_driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    # Open McDVoice website in Firefox
    firefox_driver.get("https://www.mcdvoice.com")

    return firefox_driver


def closeChromeBrowser(chrome_driver):
    # Close Chrome browser
    chrome_driver.quit()


def closeFirefoxBrowser(firefox_driver):
    # Close Firefox browser
    firefox_driver.quit(firefox_driver)


def split_surv_code(text_file):
    """
    Opens a text file containing a survey code, reads the content, and splits the code into six parts
    based on the hyphen delimiter. Each part is returned as a separate variable.

    Args:
        text_file (str): The path to the text file containing the survey code.

    Returns:
        tuple: A tuple containing six elements, each representing a part of the survey code.
    """
    # Open the specified text file in read mode
    with open(text_file, "r") as file:
        # Read the entire content of the file into a string
        survey_code = file.read()

    # Split the survey code string into six parts using the hyphen as a delimiter
    # Each part is assigned to a separate variable (p1, p2, p3, p4, p5, p6)
    p1, p2, p3, p4, p5, p6 = survey_code.split("-")

    # IceCream Validation Check (commented out)
    # This line is used for debugging purposes to print the split parts
    # ic(p1, p2, p3, p4, p5, p6)

    # Return the six parts as a tuple
    return p1, p2, p3, p4, p5, p6


# Empty for the moment
def fill_first_page(c_browser):

    c1, c2, c3, c4, c5, c6 = split_surv_code(txt_file)
    # The survey code entry is 5 5-digit codes & 1 1-digit code
    # Codes_list contains the 6 segements of codes from the survey code
    codes_5_list = [c1, c2, c3, c4, c5]

    # Find all input elements with the class "coupon-length-5"
    input_elements = c_browser.find_elements(By.CLASS_NAME, "coupon-length-5")

    # Loop through each input element FOR THE 5 DIGIT LENGHTS
    for index, input_element in enumerate(input_elements):
        # Clear any existing text
        input_element.clear()

        # Enter the value based on index (e.g., #0, #1, etc.)
        input_element.send_keys(str(codes_5_list[index]))
        time.sleep(1)

    ic("5 Elements done.")

    # Find all input elements with the class "coupon-length-5"
    input_elements = c_browser.find_elements(By.CLASS_NAME, "coupon-length-1")

    # Loop through each input element FOR THE 1 DIGIT LENGHTS
    for index, input_element in enumerate(input_elements):
        # Clear any existing text
        input_element.clear()

        # Enter the value based on index (e.g., #0, #1, etc.)
        input_element.send_keys(str(c6))
        time.sleep(1)

    ic("1 Elements done.")

    # Find the "Start" button

    # Find all input elements with the class "NextButton"
    next_button = c_browser.find_element(By.CLASS_NAME, "NextButton")
    # Simulate hitting "Enter" on the button
    next_button.send_keys(Keys.ENTER)


# ______________ ACTION TIME ___________________________


# ic(c1, c2, c3, c4, c5, c6)

c_browser = openChromeBrowser()

fill_first_page(c_browser)

time.sleep(3)

closeChromeBrowser(c_browser)
