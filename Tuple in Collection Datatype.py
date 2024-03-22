Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tuple in Collection Datatype:-
>>> t = (1,2,3,4)
>>> t = (10,15.5,8j,True,"hai",(1,2,3),[1,2,3],{'a','b'},{'a':100,'b':200})
>>> a = (10)
>>> type(a)
<class 'int'>
>>> a = (10,)
>>> type(a)
<class 'tuple'>
>>> # Indexing in tuple:-
>>> t = (1,2,3,4)
>>> print(t[2])
3
>>> print(t[3])
4
>>> t = (10,15.5,8j,True,"hai",(1,2,3),[1,2,3],{'a','b'},{'a':100,'b':200})
>>> print(t[4])
hai
>>> print(t[3])
True
>>> print(t[4][1])
a
>>> print(t[6][2])
3
>>> print(t[7])
{'b', 'a'}
>>> print(t[8])
{'a': 100, 'b': 200}
>>> print(t[8][b])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(t[8][b])
NameError: name 'b' is not defined
>>> print(t[8]['b'])
200
>>> # Slicing in tuple:-
>>> print(t[4:7:])
('hai', (1, 2, 3), [1, 2, 3])
print(t[6][4::])
[]
print(t[6][1::])
[2, 3]
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
t.count(1)
1
t.index(4)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t.index(4)
ValueError: tuple.index(x): x not in tuple
t = (1,2,3,4,1,2,1,3,4,2,3,4,1)
t.index(4)
3
t.index(4,4)
8
t.index(10)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
