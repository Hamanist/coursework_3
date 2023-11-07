import pytest

LIST = [{
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


@pytest.fixture
def list_fixture():
    return LIST
