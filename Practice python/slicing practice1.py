Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir(int())
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
5+9
14
5&&3
SyntaxError: invalid syntax
for(5 && 3 || 3<5)
SyntaxError: invalid syntax
for(5 && 3 || 3<5):
    
SyntaxError: invalid syntax
dir(float())
['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
rdivmod(25,5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    rdivmod(25,5)
NameError: name 'rdivmod' is not defined. Did you mean: 'divmod'?
a = rdivmod(25,5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a = rdivmod(25,5)
NameError: name 'rdivmod' is not defined. Did you mean: 'divmod'?
divmod(80,8)
(10, 0)
dir(bool())
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
help(int())

help(divmod())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    help(divmod())
TypeError: divmod expected 2 arguments, got 0
help()
Welcome to Python 3.12's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help> help(keywords)
No Python documentation found for 'help(keywords)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> divmod()
No Python documentation found for 'divmod()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  exit(name, eof)
 |
 |  Methods defined here:
 |
 |  __call__(self, code=None)
 |      Call self as a function.
 |
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

help> divmod
Help on built-in function divmod in module builtins:

divmod(x, y, /)
    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

help> abs
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

help> exit(help)
No Python documentation found for 'exit(help)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
s = 'hello this is adarsh pandey'
s
'hello this is adarsh pandey'
# slicing and split and strip
;-
SyntaxError: invalid syntax
help
Type help() for interactive help, or help(object) for help about object.
help()
Welcome to Python 3.12's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help> slicing
No Python documentation found for 'slicing'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> split
No Python documentation found for 'split'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> s = 'Hello all we are going for party tonight'
>>> print(s[-len()])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(s[-len()])
TypeError: len() takes exactly one argument (0 given)
>>> print(s[-len(s)])
H
>>> print(s[len(s)- 1])
t
>>> print(s[-len(s):(len(s)-1)+1:])
Hello all we are going for party tonight
>>> s = 'Adarsh is very Handsome boy in the training institute'
>>> print(s[-len(s):(len(s)-1)+1:])
Adarsh is very Handsome boy in the training institute
>>> print(s[(-len(s)+ len(s))+ 5:(len(s)-1)+1:])
h is very Handsome boy in the training institute
>>> print(s[(-len(s)+ len(s))+ 6:((len(s)-1)-10)+1:])
 is very Handsome boy in the training
>>> def slicing(n,p):
...     print(s[(-len(s)+ len(s))+ n:((len(s)-1)-p)+1:])
... 
...     
>>> slicing(2,4)
arsh is very Handsome boy in the training insti
>>> def slicing(n,s,e):
...     print(n[(-len(n) + len(n))+ s:((len(n)-1)-e)+1:])
... 
...     
>>> s = "Hello Adarsh Pandey"
>>> slicing(s,1,6)
ello Adarsh 
>>> slicing(s,0,0)
Hello Adarsh Pandey
