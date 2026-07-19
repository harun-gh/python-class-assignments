import re

phone_numbers = [
    "047-478-0222",
    "047-454-9754",
    "047-451-1151"
]

def where(phn):
    if re.match(r"^047-478-", phone_number):
        return "千葉工大津田沼校舎"
    elif re.match(r"^047-454-", phone_number):
        return "千葉工大新習志野校舎"
    else:
        return "不明"

for phone_number in phone_numbers:
    place = where(phone_number)

    print(phone_number, ":", place)