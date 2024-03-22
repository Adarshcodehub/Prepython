Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# String Datatype:-
s = "Hello"
s1 = "Hai"
s2 = """Welcome"""
str1 = str()
print(str1)

print(str("Adarsh 123@ gugARGV"))
Adarsh 123@ gugARGV
# Module of String Method in Python:-
id(s)
2325819536992
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# Example of Strings:-
s = "hello"
len(s)
5
a = len(s)
print(s[-a])
h
print(s[a-1])
o
print(s[-1])
o
# Slicing in String:-
print(s[1:4:])
ell
print(s[1:-1:])
ell
print(s[-2:0:-1])
lle
print(s[::])
hello
print(s[::-1])
olleh
# capitalize() Methods:-
s = "hello"
s.captitalize()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s.captitalize()
AttributeError: 'str' object has no attribute 'captitalize'. Did you mean: 'capitalize'?
s.capitalize()
'Hello'
"Welcome".capitalize()
'Welcome'
'123hai'.capitalize()
'123hai'
# casefold() Methods:-
"Hello All".casefold()
'hello all'
# count() Method:-
s.count('l')
2
s.count('ll')
1
s = "hello all how are you"
print(s[0:6:].count('l'))
2
print(s.count('l',0,6))
2
# endswith() Methods:-
print(s.endswith('you'))
True
print(s.endswith('how',0,13))
True
# find() Methods:-
s.find("l")
2
s.find("l",3)
3
s.find('l',13)
-1
# Index() Methods:-
s.index("l")
2
s.index("l",13)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.index("l",13)
ValueError: substring not found
# isalnum() Methods:-
"apple123".isalnum()
True
"user name".isalnum()
False
# isalpha() Methods:-
"hello all".isalpha()
False
"Adarsh".isalpha()
True
# isdigit() Methods:-
"34678".isdigit()
True
"123@#".isdigit()
False
>>> # isspace() Methods:-
>>> "hello all hai!!!".isspace()
False
>>> " ".isspace()
True
>>> # isdecimal() Methods:-
>>> "234".isdecimal()
True
>>> "123.234".isdecimal()
False
>>> # isascii() Methods:-
>>> "gfhdgsakucg".isascii()
True
>>> #  islower() Methods:-
>>> "hello".islower()
True
>>> "HELLO".islower()
False
>>> "Adarsh123@#$".islower()
False
>>> "Adarsh 123#$@".islower()
False
>>> # isupper() Methods:-
>>> "HELLO".isupper()
True
>>> 'Adarsh'.isupper()
False
>>> # istitle() Methods:-
>>> "Good Morning All 123$%^".istitle()
True
>>> # lower() Methods:-
>>> "gooD MOrinNg".lower()
'good morinng'
>>> # upper() Methods:-
>>> 'gooD MoriNg".upper()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'gooD MornG'.upper()
'GOOD MORNG'





