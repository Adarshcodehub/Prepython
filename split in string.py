Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Split() Module in String:-
s = "hello all how are you ?"
s.split()
['hello', 'all', 'how', 'are', 'you', '?']
len(s.split())
6
s.split(" ",2)
['hello', 'all', 'how are you ?']
s.split("h")
['', 'ello all ', 'ow are you ?']
# rfind() Methods:-
s = "hello all how are you??"
s.rfind('l')
8
s.rfind("l",4,8)
7
s.rfind("l",4,7)
-1
s.split("h")
['', 'ello all ', 'ow are you??']
# join() Methods:-
s1 = s.split()
print(s1)
['hello', 'all', 'how', 'are', 'you??']
>>> " ".join(s1)
'hello all how are you??'
>>> s = "Welcome"
>>> "**".join(s)
'W**e**l**c**o**m**e'
>>> # replace() Methods:-
>>> a = "hello all"
>>> a.replace("all","everyone")
'hello everyone'
>>> a = "hello all how are you all? i wish i could meet all"
>>> a.replace("all","everyone")
'hello everyone how are you everyone? i wish i could meet everyone'
>>> a.replace("all","everyone",1)
'hello everyone how are you all? i wish i could meet all'
>>> # strip() Methods:-
>>> s = "   hello all   "
>>> s.strip()
'hello all'
>>> s.lstrip()
'hello all   '
>>> s.rstrip()
'   hello all'
>>> # startswith() Methods:-
>>> s.startswith("h")
False
>>> s.startswith("hello")
False
>>> s.startswith("hello",9)
False
>>> s.startswith("hello",10)
False
>>> s = "hello all how are you??"
>>> # swapcase() Methods:-
>>> s.swapcase()
'HELLO ALL HOW ARE YOU??'
>>> # title() Methods:-
>>> s.title()
'Hello All How Are You??'
