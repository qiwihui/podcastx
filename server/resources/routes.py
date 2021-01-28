from resources.article_podcast import Article, ArticleAudios, Articles


def initialize_routes(api):

    api.add_resource(Article, "/api/articles/<article_id>")
    api.add_resource(ArticleAudios, "/api/articles/<article_id>/audios")
    api.add_resource(Articles, "/api/articles")
