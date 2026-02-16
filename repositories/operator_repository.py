from database.database import Database
from database.enums.database_type import DatabaseType
from models.operator import Operator


class OperatorRepository:
    @staticmethod
    def get_operator_by_email_and_password(email: str, password: str):
        conn = Database.get_connection(DatabaseType.PRODUCTION)
        cur = conn.cursor()
        query = """
            SELECT
                OperatorId,
                Name,
                Surname,
                Email,
                Password,
                InsertDate
            FROM
                Operators
            WHERE
                Email = ? AND Password = ? 
        """
        credentials = (email, password)
        cur.execute(query, credentials)
        res = cur.fetchone()
        conn.close()

        if res is None:
            return None
        else:
            return Operator(
                res["OperatorId"], res["Name"], res["Surname"], res["Email"], res["Password"], res["InsertDate"]
            )
