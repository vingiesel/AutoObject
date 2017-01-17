# AutoObject is an object to store dict-like key/value pairs as attribute/values in an object
# creating an AutoObject will recursively convert attribute values to AutoObject, until it hits
# the bedrock of primitive values:
#   using AutoObject on a dict will return an AutoObject node
#   using AutoObject on a list will return a list of AutoObject nodes
#   using AutoObject on a string, number, or object will result in an object.

class AutoObject(object):
    def __new__(cls, thing):
        if type(thing) is dict:
            node = super(AutoObject, cls).__new__(cls)
            for key, value in thing.items():
                super(AutoObject, node).__setattr__(key, AutoObject(value))
            return node
        elif type(thing) in (list, tuple, set):
            return [AutoObject(i) for i in thing]
        else:
            return thing

    def __repr__(self):
        items = [key + ': ' + repr(getattr(self, key)) for key in self.__dict__.keys()]
        return u'{' + u', '.join(items) + u'}'

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __setattr__(self, key, value):
        super(AutoObject, self).__setattr__(key, AutoObject(value))

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
