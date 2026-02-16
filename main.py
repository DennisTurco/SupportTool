from database.database_initializer import DatabaseInitializer
from database.enums.database_type import DatabaseType
from repositories.operator_repository import OperatorRepository

if __name__ == "__main__":
    DatabaseInitializer.init_database(DatabaseType.PRODUCTION)

    while True:
        email = str(input("Inserisci l'Email: "))
        password = str(input("Inserisci la Password: "))
        operator = OperatorRepository.get_operator_by_email_and_password(email, password)
        if operator is None:
            print("Email o Password Errati")
        else:
            print(operator.name)
            break
