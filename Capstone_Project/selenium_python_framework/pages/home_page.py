from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account']")
    LOGIN_OPTION = (By.XPATH, "//a[text()='Login']")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'btn-default')]")
    PRODUCT_TITLE = (By.XPATH, "//div[contains(@class,'product-layout')]//h4/a")
    NO_PRODUCT_MSG = (By.XPATH, "//p[contains(text(),'There is no product')]")

    def navigate_to_login(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_OPTION)

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def is_product_displayed(self, product_name):
        try:
            element = self.find((By.LINK_TEXT, product_name))
            return element.is_displayed()
        except:
            return False


