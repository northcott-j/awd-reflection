"""Goals Controller File"""
import requests
from bs4 import BeautifulSoup
from flask import abort


def list_goals():
    """
    The available writing goals
    :return: Dict of goal number to desc
    """
    goals = {
        1: "Students write both to learn and to communicate what they learn.",
        2: "Students negotiate their own writing goals and audience expectations regarding conventions of genre, medium, and situation.",
        3: "Students formulate and articulate a stance through and in their writing",
        4: "Students revise their writing using responses from others, including peers, consultants, and teachers.",
        5: "Students generate and pursue lines of inquiry and search, collect, and select sources appropriate to their writing projects.",
        6: "Students effectively use and appropriately cite sources in their writing.",
        7: "Students explore and represent their experiences, perspectives, and ideas in conversation with others.",
        8: "Students use multiple forms of evidence to support their claims, ideas, and arguments.",
        9: "Students practice critical reading strategies.",
        10: "Students provide revision-based response to their peers.",
        11: "Students reflect on their writing processes and self-assess as writers."
    }
    return goals


def goal_search_query(goal):
    """
    Search query for a goal
    :return: Google search query for a goal
    """
    queries = {
        1: "Tips for effective writing communication",
        2: "How to negotiate with professor",
        3: "How to develop a thesis",
        4: "How to revise a paper",
        5: "How to do research for a paper",
        6: "Tools for citing sources ieee acm",
        7: "How to brainstorm with others",
        8: "How to show evidence in writing",
        9: "Critical reading strategies",
        10: "How to write a peer review",
        11: "How to reflect on writing process"
    }
    return queries.get(goal, None)


def query_to_url(query):
    """
    Turns a Google search query into a Google url
    :param query: string of query
    :return: URL as a string
    """
    return "https://www.google.com/search?q={0}".format(query.lower().replace(" ", "+"))


def search_results(url):
    """
    Gets Google Search results
    :param url: URL for Google search query
    :return: Array of {title: str, url: str, desc: str}
    """
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    search_div = soup.find('div', {'id': 'search'})
    search_divs = search_div.find('ol')
    parsed_results = []
    for div in search_divs:
        if div.find('a') and div.find('cite'):
            result_info = dict()
            result_info['title'] = div.find('a').text
            result_info['res_url'] = div.find('a')['href'].replace('/url?q=', '').split('&')[0]
            result_info['disp_url'] = div.find('cite').text.replace(" ", "")
            max_span = ''
            max_span_length = 1
            for s in div.find_all('span'):
                s_len = len(s.text)
                if s_len > max_span_length:
                    max_span = s.text
                    max_span_length = s_len
            result_info['summary'] = max_span
            if max_span_length > 5:
                parsed_results.append(result_info)
    return parsed_results


def get_goal_articles(goal):
    """
    Gets the Google results associated with an article
    :param goal: goal number to lookup
    :return: List of Google searches
    """
    if goal not in range(1, (len(list_goals()) + 1)):
        abort(400, "Invalid goal number, yah Dingus!")
    return search_results(query_to_url(goal_search_query(goal)))


def error():
    """
    Function to handle a large error
    :return: error message
    """
    return 'There was some kinda error. Server may have died'
