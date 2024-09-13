from WildCatZoo.animal import Animal
from WildCatZoo.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):

        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):

        if self.__budget >= price and len(self.animals) < self.__animal_capacity:

            self.animals.append(animal)
            self.__budget -= price
            return f" {animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):

        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:

            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

    def pay_workers(self):
        all_sum = sum([w.salary for w in self.workers])

        if self.__budget >= all_sum:
            self.__budget -= all_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        all_sum = sum([a.money_for_care for a in self.animals])

        if self.__budget >= all_sum:
            self.__budget -= all_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):

        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__entity_status(self.animals, 'Lion')
        result += self.__entity_status(self.animals, 'Tiger')
        result += self.__entity_status(self.animals, 'Lion')
        result += self.__entity_status(self.animals, 'Cheetah')
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__entity_status(self.workers, 'Keeper')
        result += self.__entity_status(self.workers, 'Caretaker')
        result += self.__entity_status(self.workers, 'Vet')
        return result

    def __entity_status(self, type_collection, entity):
        counter = 0
        result = ''
        for ent in type_collection:
            if ent.__class__.__name__ == entity:
                counter += 1
                result += repr(ent) + '\n'
        return f"----- {counter} {entity}s:\n" + result
