import re
import requests

funky_regex = (
    r"([0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\n"
    r"([0-9]{1,2} minutes)\n"
    r"([0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\n"
    r"place\n"
    r"directions_bike\n"
    r"place\n"
    r"([^\n]+)\n"
    r"([^\n]+)"
)

def get_trajets_html(path, session_cookie):
    return requests.get(path, cookies={"a_velo_session": session_cookie})

def extract_from_file(data_file):
    with open(data_file, "r") as raw_trajets:
        text = raw_trajets.read()
        pattern = re.compile(funky_regex)
        match = pattern.search(text)

        while match != None:
            yield match.groups()
            match = pattern.search(text, pos=match.end())
