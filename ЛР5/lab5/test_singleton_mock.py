# test_singleton_mock.py
from unittest.mock import patch
from singleton import Singleton

def test_singleton_mock():
    with patch.object(Singleton, 'get_value', return_value='mocked') as mock_method:
        s = Singleton()
        value = s.get_value()
        assert value == 'mocked'
        mock_method.assert_called_once()
