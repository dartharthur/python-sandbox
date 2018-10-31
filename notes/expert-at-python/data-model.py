# some behavior that I want to implement --> write some dunder methods (__function__) aka data model methods
# common pattern: top-level function or top-level syntax --> corresponding underscore function

#   x + y --> __add__
#  init x --> __init__
# repr(x) --> __repr__
#     x() --> __call__

# python data model is a means by which you can implement protocols that have 
# abstract meanings that depend on the object itself i.e. on the object on which
# the protocol operates

# when we implement a protocol, we delegate back to the protocol itself
# add is implemented by using the + operator
# repr is implemented by calling repr on some component

# implement custom behavior on a python object do it by implementing an underscore function
# which ties to some top-level function or top-level syntax and implement in terms of that 
# thing itself

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        # representation of a python object is typically whatever string
        # we'd have to type in the console to create another instance of said object
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    # doesn't make sense in terms of polynomial, just an example
    def __call__(self):
        pass

# python -i data-model.py
p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)

# three core patterns / mental models for understanding object orientation of python
# 1 - protocol view of python
# 2 - built-in inheritance protocol --> how it works, where you go on a python object to look for things
# 3 - caveats around how object orientation of python works
