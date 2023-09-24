from src import utils
from  utils  import get_date, mask_account_num, mask_card_num, final_mask, filter_and_sorted
import json
with open("operations.json", "r", encoding="utf-8") as file:
    all_information = json.load(file)

def test_get_date():
    assert get_date("2019-08-26T10:50:58.294041") == "26.08.2019"

def test_mask_account_num():
    assert mask_account_num("Счет 64686473678894779589") == "Счет **6864"


def test_ask_card_num():
    assert mask_card_num("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

def test_final_mask():
    assert final_mask("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert final_mask("Счет 64686473678894779589") == "Счет **6864"

def test_filter_and_sorted():
    assert filter_and_sorted(all_information)[0] == {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}