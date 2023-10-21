import unittest

from avelo_map.trajets_extraction import request_trajets_html, parse_web_page, extract_from_text

valid_session_cookie = "eyJpdiI6IlwvcDd1dzYycEJMTXBiT0tOeU1ZZlpBPT0iLCJ2YWx1ZSI6IjUxT1hDaGVLSm1JM0R5Q0pMYXdZZUJZRXZCZytUK1Jpamw1UWI3WDRqbm1QWWNZYldrV29pOUx2b3hicGM4WUMiLCJtYWMiOiIzOGRjYmRlZDI0ZDUyOTc2ZGE0NWRlNzZiZDk0Y2Y4YzdjZWUyYzRmMDQyZTVjZDVkMDFkMWU0NGY2MGIxMTJiIn0=" 
    
path = "https://avelo.rtcquebec.ca/trips?period=custom&date%5Bstart%5D=02-10-2023&date%5Bend%5D=08-10-2023"

class TestTrajetsExtraction(unittest.TestCase):
       def test_avelo_site_is_responding(self):
              response = request_trajets_html(path, valid_session_cookie).text
              self.assertTrue(response.ok)
       
       def test_avelo_site_is_auth(self):
              html_page = request_trajets_html(path, valid_session_cookie).text
              parse_web_page(html_page)

       def test_regex(self):
              raw_trajets = open('test/assets/raw_trajets.txt', 'r')
              trajets = extract_from_text(raw_trajets.read())
              for t in trajets:
                     print(t)
              raw_trajets.close()



