"""RSS Controller File"""
import feedparser
import random
from datetime import datetime
from time import mktime
from server.utils.Future import Future


def rss_feeds():
    """
    All available RSS feeds
    :return: Links to available RSS feeds
    """
    feeds = [
        "https://www.wired.com/feed/category/science/latest/rss",
        "https://www.wired.com/feed/category/security/latest/rss",
        "https://www.wired.com/feed/rss",
        "https://www.npr.org/sections/opinion/",
        "https://www.npr.org/sections/science/",
        "https://www.npr.org/sections/technology/",
        "http://feeds.reuters.com/reuters/scienceNews",
        "http://feeds.reuters.com/reuters/technologyNews",
        "https://www.theguardian.com/tone/editorials/rss",
        "http://feeds.bbci.co.uk/news/technology/rss.xml",
        "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
        "http://feeds.foxnews.com/foxnews/opinion",
        "http://feeds.foxnews.com/foxnews/tech",
        "http://feeds.foxnews.com/foxnews/science",
        "http://rss.cnn.com/rss/cnn_tech.rss",
        "http://rss.cnn.com/rss/money_technology.rss",
        "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Space.xml"
    ]
    return feeds


def clean_time_structs(f_items):
    """
    Helper function to clean time structs from feedparser items
    :param f_items: list of feed items
    :return: f_items where each entry uses datetime instead
    """
    date_fields = ['published_parsed', 'updated_parsed', 'created_parsed', 'expired_parsed']
    for i in f_items:
        for f in date_fields:
            if f in i:
                dt = datetime.fromtimestamp(mktime(i[f]))
                i[f] = str(dt   )
    return f_items


def get_articles(limit):
    """
    Gets a number of random articles from RSS feeds
    :param limit: Returns this number of articles
    :return: Custom RSS Feed
    """
    # pull down all feeds
    future_calls = [Future(feedparser.parse, rss_url) for rss_url in rss_feeds()]
    # block until they are all in
    feeds = [future_obj() for future_obj in future_calls]
    entries = []
    for feed in feeds:
        entries.extend(clean_time_structs(feed["items"]))
    random.shuffle(entries)
    # Limit isn't working for some reason...
    # return entries[:limit]
    return entries


def error():
    """
    Function to handle a large error
    :return: error message
    """
    return 'There was some kinda error. Server may have died'
