# user.py
# team uses library to implement business logic, works on business problems
# user can only work with this code

from library import Base

########################################
# Case 1 - user unable to touch library

# breaks if no foo method
# how can we give code ability to fail BEFORE hitting production runtime env?
# can write a test

# can also enforce a constraint
# Dervied class enforces constraint on Base class

assert hasattr(Base, 'foo'), "you broke it, you fool!"

class Derived(Base):
    def bar(self):
        return self.foo()
########################################

########################################
# Case 2 - library unable to touch user

class Derived(Base):
    def bar(self):
        return 'bar'