import random
import json
from faker import Faker

fake_ru = Faker("ru_RU")


def main():
    """
       Эта функция создает словать и закидвает его в json
       :return: dict
       """

    main = {}

    for i in range(1, 101):
        main[i] = {'title': title_(), 'year': year_(), 'pages': pages_(),
                   'number': number_(), 'rating': rating_(), 'price': price_(),
                   'author': author_()}

        with open("ds.json", 'w', encoding='utf-8') as f:
            json.dump(main, f, indent=4, ensure_ascii=False)


def title_():
    """
        Эта функция выбирает заголовок из txt документа
        :return: i.strip()
        """
    with open('books', 'r', encoding='utf8') as f:
        dict_ = []
        for i in f:
            dict_.append(i)
    return random.choice(dict_)


def year_():
    """
        Эта  функция выбирает год написание от 1700 до 2020
        :return: random.randint
        """
    return "год", random.randint(1700, 2020)


def pages_():
    """
        Эта функция возвращает количество страниц от 80 до 200
        :return: random.randint
        """
    return 'количество страниц -', random.randint(80, 200)


def number_():
    """
        Эта функция возвращает isbn13 из модуля faker
        :return: fake_ru.isbn13()
        """
    return fake_ru.isbn13()


def rating_():
    """
        Эта функция возвращает рейтинг от 1 до 6
        :return: random.uniform(1, 6)
        """
    return random.randint(1, 6)


def price_():
    """
        Эта функция возвращает стоимость книги от 200 до 1000
        :return: ('стоимость', random.randint(200, 1000))
        """
    return 'стоимость', random.randint(200, 1000)


def author_():
    """
        Эта функция возвращает имя автора книги из модуля faker
        :return: fake_ru.name()
        """
    list_authors = []
    for _ in range(random.randint(1, 4)):
        list_authors.append(fake_ru.name())
    return list_authors


if __name__ == "__main__":
    main()
