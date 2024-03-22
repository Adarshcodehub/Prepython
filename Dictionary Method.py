Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d = {}
dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d.update({1:100,2:2.25,3:(3+9j),4:'Adarsh',5:[1,2,3],6:{'a':10,'b':200}})
d
{1: 100, 2: 2.25, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}}
d.update({2:2.24})
d
{1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}}
d.update([{7,300},{8,400}])
d
{1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}, 300: 7, 8: 400}
d.pop()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.pop(1)
100
d.pop(9)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d.pop(9)
KeyError: 9
d.popitem()
(8, 400)
s = {}
s.popitem()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.popitem()
KeyError: 'popitem(): dictionary is empty'
print(d.clear())
None
d
{}
del d
d
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
f = {1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}, 300: 7, 8: 400}
f.key()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    f.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d.dict_keys([1,2,3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d.dict_keys([1,2,3,4,5,6])
NameError: name 'd' is not defined. Did you mean: 'id'?
f.dict_keys([1,2,3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    f.dict_keys([1,2,3,4,5,6])
AttributeError: 'dict' object has no attribute 'dict_keys'
f = {1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}, 300: 7, 8: 400}
print(f.key())
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(f.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
print(f.keys())
dict_keys([1, 2, 3, 4, 5, 6, 300, 8])
print(f.values())
dict_values([100, 2.24, (3+9j), 'Adarsh', [1, 2, 3], {'a': 10, 'b': 200}, 7, 400])
list(f.keys())
[1, 2, 3, 4, 5, 6, 300, 8]
list(f.values())
[100, 2.24, (3+9j), 'Adarsh', [1, 2, 3], {'a': 10, 'b': 200}, 7, 400]
f.item()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
>>> f.items()
dict_items([(1, 100), (2, 2.24), (3, (3+9j)), (4, 'Adarsh'), (5, [1, 2, 3]), (6, {'a': 10, 'b': 200}), (300, 7), (8, 400)])
>>> tuple(f.items())
((1, 100), (2, 2.24), (3, (3+9j)), (4, 'Adarsh'), (5, [1, 2, 3]), (6, {'a': 10, 'b': 200}), (300, 7), (8, 400))
>>> d.get(4)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.get(4)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> f.get(4)
'Adarsh'
>>> f.get(10)
>>> f
{1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}, 300: 7, 8: 400}
>>> f.get(10,"Key is not Available in Dictionary")
'Key is not Available in Dictionary'
>>> d.setdefault(4)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d.setdefault(4)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> f.setdefault(4)
'Adarsh'
>>> f.setdefault(7)
>>> f
{1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}, 300: 7, 8: 400, 7: None}
>>> f.setdefault(9,[1,2,3])
[1, 2, 3]
>>> f
{1: 100, 2: 2.24, 3: (3+9j), 4: 'Adarsh', 5: [1, 2, 3], 6: {'a': 10, 'b': 200}, 300: 7, 8: 400, 7: None, 9: [1, 2, 3]}
>>> d ={}
>>> d.fromkeys("Hello")
{'H': None, 'e': None, 'l': None, 'o': None}
>>> d.fromkeys([1,2,3])
{1: None, 2: None, 3: None}
>>> d.fromkeys("Love You","Adarsh")
{'L': 'Adarsh', 'o': 'Adarsh', 'v': 'Adarsh', 'e': 'Adarsh', ' ': 'Adarsh', 'Y': 'Adarsh', 'u': 'Adarsh'}
