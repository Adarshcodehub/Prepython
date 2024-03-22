# WAP to print square and cube of the given number:-
'''n = int(input("Enter: "))
sq_cu = lambda n: (n**2,n**3)
print(*(sq_cu(n)))'''

# WAP to check the given number is palindrome or not:-
'''n = input("Enter: ")
pal = lambda r: f"{n} is palindrome number" if r == n[::-1] else f"{n} is not palindrome number"
print(pal(n))'''

# WAP to convert negative number to positive number:-
'''n = int(input("Enter: "))
neg = lambda n: abs(n)
print(neg(n))'''

# WAP to return the key of a dictionary:-
'''d = {'a':1,'b':3,4:8,8j:'n'}
k = lambda d: d.keys()
print(*(k(d)))'''

# WAP to return the value of the dictionary:-
'''d = {'a':1,'b':8j,4:'s',5:9}
v = lambda d: d.values()
print(*(v(d)))'''

# WAP to sum of 2 number:-
'''num = lambda s,s1: (s+s1)
print(num(2,6))'''  

# Program to check if the number is even or odd:-
'''n = eval(input("Enter: "))
e_o = lambda n: f"{n} is an even number" if n % 2 == 0 else f"{n} is an odd number"
print(e_o(n))'''

# WAP program to check if the string is palindrome or not:-
'''s = input("Enter: ")
pal_s = lambda s: f"{s} is palindrome" if s.casefold() == s[::-1].casefold() else f"{s} is not palindrome"
print(pal_s(s))'''

# WAP which return first element of a sequence:-
'''l = input("Enter: ")
sequ = lambda l: l[0]
print(sequ(l))'''

# WAP which return length of any iterable:-
'''i = [1,2,3,4,5]
it_er = lambda i: len(i)
print(it_er(i))'''

# WAP which return the list of square of number in a list:-
'''l = [2,4,6,8,9]
sq = lambda l:[i**2 if isinstance(i,int) else None for i in l]
print(sq(l))'''
# By using map()
'''l1 = [6,9.2,2,5.4,4,9]
s_q = lambda i:i**2 if isinstance(i,(int,float)) else None
print(list(map(s_q,l1)))'''
# By using filter():-

# WAP to check list elements are palindrome are not:-
#l = ['Adarsh','Radar','Doggy','Dad','Pat','orgro']
'''l_t = lambda l:[True if i.casefold() == i[::-1].casefold() else False for i in l]
print(l_t(l))'''
# By Map():-
'''l_t = lambda i:i if i.casefold() == i[::-1].casefold() else 0
print(tuple(map(l_t,l)))'''
# By filter():-
'''l_t = lambda i:i if i.casefold() == i[::-1].casefold() else None
print(list(filter(l_t,l)))'''

# WAP to fetch list element and return it with its length pair:-
l = ['Adarsh',2,'Orange',6j,'People',True,'Banana','good']
'''pa_ir = lambda l:[(i,len(i)) for i in l]
print(*(pa_ir(l)))'''
# By Map():-
'''pa_ir = lambda l:(l,len(l))
print(*(map(pa_ir,l)))'''
# By Filter():-

# WAP to create list of (list element ** its indices):-
'''l = [1,2,3,4,5]
ind = lambda l:[l[i]**i for i in range(len(l))]
print(ind(l))'''
# By Map():-
l = [1,'2',3,'4',5]
'''l_t = lambda i:l[i]**i if isinstance(l[i],(int,float)) else None
print(list(map(l_t,range(len(l)))))'''
# By filter():-

# WAP to return a list of even numbers:-
'''n = int(input("Enter: "))
e_v = lambda i:[i for i in range(n) if i % 2 == 0]
print(e_v(n))'''

# WAP to get a list of even length of element:-
'''l = ['Adarsh','Cango','Cammando','Booster','Jayesh','Sahil']
l_t = lambda l:[i for i in l if len(i) % 2 == 0]
print(l_t(l))'''

# Note:-
#print(*(set(i if i % 2 == 0 else 0 for i in range(20))))

# WAP to find the replica of each character from the given string.
'''s = 'Adarsh is good and handsome boy'
rep_ca = lambda s:[i for i in s.casefold() if s.count(i) > 1]
print(rep_ca(s))'''

# WAP to return only list with positive integer:-
'''po_int = lambda :[i for i in range(-20,20) if i >= 0]
print(po_int())'''

# WAP to add 2 lists(need to add corresponding values of elements with similar index value):-
'''l = [1,2,3,4,5]
l1 = [6,7,8,9,19]
a_d = lambda l,l1:[i[0]+i[1] for i in zip(l,l1)]
print(a_d(l,l1))'''

# WAP to Print the numbers present in a list with their corresponding indices pair:-
'''l = [2,9,5,8,4,5]
p_t = lambda l:[i for i in enumerate(l)]
print(p_t(l))'''

# WAP to raise the number to the power of its indices:-
'''l = [2,9,5,8,4,5]
ra_is = lambda l:[l[i]**i for i in range(len(l))]
print(ra_is(l))'''

# WAP to fetch perfect square from the given range:-
'''r_g = lambda n: (n**0.5)**2 == n
print(list(filter(r_g,range(51))))'''

# WAP to fetch perfect cube from the given range:-
'''c_b = lambda i: (i**0.3)**2 == i
print(list(filter(c_b,range(51))))'''

t = tuple()
for i in "Hello all":
    t += tuple(i)
print(t)










