from datetime import datetime


class Operator:
    def __init__(self, operator_id: str, name: str, surname: str, email: str, password: str, insert_date: datetime):
        self.id = operator_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.insert_date = insert_date
