import pytest

from FIRST.shopping_cart import ShoppingCart

class TestShoppingCart:
    ITEM_PRICE = 100.0
    ITEM_PRICE_2 = 50.0
    ITEM_PRICE_3 = 75.0
    DISCOUNT_PERCENTAGE = 20.0
    EXPECTED_DISCOUNTED_PRICE = ITEM_PRICE - (ITEM_PRICE * DISCOUNT_PERCENTAGE / 100)
    EXPECTED_TOTAL_COST_ZERO = 0.0
    EXPECTED_TOTAL_COST = ITEM_PRICE + ITEM_PRICE_2 + ITEM_PRICE_3

    ITEM_NAME = "Item X"
    ITEM_NAME_2 = "Item Y"
    ITEM_NAME_3 = "Item Z"

    def setup_method(self):
        self.cart = ShoppingCart()

    def test_given_items_when_adding_items_then_items_are_added_to_cart(self):
        # Act
        self.cart.add_item(self.ITEM_NAME, self.ITEM_PRICE)
        self.cart.add_item(self.ITEM_NAME_2, self.ITEM_PRICE)

        # Assert
        expected_count = 2
        assert len(self.cart.get_items()) == expected_count

    def test_given_a_cart_with_an_item_when_apply_discount_then_item_price_is_discounted(self):
        # Arrange
        self.cart.add_item(self.ITEM_NAME, self.ITEM_PRICE)

        # Act
        self.cart.apply_discount(self.ITEM_NAME, self.DISCOUNT_PERCENTAGE)

        # Assert
        items = self.cart.get_items()
        item_discounted = next(item for item in items if item['name'] == self.ITEM_NAME)
        assert item_discounted['price'] == pytest.approx(self.EXPECTED_DISCOUNTED_PRICE)

    def test_given_empty_cart_when_get_total_cost_then_total_cost_is_zero(self):
        # Action
        total_cost = self.cart.get_total_cost()

        # Validation
        assert total_cost == self.EXPECTED_TOTAL_COST_ZERO

    def test_given_a_cart_with_items_when_get_total_cost_then_item_total_cost_is_sum_of_item_prices(self):
        # Arrange
        self.cart.add_item(self.ITEM_NAME, self.ITEM_PRICE)
        self.cart.add_item(self.ITEM_NAME_2, self.ITEM_PRICE_2)
        self.cart.add_item(self.ITEM_NAME_3, self.ITEM_PRICE_3)

        # Action
        total_cost = self.cart.get_total_cost()

        # Validation
        assert total_cost == pytest.approx(self.EXPECTED_TOTAL_COST)

    def test_given_shopping_cart_with_an_item_when_remove_item_then_item_is_removed(self):
        # Arrange
        self.cart.add_item(self.ITEM_NAME, self.ITEM_PRICE)

        # Act
        self.cart.remove_item(self.ITEM_NAME)

        # Assert
        items = self.cart.get_items()
        assert len(items) == 0

    def test_given_empty_shopping_cart_when_remove_item_then_exception_is_thrown(self):
        # Act & Assert
        with pytest.raises(ValueError):
            self.cart.remove_item(self.ITEM_NAME)

    # TODO: Completez les 3 tests suivants
    # def test_given_empty_cart_when_clear_cart_then_cart_is_empty(self):


    # def test_given_cart_with_an_existing_item_when_item_exists_then_return_true(self):


    # def test_given_empty_cart_when_item_exists_then_return_false(self):

