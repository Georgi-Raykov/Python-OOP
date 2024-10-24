from Bank_Committed.clients.base_client import BaseClient


class Student(BaseClient):

    TYPE_LOAN = 'StudentLoan'

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=2.0)

    def increase_clients_interest(self):

        self.interest += 1.0

