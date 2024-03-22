# WAP for decorator to print prime number from given range:-
'''n = int(input("Enter: "))
l = []
def deco(func):
    def wrapper(*args,**kwargs):
        l1 = func(*args,**kwargs)
        for i in l1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i)
    return wrapper

@deco
def disp(n):
    for i in range(2,n+1):
        global l
        l.append(i)
    return l
disp(n)'''

# WAP to display the square root of the given number:-
'''n = int(input("Enter: "))
r = n ** 0.5
def deco(func):
    def wrapper(*args,**kwargs):
        global r
        if func(*args,**kwargs) == r ** 2:
            print(f"{n} is a perfect square root")
        else:
            print(f"{n} is not the perfect square root.")
    return wrapper
@deco
def sq_re(n):
    if isinstance(n,(int,float)):
        return n
    else:
        print("It is not an Integer values.")
sq_re(n)'''

# WAP to count the number of vowel present in the string using decorator:-
'''s = input("Enter: ")
c = 0
def deco(func):
    def wrapper(*args,**kwargs):
        global c
        for i in func(*args,**kwargs):
            if i in "AEIOUaeiou":
                c += 1
        print(f"{c} number of vowels present.")
    return wrapper
                
@deco
def c_s(s):
    if isinstance(s,str):
        return s
    else:
        print("It's not a string.")

c_s(s)'''

# Create a decorator to return only positive output for any subtraction
'''n1 = int(input("Enter: "))
n2 = int(input("Enter: "))
def deco(func):
    def wrapper(*args,**kwargs):
        print(abs(func(*args,*kwargs)))
    return wrapper
@deco
def disp(n1,n2):
    a = n1 - n2
    return a
disp(n1,n2)'''

# Create a decorator to log a message "welcome all".
'''def deco(func):
    def wrapper(*args,**kwargs):
        print(func(*args,*kwargs))
    return wrapper

@deco
def con(n1,n2):
    if n1 > n2:
        return "Welcome all"
    else:
        return None
con(3,2)'''

# Create a decorator that execute a function for 3 times.

