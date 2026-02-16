from models.operator import Operator
from repositories.operator_repository import OperatorRepository


def test_get_operator_by_credentials_success(mocker):
    mock_connection = mocker.Mock()
    mock_cursor = mocker.Mock()

    mock_connection.cursor.return_value = mock_cursor

    mock_cursor.fetchone.return_value = {
        "OperatorId": 1,
        "Name": "Admin",
        "Surname": "User",
        "Email": "admin@gmail.com",
        "Password": "asdasd123",
        "InsertDate": "2024-01-01",
    }

    mocker.patch("repositories.operator_repository.Database.get_connection", return_value=mock_connection)

    operator: None | Operator = OperatorRepository.get_operator_by_email_and_password("admin@gmail.com", "asdasd123")

    mock_cursor.execute.assert_called_once()
    mock_connection.close.assert_called_once()

    assert isinstance(operator, Operator)
    assert operator.email == "admin@gmail.com"


def test_get_operator_by_credentials_not_found(mocker):
    mock_connection = mocker.Mock()
    mock_cursor = mocker.Mock()

    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None

    mocker.patch("repositories.operator_repository.Database.get_connection", return_value=mock_connection)

    operator = OperatorRepository.get_operator_by_email_and_password("wrong@gmail.com", "wrongpass")

    mock_cursor.execute.assert_called_once()
    mock_connection.close.assert_called_once()

    assert operator is None
