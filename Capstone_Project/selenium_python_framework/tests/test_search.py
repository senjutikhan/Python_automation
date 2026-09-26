import unittest
import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestProductSearch(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def inject_driver(self, setup):
        self.driver = setup
        self.home_page = HomePage(self.driver)

    def test_search_existing_product(self):
        product_name = "MacBook"
        self.home_page.search_product(product_name)
        self.assertTrue(
            self.home_page.is_product_displayed(product_name),
            f"Product '{product_name}' was not found in search results."
        )

    def test_search_non_existing_product(self):
        self.home_page.search_product("NonExistentGadget123")
        self.assertTrue(
            self.home_page.is_displayed(self.home_page.NO_PRODUCT_MSG),
            "Expected 'No product' message was not displayed."
        )