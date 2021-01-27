from .article_podcast import Article, ArticlePodcast, Articles


def initialize_routes(api):

    api.add_resource(Article, "/api/articles/<article_id>")
    api.add_resource(ArticlePodcast, "/api/articles/<article_id>/podcast")
    api.add_resource(Articles, "/api/articles")
