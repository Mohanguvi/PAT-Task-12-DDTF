
from selenium.webdriver.common.by import By



class pageLocator:

    def __init__(self):
        """
        The __init__() method initializes the class instance with the following attributes:
            - Username: Locator for the username input field.
            - Password: Locator for the password input field.
            - loginButton: Locator for the login button.
            - userMenu: Locator for the user menu.
            - logout: Locator for the logout button.
        """
        self.Username = "username"
        self.Password = "password"
        self.loginButton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        self.userMenu = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]'
        self.logout = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def enterText(self, driver, locator, text):
        """
        The enterText() method takes three arguments: driver, locator, and text.
        It finds the element based on the specified locator and enters the provided text into the input field.
        :param driver:
        :param locator:
        :param text:
        :return:
        """

        key = driver.find_element(by=By.NAME, value=locator)
        key.clear()
        key.send_keys(text)


    def clickButton(self, driver, locator):
        """
        The clickButton() method takes two arguments: driver and locator.
        It finds the element based on the specified locator and clicks on it.
        :param driver:
        :param locator:
        :return:
        """

        driver.find_element(by=By.XPATH, value=locator).click()
