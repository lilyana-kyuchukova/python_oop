from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

        # try:
        #     product = next(filter(lambda p: p.name == product_name, self.products))
        #     return product
        # except StopIteration:
        #     return None

    def remove(self, product_name):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = []
        for p in self.products:
            result.append(f"{p.name}: {p.quantity}")

        return "\n".join(result)