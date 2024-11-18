# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), (получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".

def send_email(message = "String", recipient = "String", *,  sender = "university.help@gmail.com"):
    for elem in recipient:
        if elem == "@":
            _index = recipient.index('@')
            print(recipient[_index:])


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')