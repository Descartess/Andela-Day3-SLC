""" unit tests for game of thrones api """
import unittest
import requests
from mock import patch, Mock

from game_of_thrones import get_character,get_house,get_book

class GameofThronesTest(unittest.TestCase):
    """unit tests for public api code """
    def test_get_character(self):
        """ tests api call to get characters """
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            self.assertEqual(get_character('1'), 200)

    def test_get_house(self):
        """ tests api call to get houses """
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            self.assertEqual(get_house('1'), 200)

    def test_get_book(self):
        """ tests api call to get books """
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            self.assertEqual(get_book('1'), 200)
            
if __name__ == "__main__":
    unittest.main()