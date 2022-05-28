import requests
from bs4 import BeautifulSoup
from src.structures.hashmap import HashMap
from threading import Thread


class Article:
    def __init__(self, url, write_links=False, create_hashmap_file=False):
        self.url = url
        self.req = requests.get(url)
        self.html = self.req.text
        self.title = self.url[self.url.index('/wiki/') + 6:]
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.links = []
        self.links_list(write=write_links)
        self.text = self.soup.text
        self.cnt_words = HashMap()
        self.calc_cnt_words()
        if create_hashmap_file is True:
            self.cnt_words.write_to_file('files/hashmaps/' + self.title + ".txt")

    def links_list(self, write=False):
        links = list(filter(lambda x: (x[0] is not None) and x[1] is not None,
                            map(lambda x: (x.get('href'), x.get('title')), self.soup.find_all('a'))))

        if write is True:
            f = open("files/links/" + self.title + ".txt", 'w+')
        for link in links:
            if link[0][:6] == '/wiki/':
                new_url = 'https://en.wikipedia.org' + link[0] + '\n'
                if write is True:
                    f.write(new_url)
                self.links.append(new_url)
        if write is True:
            f.close()

    def calc_cnt_words(self):
        def add_word(new_word):
            if new_word in self.cnt_words:
                self.cnt_words[new_word] = self.cnt_words[new_word].value + 1
            else:
                self.cnt_words[new_word] = 1

        for line in self.text.split('\n'):
            if line != '':
                for word in line.lower().split():
                    if word.isalpha():
                        add_word(word)
                    elif word[:-1].isalpha():
                        add_word(word[:-1])

    @classmethod
    def create_a_lot_of_articles(cls, link_arr, write_links=False, create_hashmap_file=False):
        article_arr = []
        for link in link_arr:
            article_arr.append(Article(url=link, write_links=write_links, create_hashmap_file=create_hashmap_file))
        return article_arr

    @classmethod
    def multi_create_a_lot_of_articles(cls, link_arr, write_links=False, create_hashmap_file=False):
        article_arr = []
        for link in link_arr:
            article_arr.append(Thread(target=Article, args=(link, write_links, create_hashmap_file)))
        for article in article_arr:
            article.start()
        for article in article_arr:
            article.join()
        return article_arr

    @classmethod
    def create_articles_by_file_with_links(cls, path, write_links=False, create_hashmap_file=False):
        links_lst = list(filter(lambda x: x != '', map(lambda x: x[:-1], open(path, 'r').readlines())))
        return Article.create_a_lot_of_articles(links_lst, write_links=write_links,
                                                 create_hashmap_file=create_hashmap_file)

    @classmethod
    def multi_create_articles_by_file_with_links(cls, path, write_links=False, create_hashmap_file=False):
        links_lst = list(filter(lambda x: x != '', map(lambda x: x[:-1], open(path, 'r').readlines())))
        return Article.multi_create_a_lot_of_articles(links_lst, write_links=write_links,
                                                       create_hashmap_file=create_hashmap_file)

    def __repr__(self):
        return f'<Article {self.url}>'
