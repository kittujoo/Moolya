import time
import pytest
from selenium.common import TimeoutException

from Config.configtest import setup
from Pom_login.search_order import SearchProduct


@pytest.mark.usefixtures("setup")
class Test_Search:
    SEARCH_ITEM = "Samsung"

    def test_search_product(self, setup):
        global search_product
        search_product = SearchProduct(setup)
        search_product.search_order(self.SEARCH_ITEM)
        search_product.select_order()
        search_product.go_to_next_page()

    def test_add_order_item_to_cart(self):
        search_product.add_order_item_to_cart()
        search_product.go_to_cart()

    def test_assert_price(self):
        total_price, item_price = search_product.price_validation_total_vs_item()
        assert total_price == item_price

    def test_place_order(self):
        search_product.order_placement()
