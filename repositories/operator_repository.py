from database.database import Database
from models.operator import Operator


class OperatorRepository:
    @staticmethod
    def get_operator_by_email_and_password(email: str, password: str):
        conn = Database.get_connection()
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
