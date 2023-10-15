import unittest

from avelo_map.trajets_extraction import get_trajets_html

valid_session_cookie = "eyJpdiI6Im96Vks3cWtBR3NPVm5IVFR6NGZteGc9PSIsInZhbHVlIjoiVWhubXE1M1VJNWVtV2xyZmdpaEMwb0lHQ0lXQ2V3MDBqc0JoQnZ1MmxoRmNHV2hGNkg2SlN0b3hHV0RIU053SiIsIm1hYyI6ImVjNzc0YjFkMGE0NzNjYjllZmE2Y2RhZmVlMjc1ODdhODdmOTk0NjUxZDMyNDAyNWM4NTQ4ZTJmZGEzNzZiZTIifQ==" 
    
path = "https://avelo.rtcquebec.ca/trips?period=custom&date%5Bstart%5D=02-10-2023&date%5Bend%5D=08-10-2023"


class TestTrajetsExtraction(unittest.TestCase):

       def test_avelo_site_is_responding(self):
        response = get_trajets_html(path, valid_session_cookie)
        self.assertTrue(response.ok)

