Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list()
[]
>>> a = list()
>>> append.a[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    append.a[1]
NameError: name 'append' is not defined
>>> a = []
>>> a
[]
>>> l = [10,25.55,'hai',100,True,(1,2,3),[1,2,3]]
>>> l[-1]
[1, 2, 3]
>>> l[-1][2]
3
>>> l
[10, 25.55, 'hai', 100, True, (1, 2, 3), [1, 2, 3]]
>>> l[-1][0]
1
>>> l[-1][0] = 200
>>> l
[10, 25.55, 'hai', 100, True, (1, 2, 3), [200, 2, 3]]
>>> l
[10, 25.55, 'hai', 100, True, (1, 2, 3), [200, 2, 3]]
>>> l[4] = False
>>> l
[10, 25.55, 'hai', 100, False, (1, 2, 3), [200, 2, 3]]
>>> l[4] = 0
>>> l
[10, 25.55, 'hai', 100, 0, (1, 2, 3), [200, 2, 3]]
>>> l[-2][1::]
(2, 3)
>>> l[-1][0:1:-1]
[]
>>> l[-1][1:0:-1]
[2]
>>> l[-1][1:-3:-1]
[2]
l[-1]
[200, 2, 3]
l
[10, 25.55, 'hai', 100, 0, (1, 2, 3), [200, 2, 3]]
dir(l)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
l = [1,2,3,4,1,2,3,1,2,1,2,1,3,5,4,7,8]
l.count(1)
5
l.index(3)
2
l.index(7)
15
l.index(2,3)
5
for el in range(len(l)):
    a = l[el]

    
print(a)
8
l = []
l.append(1)
l.append('hai')
l.append(21.23)
l.append((1,2,3))
l.append([3,4,5])
l.append({8,9,0})
l.append({1:'hai',2:'Adarsh'})
l
[1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}]
l.append(2j)
l
[1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}, 2j]
l[7] = complex(2,3)
l
[1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}, (2+3j)]
l = list("Hello")
l
['H', 'e', 'l', 'l', 'o']
l = list([1,4,8])
l
[1, 4, 8]
l.extend("Pandey")
l
[1, 4, 8, 'P', 'a', 'n', 'd', 'e', 'y']
l = [1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}]
l = list("Pandey")
l
['P', 'a', 'n', 'd', 'e', 'y']
for a in range(len(l)):
    print(f"Position of {l[a]} element is {a}.")

    
Position of P element is 0.
Position of a element is 1.
Position of n element is 2.
Position of d element is 3.
Position of e element is 4.
Position of y element is 5.
l.insert(3,@)
SyntaxError: invalid syntax
l.insert(3,'@')
l
['P', 'a', 'n', '@', 'd', 'e', 'y']
l = [1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}, (2+8j)]
l = [1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}]
l.insert(7,complex(2,8))
l
[1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}, (2+8j)]
l.remove(21.23)
l
[1, 'hai', (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}, (2+8j)]
l[1].remove('a')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    l[1].remove('a')
AttributeError: 'str' object has no attribute 'remove'
l.remove('a')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l.remove('a')
ValueError: list.remove(x): x not in list
l.pop()
(2+8j)
l.pop(3)
[3, 4, 5]
print(l.clear())
None
l
[]
del l
l
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l
NameError: name 'l' is not defined. Did you mean: 'el'?
l = [1, 'hai', 21.23, (1, 2, 3), [3, 4, 5], {0, 8, 9}, {1: 'hai', 2: 'Adarsh'}, (2+8j)]
l.reverse()
l
[(2+8j), {1: 'hai', 2: 'Adarsh'}, {0, 8, 9}, [3, 4, 5], (1, 2, 3), 21.23, 'hai', 1]
l = [9,5,3,1,2,6]
l.sort()
l
[1, 2, 3, 5, 6, 9]
l.sort(reverse = True)
l
[9, 6, 5, 3, 2, 1]
ord('a')
97
chr(97)
'a'
l = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    l = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
NameError: name 'b' is not defined
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for a in range(len(l)):
    print(f"Element {l[a]} having ASCII Value is {ord(l[a])}")

    
Element a having ASCII Value is 97
Element b having ASCII Value is 98
Element c having ASCII Value is 99
Element d having ASCII Value is 100
Element e having ASCII Value is 101
Element f having ASCII Value is 102
Element g having ASCII Value is 103
Element h having ASCII Value is 104
Element i having ASCII Value is 105
Element j having ASCII Value is 106
Element k having ASCII Value is 107
Element l having ASCII Value is 108
Element m having ASCII Value is 109
Element n having ASCII Value is 110
Element o having ASCII Value is 111
Element p having ASCII Value is 112
Element q having ASCII Value is 113
Element r having ASCII Value is 114
Element s having ASCII Value is 115
Element t having ASCII Value is 116
Element u having ASCII Value is 117
Element v having ASCII Value is 118
Element w having ASCII Value is 119
Element x having ASCII Value is 120
Element y having ASCII Value is 121
Element z having ASCII Value is 122
