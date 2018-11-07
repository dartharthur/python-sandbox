# library.py
# core infra group maintains this library, works on technical problems
# user can't touch this code

########################################
# Case 1 - user unable to touch library

class Base:
    def foo(self):
        return 'foo'
########################################

########################################
# Case 2 - library unable to touch user

# entire python language has notion of hooks, protocols, safety valves

# python runs top to bottom, almost everything is executable code
# class statements are runtime executable code
# creation of a class has a hook you can tap into when building a class

### in interpreter
# def _():
#     class Base:
#         pass
# from dis import dis
# dis(_) #disassemble

# class Base:
#     def foo(self):
#         # how can we ensure this doesn't break?
#         return self.bar()

# old_bc = __build_class__
# def my_bc(*a, **kw):
#     print('my buildclass->', a, kw)
#     return old_bc(*a, **kw)

# wouldn't normally do this, this just shows that this protocol oriented
# nature of python is a common pattern and very fundamental

# def my_bc(fun, name, base=None, **kw):
#     if base is Base:
#         print('check if bar method defined')
#     if base is not None:
#         return old_bc(fun, name, base, **kw)
#     return old_bc(fun, name, **kw)
# import builtins
# builtins.__build_class__ = my_bc

# python -i user.py
# log what python does when it creates a class

# almost everything python does has a hook you can hook into

# original problem was, how do you enforce a constraint from a derived
# class to a base class i.e. the derived class must have some property or method

# two ways this problem is normally solved
# 1) metaclasses - mechanism by which classes are constructed
#   - they are classes that derive from type with special methods
#   - allow you to intercept construction of derived types
#   - if only control code in library, can still enforce constraints
#     on users who use the library
# 2) __init_subclass__ (Python 3.6+)

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        if not 'bar' in body:
            raise TypeError("bad user class")
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    # def __init_subclass__(cls, *a, **kw):
    #     print('init_subclass', a, kw)
    #     return super().__init_subclass__(cls, *a, **kw)
