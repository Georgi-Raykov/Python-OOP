from Bank_Committed.clients.base_client import BaseClient


class Adult(BaseClient):

    TYPE_LOAN = 'MortgageLoan'

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=4.0)

    def increase_clients_interest(self):
        self.interest += 2.0