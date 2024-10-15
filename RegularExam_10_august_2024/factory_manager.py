from RegularExam_10_august_2024.products.chair import Chair
from RegularExam_10_august_2024.products.hobby_horse import HobbyHorse
from RegularExam_10_august_2024.stores.furniture_store import FurnitureStore
from RegularExam_10_august_2024.stores.toy_store import ToyStore


class FactoryManager:

    def __init__(self, name):
        self.name = name
        self.income = 0
        self.products = []
        self.stores = []

    def produce_item(self, product_type, model, price):

        valid_types = {'Chair': Chair, 'HobbyHorse': HobbyHorse}

        if product_type not in valid_types:
            raise Exception('Invalid product type!')
        product = valid_types[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type, name, location):

        valid_stores = {'FurnitureStore': FurnitureStore, 'ToyStore': ToyStore}

        if store_type not in valid_stores:
            raise Exception(f"{store_type} is an invalid type of store!")
        store = (valid_stores[store_type](name, location))
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):

        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [p for p in products if p.sub_type.lower() in store.store_type.lower()]

        if not filtered_products:
            return 'Products do not match in type. Nothing sold.'

        for product in filtered_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price
        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name):

        store = self.__find_store_by_name(store_name)
        if not store:
            raise Exception('No such store!')

        if store.products:
            return 'The store is still having products in stock! Unregistering is inadvisable.'
        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model):

        discounted_products = [p for p in self.products if p.model == product_model]
        [p.discount() for p in discounted_products]
        return f"Discount applied to {len(discounted_products)} products with model: {product_model}"

    def request_store_stats(self, store_name):
        store = self.__find_store_by_name(store_name)
        if not store:
            return 'There is no store registered under this name!'

        return store.store_stats()

    def statistics(self):

        total_sum = 0
        products_and_count = {}
        for product in self.products:
            if product.model not in products_and_count:
                products_and_count[product.model] = 0
            products_and_count[product.model] += 1
            total_sum += product.price
        result = f"Factory: {self.name}\n" + f'Income: {self.income}\n' + \
                 '***Products Statistics***' + '\n' + f"Unsold products: {len(self.products)}. " \
                                                      f"Total net price: {total_sum}\n"

        for key, value in sorted(products_and_count.items()):
            result += f"{key}: {value}"

        result += f"\n***Partner Stores: {len(self.stores)}***\n"
        for store in sorted(self.stores, key=lambda x: x.name):
            result += f"{store.name}\n"

        return result.strip()

    def __find_store_by_name(self, name):

        for store in self.stores:
            if store.name == name:
                return store
        return None
