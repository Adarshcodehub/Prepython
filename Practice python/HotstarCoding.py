import time
n = input("Enter your name: ")
print()
print(f"Hello, {n} welcome to HOTSTAR FlicksWorld!!")
print()
print("You have an option to move:",end='\n')
print()
d = {1:'Home',2:'Search Icon',3:'News & Hobs',4:'Download',5:'My-Space'}
print(f" 1 ------> {d[1]}")
print(f" 2 ------> {d[2]}")
print(f" 3 ------> {d[3]}")
print(f" 4 ------> {d[4]}")
print(f" 5 ------> {d[5]}")
print()

x = int(input('Enter the number: '))

if x == 2:
    l = ['India','Action','Comedy','Crime','Drama','Romance','Thriller','Horror']
    print(f"You are in {d[2]}")
    print("Please, Wait.....")
    time.sleep(5)
    print()
    print('********You can search in below given Domain********')
    print()
    print(f"1 -----> {l[0]}")
    print(f"2 -----> {l[1]}")
    print(f"3 -----> {l[2]}")
    print(f"4 -----> {l[3]}")
    print(f"5 -----> {l[4]}")
    print(f"6 -----> {l[5]}")
    print(f"7 -----> {l[6]}")
    print(f"8 -----> {l[7]}")

    y = input("Search: ")
    print(f"Please Wait {n}, we are Synchronizing..................")
    time.sleep(7)
    if y in ('India','Action','Comedy','Crime','Drama','Romance','Thriller','Horror'):
        if y == 'Romance':
            l1 = ['Romance Free Show','Romance Show','Romance movie','Romance Free','Romance Free Movie']
            print()
            print(f"1 -----> {l1[0]}")
            print(f"2 -----> {l1[1]}")
            print(f"3 -----> {l1[2]}")
            print(f"4 -----> {l1[3]}")
            print(f"5 -----> {l1[4]}")
            print()
            z = input("Show Type: ")
            if z in ['Romance Free Show','Romance Show','Romance movie','Romance Free','Romance Free Movie']:
                print()
                print("*****Choose the Language***** \n\n 1 -----> Hindi \n 2 -----> English \n 3 -----> Franch")
                print()
                z1 = input("Language Type: ")
                if z1 in {'Hindi','English','Franch'}:
                    if z1 == 'Hindi':
                        m = ['Aashiqui','Love AajKal','Aksar','Hero','Sanam Re','Izzajat','Sammohanam']
                        print(f" *****Hindi Romance Movie*****\n\n 1.{m[0]}\n\t2.{m[1]}\n\t\t3.{m[2]}\n4.{m[3]}\n\t5.{m[4]}\n\t\t6.{m[5]}")
                    elif z1 == 'English':
                        c = ['Ooh ya','Titanic','LaLaLand','Crazy','The Notebook','The Proposal']
                        print(f" *****English Romance Movie*****\n\n 1.{c[0]}\n\t2.{c[1]}\n\t\t3.{c[2]}\n4.{c[3]}\n\t5.{c[4]}\n\t\t6.{c[5]}")
                    else:
                        print("Franch Movie is not Available Rigt now!!. SORRY")
                        print(f"{n} your pragram is End now!!!!")
                    

                    
                    
                else:
                    print(f"{z1} is not Available!!")

            else:
                print(f" {z} is not Found!!")
        else:
            print(f" {y} is currently not in Production. SORRY!!")
    else:
        print(f" {y} is not Available. SORRY!!")


else:
    print("It is not available right Now. SORRY!!")

