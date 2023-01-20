
class DataCamp():
    pass

DataCampClass = type('DataCamp', (), {})
# print(DataCampClass)
# print(DataCamp())

PythonClass = type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Doe'} )
# print(PythonClass.start_date, PythonClass.instructor)
# print(PythonClass)

PythonClass = type('PythonClass', (DataCamp,), {'start_date': 'August 2018', 'instructor': 'John Doe'} )

print(type(PythonClass))

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass

# print(type(MyMeta))
# print(type(MyClass))
# print(type(MySubclass))

class MetaOne(type):
    def __new__(cls, name, bases, dict):
        pass

class MetaTwo(type):
    def __init__(self, name, bases, dict):
        pass

# print(type(MetaOne))
# print(type(MetaTwo))