from src.article import Article
from src.structures.hashmap import HashMap
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


PATHS_LIST = [
    'files/hashmaps/1st_Krajina_Corps.txt',
    'files/hashmaps/2nd_Corps_of_the_Army_of_the_Republic_of_Bosnia_and_Herzegovina.txt',
    'files/hashmaps/3rd_Corps_of_the_Army_of_the_Republic_of_Bosnia_and_Herzegovina.txt',
    'files/hashmaps/3rd_Marine_Infantry_Regiment.txt',
]

if __name__ == '__main__':
    '''
    это какая-тто рандоманя hash map
    hp = HashMap()
    for i in range(20):
        hp[str(i)] = random.randint(1, 1000)
    hp.write_to_file('files/hashmaps/example.txt')
    '''
    '''
    это просто создаем из файла
    inst = HashMap.read_from_file('files/hashmaps/example.txt')
    print(inst)

    '''
    # art = Article('https://en.wikipedia.org/wiki/Battle_of_Vrbanja_Bridge', write_links=True)
    '''
    это чтобы проверить многопоточность
    lst = Article.multi_create_articles_by_file_with_links('files/links/Battle_of_Vrbanja_Bridge.txt', False, True)
    for art in lst:
        print(art)
    '''
    '''
    это чтобы проверить соединение в одну
    big_zur = HashMap.one_from_a_lot(path_lst=PATHS_LIST)
    big_zur.write_to_file('files/hashmaps/big_zur.txt')
    '''
