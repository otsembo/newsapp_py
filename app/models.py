class Source:
    def __init__(self, id, name):
        self.source_id = id
        self.name = name


class Article:
    def __init__(self, source: Source, author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = (description[:40]+'...' if len(description) > 40 else description)
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class FullSource:
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = (description[:40]+'...' if len(description) > 40 else description)
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class NewsResponse:
    def __init__(self, status, totalResults, articles):
        self.status = status
        self.totalResults = totalResults
        self.articles = articles


class SourcesResponse:
    def __init__(self, status, sources):
        self.status = status
        self.sources = sources

