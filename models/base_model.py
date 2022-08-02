#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Create a new model"""

        if kwargs is not None:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    value = datetime.strptime(value, fmt)
                if key == 'updated_at':
                    value = datetime.strptime(value, fmt)
                setattr(self, key, value)

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Representation of BaseModel instances"""

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary that contains all
        keys/values of the instance"""

        clsName = self.__class__.__name__
        classDict = self.__dict__
        classDict['updated_at'] = self.updated_at.isoformat()
        classDict['created_at'] = self.created_at.isoformat()
        classDict['__class__'] = clsName

        return classDict


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
