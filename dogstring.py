import json
from faker import Faker
import random


def main():
    """
    Эта функция создает словать и закидвает его в json
    :return: dict
    """


def title_():
    """
    Эта функция выбирает заголовок из txt документа
    :return: i.strip()
    """


def year_():
    """
    Эта  функция выбирает год написание от 1700 до 2020
    :return: random.randint
    """


def pages_():
    """
    Эта функция возвращает количество страниц от 80 до 200
    :return: random.randint
    """


def number_():
    """
    Эта функция возвращает isbn13 из модуля faker
    :return: fake_ru.isbn13()
    """


def rating_():
    """
    Эта функция возвращает рейтинг от 1 до 6
    :return: random.uniform(1, 6)
    """


def price_():
    """
    Эта функция возвращает стоимость книги от 200 до 1000
    :return: ('стоимость', random.randint(200, 1000))
    """


def author_():
    """
    Эта функция возвращает имя автора книги из модуля faker
    :return: fake_ru.name()
    """