"""
In multiple inheritance, the features of all the base classes are inherited into the derived class.

class Base1:
	pass
class Base2:
	pass
class MutliDerived(Base1, Base2):
	pass


class Base:
	pass

class Derived1(Base):
	pass

class Derived2(Derived1):
	pass

"""


# MRO : Method Resolution Order
# It provide ordering of class in multiderived



"""
MultiDerived.__mro__
( <class '__main__.MultiDerived>',
<class '__main__.Base1'>,
<class '__main__.Base12'>,
<class 'object'>)
"""

class X:
	pass

class Y:
	pass

class Z:
	pass

class A(X,Y):
	pass

class B(Y,Z):
	pass

class M(B,A,Z):
	pass

print(M.mro())


"""
OUTPUT:

[<class '__main__.M'>, 
<class '__main__.B'>, 
<class '__main__.A'>, 
<class '__main__.X'>, 
<class '__main__.Y'>, 
<class '__main__.Z'>,
 <class 'object'>]


