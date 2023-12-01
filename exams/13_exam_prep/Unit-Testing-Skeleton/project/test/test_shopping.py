from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shopping_card = ShoppingCart("Zara", 200.40)

    def test_init(self):
        self.assertEqual(self.shopping_card.shop_name, "Zara")
        self.assertEqual(self.shopping_card.budget, 200.40)
        self.assertEqual(self.shopping_card.products, {})

    def test_shop_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_card = ShoppingCart("zara1", 200.40)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_rase_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_card.add_to_cart("product", 200)
        self.assertEqual(f"Product product cost too much!", str(ve.exception))

    def test_add_to_cart_successfully(self):
        expected = "product product was successfully added to the cart!"
        result = self.shopping_card.add_to_cart("product", 39.50)

        self.assertEqual(expected, result)
        self.assertEqual(self.shopping_card.products, {"product": 39.50})

    def test_remove_from_cart_successfully(self):
        self.shopping_card.products = {"product": 39.50, "product2": 39.50}
        product_name = "product"
        result = self.shopping_card.remove_from_cart(product_name)
        expected = f"Product {product_name} was successfully removed from the cart!"

        self.assertEqual(expected, result)
        self.assertEqual(self.shopping_card.products, {"product2": 39.50})

    def test_remove_from_card_raise_value_error(self):
        product_name = "product"
        with self.assertRaises(ValueError) as ve:
            self.shopping_card.remove_from_cart(product_name)

        self.assertEqual(f"No product with name {product_name} in the cart!", str(ve.exception))

    def test__add__(self):
        self.shopping_card.add_to_cart('from_first', 1)
        second = ShoppingCart('SecondTest', 100)
        second.add_to_cart('from_second', 2)
        merged = self.shopping_card.__add__(second)
        self.assertEqual('ZaraSecondTest', merged.shop_name)
        self.assertEqual(300.4, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_products_raise_value_error(self):
        self.shopping_card.products = {"product": 39.50, "product2": 139.50, "product3": 239.50}
        total_sum = sum(self.shopping_card.products.values())
        with self.assertRaises(ValueError) as ve:
            self.shopping_card.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with {total_sum - self.shopping_card.budget:.2f}lv!", str(ve.exception))

    def test_buy_products_successfully(self):
        self.shopping_card.products = {"product": 100.00, "product2": 100.00}
        total_sum = sum(self.shopping_card.products.values())
        result = self.shopping_card.buy_products()
        expected = f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()





