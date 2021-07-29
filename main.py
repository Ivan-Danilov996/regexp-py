import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
new_contact_list = []


def edit_phone(phone):
    more_pattern = re.compile(r"(доб.)")
    if re.search(more_pattern, phone, flags=0):
        pattern = re.compile(r"^(\+7|8)\s*\(*(\d{3})\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(*(доб.)\s*(\d*)\)*")
        return pattern.sub(r"+7(\2)\3-\4-\5 \6\7", phone)
    pattern = re.compile(r"^(\+7|8)\s*\(*(\d{3})\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})")
    return pattern.sub(r"+7(\2)\3-\4-\5", phone)


def check_contact(contact):
    for new_contact in new_contact_list:
        if new_contact[0] == contact[0]:
            for index, info in enumerate(contact):
                if index == 0 or index == 1 or index == 2:
                    continue
                else:
                    if info:
                        new_contact[index] = info
            return True
    return False


for contact_index, contact in enumerate(contacts_list):
    if contact_index == 0:
        new_contact_list.append(contact)
        continue
    new_contact = [contact[0], contact[1], contact[2]]
    new_contact = ' '.join(new_contact).strip().split(' ')
    new_contact.append(contact[3])
    new_contact.append(contact[4])
    if not contact[5]:
        new_contact.append(contact[5])
    new_contact.append(edit_phone(contact[5]))
    new_contact.append(contact[6])
    if check_contact(new_contact):
        continue
    new_contact_list.append(new_contact)
pprint(new_contact_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contact_list)

