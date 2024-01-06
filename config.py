from configparser import ConfigParser
from typing import Dict, Union

URL_HHRU_VACANCIES = 'https://api.hh.ru/vacancies/'
URL_HHRU_EMPLOYERS = 'https://api.hh.ru/employers/'
LIST_WITH_HHRU_ID_EMPLOYERS = [
    {'id': 78638, 'name': 'Тинькофф'},
    {'id': 39305, 'name': 'Газпром'},
    {'id': 1740, 'name': 'Яндекс'},
    {'id': 3529, 'name': 'Сбер'},
    {'id': 80, 'name': 'АльфаБанк'},
    {'id': 907345, 'name': 'Лукойл'},
    {'id': 4934, 'name': 'Билайн'},
    {'id': 41825, 'name': 'Первый канал'},
    {'id': 1122462, 'name': 'Skypro'},
    {'id': 239363, 'name': 'Роснефть-НТЦ'}
]
PARAMS: Dict[str, Union[bool, int]] = {
    "per_page": 100,
    "only_with_salary": True
}
DATABASE_NAME = 'hhru_10_employers'


def config(filename='database.ini', section='postgresql'):
    """Получение данных для работы БД из database.ini."""

    parser = ConfigParser()  # Создание парсера
    parser.read(filename)  # Чтение данных парсером
    db = {}  # Создание словаря для данных из файла

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Некорректно заполненный файл database.ini')

    return db
