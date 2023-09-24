
def filter_and_sorted(all_information:list):
    item = [item for item in all_information if item.get("state") == "EXECUTED"]
    item.sort(key=lambda x: x.get("date"), reverse=True)
    return item[0:5]


def get_date(date:str):
    dt = date[0:10].split(sep="-")
    return dt[2] + "." + dt[1] + "." + dt[0]

def mask_account_num(msg:str):
    return "Счет **" + msg[7:11]


def mask_card_num(msg:str):
    operation_word = ""  # сюда собираем только слова ( название карты или слово "счет")
    operation_numb = ""  # сюда собираем номер карты/счета и часть цифр меняем на звездочки
    for word in msg:
        if not word.isnumeric():
            operation_word += word
        else:
            operation_numb += word
    operation_numb = operation_numb[0:4] + " " + operation_numb[4:6] + "** ****" + " " + operation_numb[12:]
    return operation_word + operation_numb

def final_mask(msg):
    if msg[0] == "С":
        return mask_account_num(msg)
    else:
        return mask_card_num(msg)












