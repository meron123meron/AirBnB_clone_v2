#!/usr/bin/python3
""" test_amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """a class"""

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """a function"""
        new = self.value()
        self.assertEqual(type(new.name), str)
