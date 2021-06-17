from collections import Counter
from zipfile import ZipFile
from glob import glob
import re


def find_txt() -> str:
    '''
    Функция ищет zip распаковывает его ищет txt возвращает название файла
    :return: str
    '''
    for file in glob('*.zip'):
        if file:
            vim = ZipFile(file)
            vim.extractall()
            vim.close()
            for file in glob('*.txt'):
                if file:
                    return file


def my_counter(foo: str):
    '''
    Удаляет все что нам не нужно из аргумента
    :param foo:
    :return:
    '''
    name = foo.rstrip().replace(' ', '').replace('\n', '')
    return Counter(name)


def sort_key(e):
    '''
    нужно для сортировки по ключю, второй элемент кортежа
    :param e:
    :return:
    '''
    return e[1]


if __name__ == '__main__':
    gg = []
    with open(find_txt(), 'r', encoding='utf8') as f:
        foo = f.read()
        result = re.sub(r'[^A-Za-zА-Яа-я]', '', foo)
        print(Counter(result))
