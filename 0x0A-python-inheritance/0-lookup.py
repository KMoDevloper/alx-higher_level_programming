#!/usr/bin/python3

def lookup(object):
    """Returns tthe list of available attributes and methods of an object."""
    return dir(object)

if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
