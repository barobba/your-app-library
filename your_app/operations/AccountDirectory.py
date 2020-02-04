
from your_app.models.Account import Account


class AccountDirectory:

    def create(self, first, last) -> Account:

        return Account(first, last, record_id=4)

    def read_list(self) -> list:

        return [
            Account('Kim', 'Brown', record_id=1),
            Account('John', 'Smith', record_id=2),
            Account('...', '...', record_id=3)
        ]

    def read(self, account_id) -> Account:

        return Account('Some', 'Result', record_id=account_id)

    def update(self, patch_data: dict):

        pass

    def delete(self):

        pass
