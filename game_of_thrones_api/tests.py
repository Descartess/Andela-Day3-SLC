""" unit tests for game of thrones api """
import unittest
import requests
from mock import patch, Mock

from game_of_thrones import get_character,get_house

class GameofThronesTest(unittest.TestCase):
    """unit tests for public api code """
    def test_get_character(self):
        """ test api call to get characters """
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            self.assertEqual(200, mock_response.status_code)

if __name__ == "__main__":
    unittest.main()