from Regular_Exam_16_april_2024.clients.regular_client import RegularClient
from Regular_Exam_16_april_2024.clients.vip_client import VIPClient

from Regular_Exam_16_april_2024.waiters.full_time_waiter import FullTimeWaiter
from Regular_Exam_16_april_2024.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type, waiter_name, hours_worker):

        valid_waiter_types = {'HalfTimeWaiter': HalfTimeWaiter, 'FullTimeWaiter': FullTimeWaiter}
        if waiter_type not in valid_waiter_types:
            return f"{waiter_type} is not a recognized waiter type."
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return f"{waiter_name} is already on the staff."

        waiter = valid_waiter_types[waiter_type](waiter_name, hours_worker)
        self.waiters.append(waiter)
        return f"{waiter.name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type, client_name):

        valid_clients = {'VIPClient': VIPClient, 'RegularClient': RegularClient}

        if client_type not in valid_clients:
            return f"{client_type} is not recognized client type."

        for client in self.clients:
            if client.name == client_name:
                return f"{client_name} is already a client."
        client = valid_clients[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}"

    def process_shifts(self, waiter_name):

        waiter = self.__find_waiter_by_name(waiter_name)
        if waiter:
            return waiter.report_shift()
        else:
            return f'No waiter found with the name {waiter_name}.'

    def process_client_order(self, client_name, order_amount):

        client = self.__find_client_by_name(client_name)
        if client:

            earned_points = client.earning_points(order_amount)
            return f'{client_name} earned {earned_points} points from the order.'
        else:
            return f'{client_name} is not a registered client.'

    def apply_discount_to_client(self, client_name):

        client = self.__find_client_by_name(client_name)
        if client:
            discount_percentage, points = client.apply_discount()
            return f"{client.name} received a {discount_percentage}% discount. Remaining points {points}"
        else:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):

        total_earnings = sum(x.calculate_earnings() for x in self.waiters)
        total_points = sum(p.points for p in self.clients)

        result = ['$$ Monthly Report $$',
                  f'Total Earnings: ${total_earnings}',
                  f'Total Clients Unused Points: {total_points}', f'Total Clients Count: {len(self.clients)}',
                  '** Waiter Details **']
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)
        for client in sorted_waiters:
            result.append(str(client))
        return '\n'.join(result)

    def __find_client_by_name(self, name):

        for client in self.clients:
            if client.name == name:
                return client
        return None

    def __find_waiter_by_name(self, name):

        for waiter in self.waiters:
            if waiter.name == name:
                return waiter
        return None
