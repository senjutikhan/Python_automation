from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_ALERT = (By.XPATH, "//div[contains(@class,'alert-danger')]")
    ACCOUNT_BREADCRUMB = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Account']")

    def enter_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        return self.is_displayed(self.ACCOUNT_BREADCRUMB)

    def get_warning_message(self):
        return self.get_text(self.WARNING_ALERT)


