import unittest
import datetime

from avelo_map.trajets_extraction import request_trajets_html, trajet_generator_from_web_page, extract_from_text, fetch_all_trajets_between_dates, fetch_for_year

valid_session_cookie = "eyJpdiI6IlBRWWpCUjRxck5PdkxKcUV5QkUyV1E9PSIsInZhbHVlIjoiV3NXWWp6QktXbTMzZW9SXC9yVjZuSlI1UkkxbWNzazY2cUJOT0JkNG82dEJ0Y3BKWm1pelpKQ0RlSTFzbFpZUnciLCJtYWMiOiI3NTQwZTgxMTIwMTA5NWU0YjM0ZTk0YjNjNGIxNTVjMDM5ZTM1MTA5YTg3NGJiMzlmNjMwNjllMTEwNDBjMDE2In0==" 
    
path = "https://avelo.rtcquebec.ca/trips?period=custom&date%5Bstart%5D=02-10-2023&date%5Bend%5D=08-10-2023"

class TestTrajetsExtraction(unittest.TestCase):
       def test_avelo_site_is_responding(self):
              response = request_trajets_html(path, valid_session_cookie)
              self.assertTrue(response.ok)
       
       def test_avelo_site_is_cookie_valid(self):
              html_page = request_trajets_html(path, valid_session_cookie).text
              trajets_generator = trajet_generator_from_web_page(html_page)
              self.assertIsNotNone(trajets_generator)

       def test_regex_extraction(self):
              raw_trajets = open('test/assets/raw_trajets.txt', 'r')
              trajets_generator = extract_from_text(raw_trajets.read())
              trajets_count = 0
              for t in trajets_generator:
                     trajets_count+=1
              self.assertEqual(trajets_count, 4)
              raw_trajets.close()

       def test_extraction_between_dates(self):
              start_date = datetime.datetime(2023, 6, 1)
              end_date = datetime.datetime(2023, 7, 1)
              trajets = fetch_all_trajets_between_dates(start_date, end_date)
              self.assertEqual(len(trajets), 14)

       def test_extract_yearly_trajets(self):
              trajets = fetch_for_year(2022)
              self.assertEqual(len(trajets), 37)

