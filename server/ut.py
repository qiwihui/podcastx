from goose3 import Goose
from goose3.text import StopWordsChinese


def url2article(url: str):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article

if __name__ == "__main__":

    art = url2article("https://coolshell.cn/articles/17497.html")

