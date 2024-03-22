Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set()
set()
>>> a = set()
>>> a
set()
>>> {}
{}
>>> s = {}
>>> s
{}
>>> type(s)
<class 'dict'>
>>> type(a)
<class 'set'>
>>> # s = {1,2.1,"Adarsh",(2+3j),True,('abc',12)}
>>> s = {1,2.1,"Adarsh",(2+3j),True,('abc',12)}
>>> s
{1, 2.1, 'Adarsh', ('abc', 12), (2+3j)}
>>> s
{1, 2.1, 'Adarsh', ('abc', 12), (2+3j)}
>>> s
{1, 2.1, 'Adarsh', ('abc', 12), (2+3j)}
>>> s
{1, 2.1, 'Adarsh', ('abc', 12), (2+3j)}
>>> s = {1,2.1,"Adarsh",(2+3j),True,('abc',12),False,0}
>>> s
{False, 1, 2.1, ('abc', 12), 'Adarsh', (2+3j)}
>>> s
{False, 1, 2.1, ('abc', 12), 'Adarsh', (2+3j)}
>>> s = {1,2.1,"Adarsh",(2+3j),True,('abc',12),False,0,0,0,0,0,0,0,0,0}
>>> s
{False, 1, 2.1, ('abc', 12), 'Adarsh', (2+3j)}
>>> {[1,2,3,'Hai',2.2]}
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    {[1,2,3,'Hai',2.2]}
TypeError: unhashable type: 'list'
>>> {(1,2,3,'Hai',2.2)}
{(1, 2, 3, 'Hai', 2.2)}
type(s)
<class 'set'>
s = set((1,2,3,'Hai',2.2))
s
{1, 2, 3, 2.2, 'Hai'}
s = set({(1,2,3,'Hai',2.2)})
s
{(1, 2, 3, 'Hai', 2.2)}
s = {1,2.1,"Adarsh",(2+3j),True,('abc',12),False,0,0,0,0,0,0,0,0,0,{1,2.1,'hai'}}
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s = {1,2.1,"Adarsh",(2+3j),True,('abc',12),False,0,0,0,0,0,0,0,0,0,{1,2.1,'hai'}}
TypeError: unhashable type: 'set'
s = set({1,2.1,"Adarsh",(2+3j),True,('abc',12),False,0,0,0,0,0,0,0,0,0})
s
{False, 1, 2.1, ('abc', 12), 'Adarsh', (2+3j)}
set({})
set()
s = set({[1,2,3,'Hai',2.2]})
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s = set({[1,2,3,'Hai',2.2]})
TypeError: unhashable type: 'list'
s = {1,2,3}
s.add(5)
s
{1, 2, 3, 5}
s.add('Adarsh')
s
{1, 2, 3, 5, 'Adarsh'}
print(s.add(True))
None
s
{1, 2, 3, 5, 'Adarsh'}
s.add(False)
s
{False, 1, 2, 3, 5, 'Adarsh'}
# False ------> 0   &   True ---------> 1
s.update([1,2,3,4,5])
s
{False, 1, 2, 3, 4, 5, 'Adarsh'}
s.add([6,,7,8])
SyntaxError: invalid syntax
s.add([6,7,8])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.add([6,7,8])
TypeError: unhashable type: 'list'
s.update('Pandey')
s
{False, 1, 2, 3, 4, 5, 'P', 'a', 'n', 'y', 'e', 'Adarsh', 'd'}
s
{False, 1, 2, 3, 4, 5, 'P', 'a', 'n', 'y', 'e', 'Adarsh', 'd'}
s.pop()
False
s
{1, 2, 3, 4, 5, 'P', 'a', 'n', 'y', 'e', 'Adarsh', 'd'}
s.pop()
1
s.pop()
2
s.pop()
3
s.pop()
4
s.pop()
5
s.pop()
'P'
s.pop()
'a'
s.pop()
'n'
s
{'y', 'e', 'Adarsh', 'd'}
s.pop()
'y'
s = {}
s.update('Adarsh')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.update('Adarsh')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
s = set()
s.update('Adarsh')
s
{'a', 's', 'h', 'A', 'r', 'd'}
s.pop()
'a'
s.pop()
's'
s.pop()
'h'
s = {'a', 's', 'h', 'A', 'r', 'd'}
s.remove('a')
s
{'s', 'A', 'h', 'r', 'd'}
s.remove('P')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.remove('P')
KeyError: 'P'
s = set()
s.pop()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.pop()
KeyError: 'pop from an empty set'
s = set(' ')
s.pop()
' '
s = set(' ')
s.remove(' ')
s
set()
s = {'s', 'A', 'h', 'r', 'd'}
s.discard('h')
s
{'s', 'A', 'r', 'd'}
s.discard(70)
s
{'s', 'A', 'r', 'd'}
s.clear()
s
set()
del s
s
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s
NameError: name 's' is not defined
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,0)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,0}
a.union(b)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
{5, 6}
a.difference(b)
{1, 2, 3, 4}
b.difference(a)
{0, 8, 9, 7}
a.symmetric_difference(b)
{0, 1, 2, 3, 4, 7, 8, 9}
a = {1,2,3,4,5,6}b = {5,6,7,8,9,0}
SyntaxError: invalid syntax
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,0}
a.update(b)
a
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a.difference_update(b)
a
{1, 2, 3, 4}
a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 6, 5, 0, 7, 8, 9}
a.isdisjoint(b)
False
a
{1, 2, 3, 4, 6, 5, 0, 7, 8, 9}
b
{0, 5, 6, 7, 8, 9}
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,0}
a.symmetric_difference_update(b)
a
{0, 1, 2, 3, 4, 7, 8, 9}
a = {1,2,3,4,5,6}
a.isdisjoint(b)
False
c = {'a','b','c'}
c.isdisjoint(b)
True
