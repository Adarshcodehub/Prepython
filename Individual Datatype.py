Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
a = int(10)
print(a)
10
a = int()
print(a)
0
# Above are some basic about "Integer in Python".
#abs() Methods in Python
print(abs(56))
56
print(-abs(-34))
-34
print(-abs(-34))
-34
# divmod() Method:-
print(divmod(25,5))
(5, 0)
# Float Datatype in Python
a = float(24.23)
>>> print(a)
24.23
>>> print(float())
0.0
>>> # round() Method:-
>>> round(345.256729,2)
345.26
>>> from math import trunc
>>> trunc(445.6712987)
445
>>> # complex() Method:-
>>> a = complex(5+3j)
>>> print(a)
(5+3j)
>>> print(complex())
0j
>>> print(complex(4,5))
(4+5j)
>>> print(complex(6))
(6+0j)
>>> dir(complex)
['__abs__', '__add__', '__bool__', '__class__', '__complex__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
>>> # Boolean Datatype:-
>>> a,b = 10,20
>>> print(a>b)
False
>>> # By Using Boolean Fuction:-
>>> print(bool())
False
>>> print(bool(a>b))
False
>>> print(bool(a<b))
True
