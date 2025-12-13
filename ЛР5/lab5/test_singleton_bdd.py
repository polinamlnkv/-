# test_singleton_bdd.py
import pytest
from singleton import Singleton

def test_singleton_behavior():
    # Given: два объекта Singleton
    s1 = Singleton()
    s2 = Singleton()

    # When: установим значение через один объект
    s1.set_value("test_value")

    # Then: второй объект должен иметь такое же значение
    assert s2.get_value() == "test_value"
