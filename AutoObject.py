class AutoObjectNode(object):
    def __init__(self, d):
        for key, value in d.items():
            setattr(self, key, AutoObject(value))

    def __repr__(self):
        items = [key + ': ' + repr(getattr(self, key)) for key in dir(self) if '__' not in key and key != 'convert']
        return u'{' + u', '.join(items) + u'}'


def AutoObject(thing):
    if type(thing) is dict:
        return AutoObjectNode(thing)
    elif type(thing) in (list, tuple, set):
        return [AutoObject(i) for i in thing]
    else:
        return thing
