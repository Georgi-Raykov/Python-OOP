from robots_app.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    allowed_service = 'SecondaryService'

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=7)

    def eating(self):

        self.weight += 1

