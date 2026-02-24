Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=5
>>> c=a
>>> print(a is c)
True
>>> print(a is not b)
True
>>> print(c is b)
False
>>> print(c is not a)
False
