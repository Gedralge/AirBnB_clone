#!/usr/bin/python3
"""This module defines a class to manage a file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self,obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + ',' + obj.id: obj})

        def save(self):

            """Saves storage dictionary to file"""
            with open(FileStorage.__file_path, 'w') as f:
                tmp = {}
                tmp.update(FileStorage.__objects)
                for key, val, in tmp.items():
                    tmp[key] = val.to_dic()
                    json.dump(tmp, f)

                    def reload(self):
                        """Loads storage dictionary from file"""
                        from models.user import User
                        from models.place import Place
                        from models.state import State
                        from models.city import City
                        from models.amentinty import Amentity
                        from models.review import Review

                        class = {'BaseModels': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amentity': Amentity, 'Review': Review}
                        try:
                            tmp = {}
                            with open(FileStorage.__File_path, 'r') as f:
                                tmp = json.load(f)
                                for key, val in tmp.items():
                                    self.all()[key] = classes[val['__class__']](**val)
                        except FileNotFoundError:
                            pass
