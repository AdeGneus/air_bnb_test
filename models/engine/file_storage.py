#!/usr/bin/python3

import json

from models.base_model import BaseModel


class FileStorage:
    """A class that serialize and deserialize instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of objects"""

        return type(self).__objects

    def new(self, obj):
        """ Sets in objects with key to self.__objects
        Args:
            obj (dict): objects to set self.__objects with.
        """
        objNameId = obj.__class__.__name__ + "." + obj.id
        type(self).__object[objNameId] = obj

    def save(self):
        """ Serializes objects to Json file specified by file path"""

        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            dict_storage = {}
            for key, val in type(self).__objects.items():
                dict_storage[key] = val.to_dict()
            json.dump(dict_storage, file)

    # def save(self):
    #     """Serialize __objects to the JSON file __file_path."""
    #     odict = FileStorage.__objects
    #     objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
    #     with open(FileStorage.__file_path, "w") as f:
    #         json.dump(objdict, f)

    def reload(self):
        """Deserializes the Json file to objects if it exists
        """
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                for obj in json.load(file).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
