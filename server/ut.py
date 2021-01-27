from goose3 import Goose
from goose3.text import StopWordsChinese


def url2text(url: str) -> str:
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == "__main__":
    print(url2text("https://coolshell.cn/articles/17497.html"))
