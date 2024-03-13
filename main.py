from Data import data
from Locator import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Data and Time
import datetime


class loginTest:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 2)

    def boot(self):
        self.driver.get(data.WebPage().url)
        self.driver.maximize_window()
        self.wait.until(EC.url_to_be(data.WebPage().url))

    def quit(self):
        self.driver.quit()

    def LoginAutomation(self):
        """
        The LoginAutomation() method attempts to log in using the credentials provided in the Excel file.
            - It iterates over the rows in the Excel file starting from the second row.
            - For each row, it reads the username and password from the Excel file.
            - It enters the username and password into the respective input fields on the webpage.
            - It clicks on the login button.
        :return:
        """
        try:
            self.boot()
            # Username - 2
            # Password - 3
            # Date - 4
            # Time - 5
            # Name - 6
            # Result - 7

            for row in range(2, data.WebPage().rowTotal() + 1):
                username = data.WebPage().readExcel(row, 2)
                password = data.WebPage().readExcel(row, 3)
                testerName = "raj"

                # Enter username
                self.wait.until(EC.visibility_of_element_located((By.NAME, locator.pageLocator().Username))).send_keys(
                    username)
                # Enter password
                self.wait.until(EC.visibility_of_element_located((By.NAME, locator.pageLocator().Password))).send_keys(
                    password)
                # Click login
                self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.pageLocator().loginButton))).click()

                try:
                    """
                      - It waits for the login page URL to match the specified login URL.
                      - If the login is successful:
                      - It prints "Login successful".
                      - It gets the current date and time.
                      - It clicks on the user menu and then the logout button.
                      - It writes "Test Passed", along with the current date, time, and tester name, to the Excel file for that row.
                      """
                    self.wait.until(EC.url_to_be(data.WebPage().LoginUrl))
                    print("Login successful")
                    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
                    current_time = datetime.datetime.now().strftime("%H-%M-%S")

                    # Click usermenu
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.pageLocator().userMenu))).click()
                    # Click logout
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.pageLocator().logout))).click()

                    data.WebPage().writeExcel(row, 4, current_date)
                    data.WebPage().writeExcel(row, 5, current_time)
                    data.WebPage().writeExcel(row, 6, testerName)
                    data.WebPage().writeExcel(row, 7, "Test Passed")
                except TimeoutException:
                    """- If the login is unsuccessful (TimeoutException): - It prints "Login Unsuccessful". - It gets 
                    the current date and time. - It writes "Test Failed", along with the current date, time, 
                    and tester name, to the Excel file for that row.
                    
                    """
                    print("Login Unsuccessful")
                    # write the data in the Excel if the credentials are not OK
                    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
                    current_time = datetime.datetime.now().strftime("%H-%M-%S")
                    data.WebPage().writeExcel(row, 4, current_date)
                    data.WebPage().writeExcel(row, 5, current_time)
                    data.WebPage().writeExcel(row, 6, testerName)
                    data.WebPage().writeExcel(row, 7, "Test Failed")
        except NoSuchElementException:
            print("Error!")
        finally:
            self.quit()


obj = loginTest()
obj.LoginAutomation()
# The class instance obj is created,
# LoginAutomation() method is called to execute the login automation.
