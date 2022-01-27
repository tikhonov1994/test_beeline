import csv

from server.models import Data


def writing_from_csv(file):
    """ Функция производит запись в БД данных из CSV файла, который принимает на вход.
    """
    with open(file, 'r', encoding='cp1251') as File:  
        reader = csv.reader(File, delimiter=',', quotechar=';',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            ip, subnet_mask, subnet, computer_number, user_name = (
                row[0], row[1], row[2], row[3], row[4]
            )
            # Далее проверка на валидность данных
            # Если данные не валидны, создаем переменную error с описанием ошибки
            # if error:
                # Data.objects.create(
                    # ip_addres=ip,
                    # subnet_mask=subnet_mask,
                    # subnet=subnet,
                    # computer_number=computer_number,
                    # user_name=user_name,
                    # error=error
                    # )
            Data.objects.create(
                ip_addres=ip,
                subnet_mask=subnet_mask,
                subnet=subnet,
                computer_number=computer_number,
                user_name=user_name,
            )

writing_from_csv()