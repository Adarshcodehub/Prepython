# Write a program to write alternative character of a string:-
# For loop:-
'''n = input("Enter the Strings: ")
for i in range(0,len(n),2):
    if n[i] == " ":
        pass
    else:
        print(n[i],end = ",")'''
# While Loop:-
'''n = input("Enter the String: ")
c = 0
while c < len(n):
    print(n[c],end=',')
    c += 2'''
# Write a program to read a string from user and print each character in both forward and reverse direction:-
# For loop:-
'''n = input()
for i in range(len(n)):
    print(n[i],end = ',') '''

# Write a program to print all vowels present inside a given string:
# For loop:-
'''n = input("Enter the String: ")
for i in range(len(n)):
    if n[i] in "aeiouAEIOU":
        print(n[i],end = ' , ')
    else:
        pass'''
# While Loop:-
'''n = input("Enter the String: ")
c = 0
while c < len(n):
    if n[c] in "AEIOUaeiou":
        print(n[c],end = ' , ')
    else:
        pass
    c += 1'''
# Write a program to achieve given output:
# i/p:- "One two three four five six seven"
# o/p:- "One owt three ruof five xis seven"

'''n = input("Enter the String: ")
p = n.split()
c = 1
s = ''
while c <= len(p):
    if c % 2 == 0:
        
    else:
        s += p[c] + ' '
    c += 1
print(s)'''

# WAP to reverse the order of words from the sentence:-
# For Loop:-
'''n = input("Enter the string: ")
l = n.split()
str = ""
for i in l:
    for j in reversed(i):
        str += j
    str += " "
print(str)'''

# while loop:-

''' WAP to print all the consonants from the given string:- '''
# while loop:-
'''n = input("Enter the string: ")

c = 0
while c < len(n):
    if n[c] not in "AEIOUaeiou":
        print(f"{n[c]}",end = ",")
    else:
        pass
    c += 1'''

# For loop:-
'''n = input("Enter the string: ")
for i in range(len(n)):
    if n[i] not in "AEIOUaeiou":
        print(f"{n[i]}",end = ",")
    else:
        pass'''
# WAP to add all the even number from the list and add them:-
'''l = ["hai",[1,2,3],2,1,5,4,9,10,'hello',(8,1)]
c = 0
sum = 0
while c < len(l):
    if isinstance(l[c],int):
        if l[c] % 2 == 0:
            sum = sum + l[c]
        else:
            pass
    elif isinstance(l[c],(list,tuple)):
        for i in l[c]:
            if i % 2 == 0:
                sum = sum + i
            else:
                pass
    c += 1
print(sum)'''
# WAP to create a list with name and number of occurance pair of domain in tuple.
# Using Both While And for loop:-
l = ['Annu','Adarsh','Rani','Santosh','Annu','Rani','Adarsh','Santosh','Devesh']
'''l1 = []
c = 0
while c < len(l):
    a = l.count(l[c])
    l1.append(a)
    c += 1
for i in zip(l,l1):
    l2.append(i)
print(l2)'''
c = 0
a = ()
while c < len(l):
    p = l[c]
    h = l.count(l[c])
    a += tuple((p,h))
    c += 1
print(list(a))










    


