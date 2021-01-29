from goose3 import Goose, Article
from goose3.text import StopWordsChinese


class ArticleInfo(object):
    def __init__(self, article: Article):
        self._article = article

    @property
    def url(self):
        return self._article.final_url

    @property
    def content(self):
        return self._article.cleaned_text

    @property
    def domain(self):
        return self._article.domain

    @property
    def site_name(self):
        if "opengraph" in self._article.infos:
            return self._article.infos.get("opengraph", {}).get("site_name", "")
        return ""

    @property
    def title(self):
        return self._article.title

    @property
    def image(self):
        return self._article

    @property
    def author(self):
        return self._article.authors[0] if self._article.authors else ""

    @property
    def image(self):
        return self._article.final_url.split(self.domain)[0] + self.domain + "/favicon.ico"


def url2article(url: str) -> ArticleInfo:
    g = Goose({"stopwords_class": StopWordsChinese})
    article = g.extract(url=url)
    return ArticleInfo(article)


if __name__ == "__main__":

    art = url2article("https://coolshell.cn/articles/17497.html")
    print(art.image)