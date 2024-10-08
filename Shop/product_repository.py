from Shop.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):

        for product in self.products:

            if product.name == product_name:
                return product

    def remove(self, product_name):

        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):

        result = [f"{product.name}: {product.quantity}" for product in self.products]
        return '\n'.join(result)
