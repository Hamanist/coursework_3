import json
from datetime import datetime


def load_json():
    with open('../file.json', 'r', encoding='utf-8') as f:
        file_json = json.load(f)
        return file_json


def executed_operations():
    executed_list = []
    for i in load_json():
        if i == {}:
            continue
        if i["state"] == 'EXECUTED':
            executed_list.append(i)
    return executed_list


def operations_by_date():
    sort_date = sorted(executed_operations(), key=lambda date: date["date"], reverse=True)
    return sort_date[:5]



def conclusion():
    for item in operations_by_date():
        date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = item['description']

        print(date, description)
        # print(data['from'], data['to'])


conclusion()
# Требования
# Последние 5 выполненных (EXECUTED) операций выведены на экран.
# Операции разделены пустой строкой.
# Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
# Сверху списка находятся самые последние операции (по дате).
# Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
# Номер счета замаскирован и не отображается целиком в формате  **XXXX
# (видны только последние 4 цифры номера счета).
