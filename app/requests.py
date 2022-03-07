from app import news_app
from urllib import request, response
import json
from .models import Source, NewsResponse, Article, SourcesResponse, FullSource

# API KEY
API_KEY = news_app.config['NEWS_API_KEY']

# BASE URL
base_url = news_app.config['NEWS_API_URL']
alt_url = news_app.config['NEWS_API_SOURCES_URL']


def get_sources():
    sources = 'top-headlines/sources'
    get_sources_url = base_url.format(sources, API_KEY)

    with request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['sources']:
            sources_list = sources_response['sources']
            sources_results = process_sources(sources_list)

    return sources_results

def search_news(search_term):
    search = 'everything?q='+search_term
    get_news_url = alt_url.format(search, API_KEY)

    with request.urlopen(get_news_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['articles']:
            sources_list = sources_response['articles']
            sources_results = process_sources_articles(sources_list)

    return sources_results

def get_news_from_source(source_id):

    source = 'top-headlines?sources='+source_id
    source_news_url = alt_url.format(source, API_KEY)

    with request.urlopen(source_news_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['articles']:
            sources_list = sources_response['articles']
            sources_results = process_sources_articles(sources_list)

    return sources_results


def process_sources(source_list):
    sources = []

    for source in source_list:
        source_object = FullSource(**source)
        sources.append(source_object)

    return sources

def process_sources_articles(source_list):
    sources = []

    for source in source_list:
        source_object = Article(**source)
        sources.append(source_object)

    return sources
