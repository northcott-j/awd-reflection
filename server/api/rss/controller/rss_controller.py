"""RSS Controller File"""
import feedparser


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
        "http://rss.nytimes.com/services/xml/rss/nyt/Space.xml",
        "https://www.nytimes.com/section/opinion/contributors?rss=1",
        "https://www.nytimes.com/section/opinion/editorials?rss=1"
    ]
    return feeds


def get_articles(limit):
    """
    Gets a number of random articles from RSS feeds
    :param limit: Returns this number of articles
    :return: Custom RSS Feed
    """
    pass


def error():
    """
    Function to handle a large error
    :return: error message
    """
    return 'There was some kinda error. Server may have died'
