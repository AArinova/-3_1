def check_mail(adress):
    ends = (".com", ".ru", ".net")
    sobaka = "@"

    if len(adress) != 0:
        end_flag = False # флаг окончания проверки тк найдена ошибка
        if sobaka in adress:
            for item in ends:
                find = adress[-len(item):]
                if find == item:
                    end_flag = True
                    break
            return end_flag
        else:
            print('Неправильно указан адрес')
            return False
    else:
        print("Адреса электронной почты не должен быть пустым.")
        return False

def send_email(mess_str, recipient, sender = 'university.help@gmail.com'):
    if recipient != sender:
        if check_mail(recipient) and check_mail(sender):
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        elif check_mail(recipient) == False or check_mail(sender) == False:
            print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    else:
        print('Нельзя отправить письмо самому себе.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


