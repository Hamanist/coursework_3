import json
from datetime import datetime


def load_json(data):
    with open(data, 'r', encoding='utf-8') as f:
        file_json = json.load(f)
        return file_json


def executed_operations(data):
    executed_list = []
    for i in data:
        if i == {}:
            continue
        if i["state"] == 'EXECUTED':
            executed_list.append(i)
    return executed_list


def operations_by_date(data, amount_of_data):
    sort_date = sorted(data, key=lambda date: date["date"], reverse=True)
    return sort_date[:amount_of_data]


def conclusion(data):
    for item in data:
        date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = item['description']
        if "from" not in item:
            item["from"] = 'Засекречено ХХХХХХХХХХХХХХХХ'
        _from = item["from"]
        card_name = _from.split(" ")
        number = card_name.pop()
        number = f'{number[:4]} {number[6:8]}** **** {number[-4:]}'
        to = f"{item['to'][:5]}**{item['to'][-4:]}"
        amount = item["operationAmount"]["amount"]
        currency = item["operationAmount"]["currency"]["name"]
        print(date, description)
        print(f'''{' '.join(card_name)} {number} -> {to}''')
        print(amount, currency, "\n")


