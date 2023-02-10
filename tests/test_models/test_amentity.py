#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.amentity import Amentity


class test_Amentity(test_basemodel):
    """ """
    super().__init__(self, *args, **kwargs)
    self.name = "Amentity"
    self.value = Amentity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
