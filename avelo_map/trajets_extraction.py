import re
import requests
from bs4 import BeautifulSoup
import datetime
import calendar

from avelo_map.trajet import trajet_from_regex

funky_regex = (
    r"\n+([0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\n+"
    r"([0-9]{1,2} minutes)\n+"
    r"([0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\n+"
    r"place\n+directions_bike\n+place\n+"
    r"([^\n]+)\n+"
    r"([^\n]+)\n+"
)

cookie = "eyJpdiI6IlBRWWpCUjRxck5PdkxKcUV5QkUyV1E9PSIsInZhbHVlIjoiV3NXWWp6QktXbTMzZW9SXC9yVjZuSlI1UkkxbWNzazY2cUJOT0JkNG82dEJ0Y3BKWm1pelpKQ0RlSTFzbFpZUnciLCJtYWMiOiI3NTQwZTgxMTIwMTA5NWU0YjM0ZTk0YjNjNGIxNTVjMDM5ZTM1MTA5YTg3NGJiMzlmNjMwNjllMTEwNDBjMDE2In0="

def fetch_for_year(year):
    # A call per month because limited by number of trips on a single page. If you do more than ~ 47 trips in a month smaller increments between call are needed
    yearly_trajets = []
    for month in range(1, 12):
        start_date = datetime.datetime(year, month, 1)
        end_date = datetime.datetime(year, month, calendar.monthrange(year, month)[1])
        trajets = fetch_all_trajets_between_dates(start_date, end_date)
        yearly_trajets += trajets
    return yearly_trajets

def fetch_all_trajets_between_dates(start_date, end_date):
    formated_start_date = start_date.strftime('%d-%m-%Y')
    formated_end_date = end_date.strftime('%d-%m-%Y')
    fetch_url = f"https://avelo.rtcquebec.ca/trips?period=custom&date%5Bstart%5D={formated_start_date}&date%5Bend%5D={formated_end_date}"
    response = request_trajets_html(fetch_url, cookie)
    trajets_generator = trajet_generator_from_web_page(response.text)
    trajets = []
    for t in trajets_generator:
        trajet = trajet_from_regex(t)
        trajets.append(trajet)
    return trajets

def request_trajets_html(path, session_cookie):
    return requests.get(path, cookies={"a_velo_session": session_cookie})

def extract_from_text(text):
    pattern = re.compile(funky_regex)
    match = pattern.search(text)

    while match != None:
        yield match.groups()
        match = pattern.search(text, pos=match.end())

def trajet_generator_from_web_page(html_page):
    soup = BeautifulSoup(html_page, features="html.parser")
    if soup.h1.string == "Se connecter":
        print("Not connected to https://avelo.rtcquebec.ca/login --> go get a valid cooke!")
        return None

    trip_blocks = soup.find_all('div', attrs={'class':'trip-block'})
    raw_trajets = ""
    for block in trip_blocks:
        raw_trajets += block.text

    return extract_from_text(raw_trajets)

def extract_from_file(data_file):
    with open(data_file, "r") as raw_trajets:
        text = raw_trajets.read()
        pattern = re.compile(funky_regex)
        match = pattern.search(text)

        while match != None:
            yield match.groups()
            match = pattern.search(text, pos=match.end())
