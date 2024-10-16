from Regular_Exam_16_april_2024.clients.base_client import BaseClient


class VIPClient(BaseClient):

    def __init__(self, name):
        super().__init__(name, membership_type='VIP')

    def earning_points(self, order_amount):
        points = int(order_amount / 5)
        self.points += points
        return points


