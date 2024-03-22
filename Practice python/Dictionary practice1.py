Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict()
{}
dict({})
{}
{}
{}
dict(var_name = 1)
{'var_name': 1}
d = {1:10,2:25.5,3:True,4:8j,5:'hai',6:(1,2,3),7:[1,2,3],8:{'a','b'},9:{'a':2,'b':4}}
d
{1: 10, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}}
d += {13:90}
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d += {13:90}
TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
d
{1: 10, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}}
d.update(10:(5+6j))
SyntaxError: invalid syntax
d.update(10,(5+6j))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d.update(10,(5+6j))
TypeError: update expected at most 1 argument, got 2
d.update((5+6j))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d.update((5+6j))
TypeError: 'complex' object is not iterable
d.update(60)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.update(60)
TypeError: 'int' object is not iterable
d.update({60})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d.update({60})
TypeError: cannot convert dictionary update sequence element #0 to a sequence
d.update({15:100})
d
{1: 10, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100}
d.update({(2+9j)})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d.update({(2+9j)})
TypeError: cannot convert dictionary update sequence element #0 to a sequence
d.update({19:(2+9j)})
d
{1: 10, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100, 19: (2+9j)}
d
{1: 10, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100, 19: (2+9j)}
>>> d.update({True:70})
>>> d
{1: 70, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100, 19: (2+9j)}
>>> d.update('p' = 'Adarsh')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> d.update(p = 'Adarsh')
>>> d
{1: 70, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100, 19: (2+9j), 'p': 'Adarsh'}
>>> dict(1='hi',34=21.3,'a'='Apple')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> dict(i='hi',c=21.3,a='Apple')
{'i': 'hi', 'c': 21.3, 'a': 'Apple'}
>>> d
{1: 70, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100, 19: (2+9j), 'p': 'Adarsh'}
>>> dict(i='hi',c=21.3,a='Apple')
{'i': 'hi', 'c': 21.3, 'a': 'Apple'}
>>> d = {1: 70, 2: 25.5, 3: True, 4: 8j, 5: 'hai', 6: (1, 2, 3), 7: [1, 2, 3], 8: {'a', 'b'}, 9: {'a': 2, 'b': 4}, 15: 100, 19: (2+9j), 'p': 'Adarsh'}
>>> len(d)
12
>>> id(1)
140718087092664
>>> id(d[1])
140718087094872
>>> d[1]
70
>>> a = {'a':12,{'b':23,'c':'Adarsh'}}
SyntaxError: ':' expected after dictionary key
>>> a = {'a':12,{'b':23,'c':"Adarsh"}
... 
...      a
...      
SyntaxError: ':' expected after dictionary key
>>> a = {'a':12,{'b':23,'c':"Adarsh"}}
... 
... 
... a
... 
...      

