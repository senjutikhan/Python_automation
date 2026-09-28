import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.csv_reader import read_csv_data


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def inject_driver(self, setup):
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    @pytest.mark.parametrize("data", read_csv_data("login_data.csv"))
    def test_login_from_csv(self, data):
        self.home_page.navigate_to_login()
        self.login_page.login(data["email"], data["password"])

        if data["expected_result"] == "success":
            assert self.login_page.is_login_successful(), f"Login failed for valid credentials: {data['email']}"
        else:
            warning_msg = self.login_page.get_warning_message()
            assert "Warning" in warning_msg, f"Warning message missing for invalid credentials: {data['email']}"
