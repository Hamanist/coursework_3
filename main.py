from functions.functions import load_json, executed_operations, operations_by_date, conclusion

FILE = 'file.json'
AMOUNT_OF_DATA = 5


def main():
    data = load_json(FILE)
    data = executed_operations(data)
    data = operations_by_date(data, AMOUNT_OF_DATA)
    data = conclusion(data)
    for data_output in data:
        print(data_output)


if __name__ == '__main__':
    main()
