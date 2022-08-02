#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Create a new model"""
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
        # return ({
        #     'id': self.id,
        #     'created_at': self.created_at.isoformat(),
        #     'updated_at': self.updated_at.isoformat(),
        #     '__class__': clsName,
        # })
        classDict = self.__dict__
        classDict['updated_at'] = self.updated_at.isoformat()
        classDict['created_at'] = self.created_at.isoformat()
        classDict['__class__'] = clsName

        return classDict


# base = BaseModel()

# print(base.to_dict())
# print(base.__dict__)
# base.name = "I am a girl"
# print(base.to_dict())
# print(base.__dict__)

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))
