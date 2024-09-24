from Gym.customer import Customer
from Gym.equipment import Equipment
from Gym.exerciseplan import ExercisePlan
from Gym.subscription import Subscription
from Gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if not any([x == customer for x in self.customers]):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):

        if not any([x == trainer for x in self.trainers]):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):

        if not any([x == equipment for x in self.equipment]):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not any([x == plan for x in self.plans]):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not any([x == subscription for x in self.subscriptions]):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = self.__get_entity_repr(self.subscriptions, subscription_id) + '\n'
        result += self.__get_entity_repr(self.customers, subscription_id) + '\n'
        result += self.__get_entity_repr(self.trainers, subscription_id) + '\n'
        result += self.__get_entity_repr(self.equipment, subscription_id) + '\n'
        result += self.__get_entity_repr(self.plans, subscription_id) + '\n'
        return result.strip()

    def __get_entity_repr(self, objects, id):

        result = ''
        for entity in objects:
            if entity.id == id:
                result = repr(entity)
        return result
