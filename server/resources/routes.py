from resources.article_podcast import Article, ArticleAudios, Articles, UserArticles
from resources.auth import Register, Login, RefreshToken
from resources.explore import ExploreArticles


def initialize_routes(api):
    # article
    api.add_resource(Article, "/api/articles/<article_id>")
    api.add_resource(ArticleAudios, "/api/articles/<article_id>/audios")
    api.add_resource(Articles, "/api/example_articles")
    api.add_resource(UserArticles, "/api/articles")
    # explore
    api.add_resource(ExploreArticles, "/api/explore/articles")
    # auth
    api.add_resource(Register, "/api/register")
    api.add_resource(Login, "/api/login")
    api.add_resource(RefreshToken, "/api/token/refresh")
