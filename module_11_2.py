from pprint import pprint
import inspect


class SomeClass:
    pass

    def some_class_method(self):
        pass


def introspection_info():
    obj_type = str(type(obj))[7:-1].replace("'", '')
    obj_attrs = []
    obj_methods = []
    obj_module = inspect.getmodule(obj).__name__ if callable(obj) else (
        inspect.getmodulename(inspect.stack()[-1].filename))
    [obj_methods.append(attr) if callable(getattr(obj, attr)) else obj_attrs.append(attr) for attr in dir(obj)]
    obj_info = {'type': obj_type,
                'attributes': obj_attrs,
                'methods': obj_methods,
                'module': obj_module}
    return obj_info


objects = [5,
           'string',
           [1, 'two', 3.0],
           SomeClass,
           SomeClass.some_class_method,
           pprint,
           inspect]
for obj in objects:
    obj_introspection = introspection_info()
    print(obj_introspection)
