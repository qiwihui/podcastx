from resources.article_podcast import Article, ArticleAudios, Articles
from resources.auth import Register

def initialize_routes(api):
    # article
    api.add_resource(Article, "/api/articles/<article_id>")
    api.add_resource(ArticleAudios, "/api/articles/<article_id>/audios")
    api.add_resource(Articles, "/api/articles")
    
    # auth
    api.add_resource(Register, "/api/register")
    # api.add_resource(Login, "/api/login")
