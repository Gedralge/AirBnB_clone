#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storge
import os


class test_file_Storage(unittest.TestCase):
    """Class to set the file storage method"""

    def setup(self):
        """Set up test enviroment"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
            for key in del_list:
                del storage._FileStorage__objects[key]

                def tearDown(self):
                    """Remove storage file at end of tests"""
                    try:
                        os.remove('file.json')
                    except:
                        pass

                    def test_obj_test_empty(self):
                        """__objects is initially empty"""
                        self.assertEqual(len(storage.all()), 0)
                        def test_new(self):
                            """New object is correctly added to __objects"""
                            new = BaseModel()
                            for obj in storage.all().values():
                                tmp = obj
                                self.assertIsInstance(temp,dict)

                                def test_base_model_instsntiation(self):
                                    """File is not created on Base Model save"""
                                    new = BaseModel()
                                    self.assertFalse(os.path.exists('file.json'))

                                    def test_empty(self):
                                        """Data is saved to file"""
                                        new = BaseModel()
                                        thing = new.to_dict()
                                        new.save()
                                        new2 = BaseModel(**thing)
                                        self.assertNotEqual(o.spath.getsize('file.json'), 0)

                                        def test_save(self):
                                            """FileStorage save method"""
                                            new = BaseModel()
                                            storage.save()
                                            self.assertTrue(os.path.exists('file.json'))

                                            def test_reload(self):
                                                """Storage file is successfully loaded to __objects"""
                                                new = BaseModel()
                                                storage.save()
                                                storage.reload()
                                                for obj in storage.all().values():
                                                    
                                                    loaded = obj
                                                    delf.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

                                                    def test_reload_empty(self):
                                                        """Load from an empty file"""
                                                        with open('file.json', 'w') as f:
                                                            pass
                                                        with self.assertRaises(ValueError):
                                                            storage.realod()

                                                            def test_reload_from_nonexistent(self):
                                                                """Nothing happens if file does not exist"""
                                                                new = BaseModel()
                                                                new.save()
                                                                self.assertTrue(os.path.exists('file.json'))

                                                                def test_type_path(self):
                                                                    """Confirm __file_path is string"""
                                                                    self.assertEqual(type(storage._FileStorage__file_path), str)

                                                                    def test_type_objects(self):

                                                                        """Confirm __objects is a dic"""
                                                                        self.assertEqual(type(storage.all()), dict)

                                                                        def test_key_format(self):

                                                                            """Key is properly formatted"""
                                                                            new = BaseModel()
                                                                            _id = new.to_dict()
                                                                            ['id']
                                                                            for key in storage.all().keys():

                                                                                tmp = key
                                                                                self.assertEqual(tmp,'BaseModel' + ',' + _id)

                                                                                def test_storage_var_created(self):
                                                                                    """FileStorage object storage created"""
                                                                                    from models.engine.file_storage import FileStorage
                                                                                    print(type(storage))
                                                                                    self.assertEqual(type(storage), Filestorage)

