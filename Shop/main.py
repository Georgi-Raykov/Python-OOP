from Shop.drink import Drink
from Shop.food import Food
from Shop.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("apple"))
repo.find("apple").decrease(5)
print(repo)