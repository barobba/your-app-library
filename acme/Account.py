
class Account:

    def __init__(self, record_id, first, last):

        self.record_id = record_id

        self.first = first

        self.last = last

    def get_name(self):

        return f'{self.first} {self.last}'
