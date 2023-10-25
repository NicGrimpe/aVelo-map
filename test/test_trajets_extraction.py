import unittest
import datetime
import os

from avelo.trajets_extraction import trajet_generator_from_web_page, extract_from_text, fetch_all_trajets_between_dates, fetch_for_year
from avelo.avelo import AVelo
  
path = "https://avelo.rtcquebec.ca/trips?period=custom&date%5Bstart%5D=02-10-2023&date%5Bend%5D=08-10-2023"

class TestTrajetsExtraction(unittest.TestCase):
       
       def setUp(self):
              self.avelo = AVelo(os.getenv("AVELO_TOKEN"))

       def test_avelo_site_is_responding(self):
              response = self.avelo.get_page(path)
              self.assertTrue(response.ok)
       
       def test_avelo_site_is_cookie_valid(self):
              html_page = self.avelo.get_page(path).text
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
              trajets = fetch_all_trajets_between_dates(self.avelo, start_date, end_date)
              self.assertEqual(len(trajets), 14)

       def test_extract_yearly_trajets(self):
              trajets = fetch_for_year(self.avelo, 2022)
              self.assertEqual(len(trajets), 37)

