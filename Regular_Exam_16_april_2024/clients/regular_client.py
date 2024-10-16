from math import floor
from Regular_Exam_16_april_2024.clients.base_client import BaseClient


class RegularClient(BaseClient):

    def __init__(self, name):
        super().__init__(name, membership_type='Regular')

    def earning_points(self, order_amount):
        points = int(order_amount / 10)
        self.points += points
        return points

