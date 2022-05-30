import random
import json
from faker import Faker


fake_ru = Faker("ru_RU")


def main():

    main = {}

    for i in range(101):
        main[i] = {'title': title_(), 'year': year_(), 'pages': pages_(),
                   'number': number_(), 'rating': rating_(), 'price': price_(),
                   'author': author_()}

        with open("ds.json", 'w', encoding='utf-8') as f:
            json.dump(main, f, indent=4, ensure_ascii=False)


def title_():
    with open('books', 'r', encoding='utf8' ) as f:
        dict_ = []
        for i in f:
                print(i)
    return i.strip()

def year_():
    return ("год", random.randint(1700, 2020))


def pages_():
    return ('количество страниц -', random.randint(80, 200))


def number_():
    return fake_ru.isbn13()


def rating_():
    return random.uniform(1, 6)


def price_():
    return ('стоимость', random.randint(200, 1000))


def author_():
    for i in range(1, 4):
        fake_ru.name(i)


if __name__ == "__main__":
    main()
