from RegularExam_10_august_2024.stores.base_store import BaseStore


class FurnitureStore(BaseStore):

    def __init__(self, name, location):
        super().__init__(name, location, 50)

    @property
    def store_type(self):
        return 'FurnitureStore'

    def store_stats(self):

        result = [f'Store {self.name}, location: {self.location}, available capacity: {self.capacity}',
                  self.get_estimate_profit(), '**Furniture for sale:']

        models_furniture = {}

        for item in self.products:

            if item.model not in models_furniture:
                models_furniture[item.model] = {'count': 0, 'price': 0}
            models_furniture[item.model]['count'] += 1
            models_furniture[item.model]['price'] += item.price

        for model in sorted(models_furniture.keys()):
            count = models_furniture[model]['count']
            average_sum = models_furniture[model]['price'] / count
            result.append(f"{model}: {count}pcs, average price {average_sum}")
        return '\n'.join(result).strip()
