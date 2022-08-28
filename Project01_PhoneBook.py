#Add Function
def add():
    name=input("name : ")
    number=input(name + "'s phone : ")
    names.append(name)
    phones.append(number)
#Search Function
def  search(name):
    c = 0
    for x in range(len(names)):
        if name in  names[x] :
            print(names[x], ":",  phones[x])
            c += 1
    print(c)
#Remove Function
def remove(name):
    if  name in  names:
        i=names.index(name)
        phones.remove(phones[i])
        names.remove(names[i])
        print("you find and remove the name")
    else:
        print("no body in your contact")
#Edit Function
def  edit(name):
    for z in  range(len(names)):
        if name == names[z]:
            number=input(f"number {name} 's  :")
            phones[z]=number
            print("contact edited")
            return
    print("no body in your contact")
#Help Function
def help():
    print(" 1:add \n 2:search \n 3:remove \n 4:edit \n 5:contact list \n exit:close app \n Help")
#contact function
def contact():
    print(f"you have {len(names)} contacts")
    for t in range(len(names)):
        print(names[t], ":" ,phones[t])
    
#*********************************************************************
print(10*"*" ,"welcome to phone book" ,10*"*")
help()
names=[]
phones=[]
while True:
    answer=input("please select the numbr of 1 to 5 or exit or help: ")
    #***Add***
    if answer == "1" :
        number = int(input("please enter number of contacts :  "))
        for i in range(number):
            add()
        print("contact added")
    #***Search***
    elif answer == "2" :
        name2=input("name for search: ")
        search(name2)
    #***Remove***
    elif answer == "3" :
        name3= input("name for remove :")
        remove( name3)
    #***Edit***
    elif answer == "4" :
        name4=input("name for edit: ")
        edit(name4)
    #***contact***
    elif answer == "5":
        contact()
    #***Help***
    elif answer=="help":
        help()
    elif answer == "exit" :
            exit()
    else:
        print("not found , please go to help")
