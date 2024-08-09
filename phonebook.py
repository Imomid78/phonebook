class shomare:
    def __init__(self,number,):
        self.number = number
        

    def __str__(self):
        return f"{self.number}"
    


class category:
    def __init__(self,cattegory):
        self.cattegory = cattegory

    def __str__(self) -> str:
        return f"{self.cattegory}"



class city:
    def __init__(self,city):
        self.city = city

    def __str__(self) -> str:
        return f"{self.city}"
        



class human:
    def __init__(self,fname,lname,shomare,city,category):
        self.fname = fname
        self.lname = lname
        self.shomare = shomare
        self.category = category
        self.city = city

    def __str__(self) -> str:
        return f"{self.fname},{self.lname},{self.shomare},{self.city},{self.category}"
    



contactlist = []



print()
def main_menu():
    print("-"*25)
    print("| 1) add new contact    |")
    print("| 2) show all contacts  |")
    print("| 3) edit contact       |")
    print("| 4) delete contact     |")
    print("| 5) exit               |")
    print("-"*25)


main_menu()
current = input()
while current != '5':
    if current == '1':
        fname = input("pleaz enter fname ")
        lname = input("pleaz enter lname ")

        shommare = input("pleaz enter number ") 

        ciity = input("mahal skonat ra benevesid ")

        cattegory = input("nesbat in mokhatab ra benevesid ")

        humman = human(fname , lname , shommare , ciity , cattegory)
        
        contactlist.append(humman)  
        print("mokhatab ezafe shod")


    elif current == '2':
        # contactlist = [h1,h2,h3]
        if len(contactlist)== 0:
            print("no contact")
        else:
            for i in contactlist:
                
                print(i)
                print("-"*40)



    elif current == '3':
        nam = input("nam mokhatab morede nazar ra benevesid ")
        for d in contactlist:
            if d.fname == nam:
                print("1) fname")
                print("2) lanme")
                print("3) shomare")
                print("4) city")
                print("5) category")
                a = input("adad mored nazar ra benevisid ")
                while a != 0:
                    if a == "1":
                        new_fname = input("name jadid ra vared konid ")
                        if new_fname == "":
                            (contactlist).fname = fname
                        else:
                            (contactlist).fname = new_fname
                        break
                    elif a == "2":
                        new_lname = input("lname jadid ra vared konid ")
                        if new_lname == "":
                            contactlist[d.lname] = lname
                        else:
                            contactlist[d.lnamename] = new_lname
                        break
                    elif a == "3":
                        new_shommare = input("shomare jadid ra vared konid ")
                        if new_shommare == "":
                            contactlist[d.shomare] = shommare
                        else:
                            contactlist[d.shomare] = new_shommare
                        break
                    elif a == "4":
                        new_city = input("city jadid ra vared konid ")
                        if new_city == "":
                            contactlist[d.city] = ciity
                        else:
                            contactlist[d.city] = new_city
                        break
                    elif a == "5":
                        new_category = input("category jadid ra vared konid ")
                        if new_category =="":
                            contactlist[d.category] = cattegory
                        else:
                            contactlist[d.category] = new_category
                        break
            else:
                print("mokhatab mored nazar yaft nashod")
                       


    elif current == '4':
        nam = input("nam mokhatab morede nazar ra benevesid ")
        for i in contactlist:
            if i.fname == nam:
                contactlist.pop()
                print(" mokhatab mored nazar pak shod")  
    
    main_menu()
    current = input()
        

 