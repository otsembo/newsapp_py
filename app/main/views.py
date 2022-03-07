from crypt import methods
from turtle import title
from flask import render_template, request
from app import news_app
from app.requests import get_sources, get_news_from_source, search_news


# Views

@news_app.route('/')
def news_sources():
    sources = get_sources()
    title = 'News Sources'
    return render_template('index.html', title=title, sources_list=sources)


@news_app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search_term = request.form["search"]
        sources = search_news(search_term)
        title = search_term+': Articles'

    return render_template('news.html', title=title, sources_list = sources)


@news_app.route('/source/<source_id>')
def news_sources_articles(source_id):
    sources = get_news_from_source(source_id)
    title = source_id+': Articles'
    return render_template('news.html', title=title, sources_list=sources)


@news_app.route('/headlines')
def headlines():
    """
    Headlines
    """
    return render_template('headlines.html')


@news_app.route('/news/<news_id>')
def news(news_id):
    """
    Specific news handle
    """
    return render_template('headlines.html', news=news_id)
