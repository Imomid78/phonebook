class shomare:
    def __init__(self,number,):
        self.number = number
        

    def __str__(self):
        return f"{self.number}"
    
shommare1 = shomare("09904123202")
shommare2 = shomare("09306603360")
shommare3 = shomare("09123176240")

class category:
    def __init__(self,cattegory):
        self.cattegory = cattegory

    def __str__(self) -> str:
        return f"{self.cattegory}"

cattegory1 = category("همکار")
cattegory2 = category("فامیل")
cattegory3 = category("فامیل")

class city:
    def __init__(self,city):
        self.city = city

    def __str__(self) -> str:
        return f"{self.city}"
        
ciity1 = city("karaj")
ciity2 = city("karaj")
ciity3 = city("karaj")


class human:
    def __init__(self,fname,lname,shomare,city,category):
        self.fname = fname
        self.lname = lname
        self.shomare = shomare
        self.category = category
        self.city = city

    def __str__(self) -> str:
        return f"{self.fname},{self.lname},{self.shomare},{self.city},{self.category}"
    

h1 = human("omid","hashemi", shommare1 , ciity1 , cattegory1)
h2 = human("amir","hashemi", shommare2 , ciity2 , cattegory2)
h3 = human("mohamad","hashemi", shommare3 , ciity3 , cattegory3)

contactlist = [h1,h2,h3]



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
                    if a == 1:
                        new_fname = input("name jadid ra vared konid ")
                        if new_fname != "":
                            contactlist.fname = new_fname
                        else:
                            contactlist.fname == fname
                        break
                    elif a == 2:
                        new_lname = input("lname jadid ra vared konid ")
                        if new_lname != "":
                            contactlist.lname = new_lname
                        else:
                            contactlist.lname == lname
                        break
                    elif a ==3:
                        new_shommare = input("shomare jadid ra vared konid ")
                        if new_shommare != "":
                            contactlist.shommare = new_shommare
                        else:
                            contactlist.shommare == shommare
                        break
                    elif a == 4:
                        new_city = input("city jadid ra vared konid ")
                        if new_shommare != "":
                            contactlist.ciity = new_city
                        else:
                            contactlist.ciity = ciity
                        break
                    elif a == 5:
                        new_category = input("category jadid ra vared konid ")
                        if new_category !="":
                            contactlist.cattegory = new_category
                        else:
                            contactlist.cattegory = cattegory
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
        

 