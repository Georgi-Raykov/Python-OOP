from Bank_Committed.clients.adult import Adult
from Bank_Committed.clients.student import Student
from Bank_Committed.loans.mortgage_loan import MortgageLoan
from Bank_Committed.loans.student_loan import StudentLoan


class BankApp:

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):

        valid_loans = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}

        if loan_type not in valid_loans:
            raise Exception('Invalid loan type!')

        self.loans.append(valid_loans[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):

        valid_clients = {'Student': Student, 'Adult': Adult}

        if client_type not in valid_clients:
            raise Exception('Invalid client type!')
        if len(self.clients) == self.capacity:
            return 'Not enough bank capacity.'

        self.clients.append(valid_clients[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):

        client = self.__find_client_by_id(client_id)
        loan = self.__find_loan_by_loan_type(loan_type)

        if client.TYPE_LOAN != loan_type:
            raise Exception('Inappropriate loan type!')
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with {client_id}."

    def remove_client(self, client_id):
        client = self.__find_client_by_id(client_id)
        if not client:
            raise Exception('No such client!')
        if client.loans:
            raise Exception('The client has loans! Removal is impossible!')
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):

        loan_collections = [l.increase_interest_rate() for l in self.loans if l.__class__.__name__ == loan_type]

        count_loans = len(loan_collections) if loan_type else 0
        return f"Successfully changed {count_loans} loans."

    def increase_clients_interest(self, min_rate):
        clients_collection = [c.increase_clients_interest() for c in self.clients if c.interest < min_rate]
        count_clients = len(clients_collection) if clients_collection else 0
        return f"Number of clients affected: {count_clients}."

    def get_statistic(self):
        total_income = sum([c.income for c in self.clients])
        count_granted_loans = sum([len(c.loans) for c in self.clients])
        granted_total_sum = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_loans_sum = sum([loan.amount for loan in self.loans])
        avg_interests_rate = sum([client.interest for client in self.clients]) / len(
            self.clients) if self.clients else 0
        result = [f"Active clients: {len(self.clients)}",  f"Total income: {total_income:.2f}",
                  f"Granted loans: {count_granted_loans}  Total sum: {granted_total_sum:.2f}",
                  f"Available loans: {len(self.loans)}  Total sum: {not_granted_loans_sum:.2f}",
                  f"Average Client Interest Rate: {avg_interests_rate:.2f}"]
        return '\n'.join(result)

    def __find_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def __find_loan_by_loan_type(self, loan_type):

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan
        return None
