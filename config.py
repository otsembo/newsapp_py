class Config:
    NEWS_API_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/{}&apiKey={}'
    pass


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
