import pytest


@pytest.fixture
def list_fixture():
    return [{
        "id": 414894334,
        "state": "EXECUTED",
        "date": "2019-06-30T15:11:53.136004",
        "operationAmount": {
            "amount": "95860.47",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 59956820797131895975",
        "to": "Счет 43475624104328495820"
    },
        {},
        {
            "id": 200634844,
            "state": "CANCELED",
            "date": "2018-02-13T04:43:11.374324",
            "operationAmount": {
                "amount": "42210.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "to": "Счет 45735917297559088682"
        },
        {
            "id": 893507143,
            "state": "EXECUTED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {
                "amount": "90297.21",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767"
        }
    ]


@pytest.fixture()
def list_fixture_2():
    return [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        }
    ]
