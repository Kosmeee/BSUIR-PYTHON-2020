singletons = {}


def singleton(Cls):
    class NewCls(object):
        instance = None

        def __new__(cls, *args, **kwargs):
            if Cls not in singletons.keys():
                instance = Cls(*args, **kwargs)
                singletons[Cls] = instance
                return instance
            else:
                return singletons[Cls]

       
    return NewCls


@singleton
class MyClass:
    def __init__(self, a):
        self.a = a


