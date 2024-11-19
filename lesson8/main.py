# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), (получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".

def send_email(message="String", recipient="String", *, sender="university.help@gmail.com"):
    if (recipient == sender):
        print(f"Нельзя отправить письмо самому себе!")

    for elem in recipient:
        if elem == "@":
            is_recipient_true = False
            if (recipient[recipient.rindex('.'):] == ".com" or recipient[recipient.rindex('.'):] == ".ru" or
                    recipient[recipient.rindex('.'):] == ".net"):
                is_recipient_true = True

    for elem in sender:
        if elem == "@":
            is_sender_true = False
            if (sender[sender.rindex('.'):] == ".com" or sender[sender.rindex('.'):] == ".ru" or
                    sender[sender.rindex('.'):] == ".net"):
                is_sender_true = True

    if (is_recipient_true == True) and (is_sender_true == True):
        if (sender == "university.help@gmail.com"):
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            if (recipient != sender):
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


# Проверки

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
