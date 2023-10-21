import re
import requests
from bs4 import BeautifulSoup

funky_regex = (
    r"\n+([0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\n+"
    r"([0-9]{1,2} minutes)\n+"
    r"([0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\n+"
    r"place\n+directions_bike\n+place\n+"
    r"([^\n]+)\n+"
    r"([^\n]+)\n+"
)

def request_trajets_html(path, session_cookie):
    return requests.get(path, cookies={"a_velo_session": session_cookie})

def parse_web_page(html_page):
    soup = BeautifulSoup(html_page, features="html.parser")
    if soup.h1.string == "Se connecter":
        print("Not connected to https://avelo.rtcquebec.ca/login --> go get a valid cooke!")
        return None

    trip_blocks = soup.find_all('div', attrs={'class':'trip-block'})
    for block in trip_blocks:
        print(block.text)

def extract_from_text(text):
    pattern = re.compile(funky_regex)
    match = pattern.search(text)

    while match != None:
        yield match.groups()
        match = pattern.search(text, pos=match.end())

def extract_from_file(data_file):
    with open(data_file, "r") as raw_trajets:
        text = raw_trajets.read()
        pattern = re.compile(funky_regex)
        match = pattern.search(text)

        while match != None:
            yield match.groups()
            match = pattern.search(text, pos=match.end())
