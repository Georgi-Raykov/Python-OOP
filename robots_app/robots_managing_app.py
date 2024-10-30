from robots_app.robots.female_robot import FemaleRobot
from robots_app.robots.male_robot import MaleRobot
from robots_app.services.main_service import MainService
from robots_app.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        valid_services = {'MainService': MainService, 'SecondaryService': SecondaryService}

        if service_type not in valid_services:
            raise Exception('Invalid service type!')
        service = valid_services[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        valid_robots = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

        if robot_type not in valid_robots:
            raise Exception('Invalid robot type!')
        robot = valid_robots[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):

        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        if robot.allowed_service != service.__class__.__name__:
            return "Unsuitable service."
        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot.")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot.name} to {service.name}"

    def remove_robot_from_service(self, robot_name, service_name):

        service = self.__find_service_by_name(service_name)

        for robot in service.robots:
            if robot.name == robot_name:
                service.robots.remove(robot)
                self.robots.append(robot)
                return f"Successfully removed {robot.name} from {service.name}."
        else:
            raise Exception('No such robot in this service!')

    def feed_all_robots_from_service(self, service_name):

        service = self.__find_service_by_name(service_name)

        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):

        service = self.__find_service_by_name(service_name)

        price_sum = sum([r.price for r in service.robots])
        return f"The value of service {service.name} is {price_sum:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def __find_robot_by_name(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot
        return None

    def __find_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service
        return None
