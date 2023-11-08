from functions.functions import load_json, executed_operations, operations_by_date, conclusion
from unittest.mock import patch, mock_open
import json


def test_load_json(list_fixture):
    with patch("builtins.open", mock_open(read_data=json.dumps(list_fixture))) as mock_file:
        assert load_json('')


def test_executed_operations(list_fixture):
    assert executed_operations(list_fixture)
    assert len(executed_operations([{}, {"state": "EXECUTED"}])) == 1


def test_operations_by_date():
    list_data = [
        {"date": "2019-06-30T15:11:53.136004"},
        {"date": "2018-02-03T07:16:28.366141"}
    ]
    assert len(operations_by_date(list_data, 1)) == 1


def test_conclusion(list_fixture_2):
    assert conclusion(list_fixture_2)
