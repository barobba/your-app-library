
from your_app.Account import Account


class YourApp:

    def get_account_list(self):

        # Retrieve and return account list
        return [
            Account(1, 'Kim', 'Brown'),
            Account(2, 'John', 'Smith'),
            Account(3, '...', '...')
        ]

    def get_account(self, account_id):

        # Retrieve and return single account
        return Account(account_id, 'Some', 'Account')

    def save_account(self, account):

        # Do nothing
        pass
