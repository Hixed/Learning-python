#add function
def add() :
    number = int(input("enter number of products : "))
    for i in range(number):
        name = input(f"name of product {i+1} : ")
        if name not in products.keys():
            product = {}
            price = int(input(f"price of {name} : "))
            number_p = int(input(f"number of {name} : "))
            product.update({"price": price , "number": number_p})
            products[name] = product
            if number_p > 1 :
                print(f"{name} with {number_p} numbers added ")
            else :
                print(f"{name} with {number_p} number added ")
        else :
            print(f"{name} is already exist but you can add more")
#edit function
def edit() :
    name = input("please enter name for edit : ")
    if name in products.keys() :
        product = {}
        products.pop(name)
        new_name = input("please enter new name : ")
        number = int(input(f"please enter number of {new_name} : "))
        price = int(input(f"please enter price of {new_name} : "))
        product.update({"price": price , "number": number})
        products[new_name] = product
    else:
        print("not found")
#remove function
def remove() :
    name = input("please enter the name for remove : ")
    if name in products.keys() :
        products.pop(name)
    else:
        print("not found")
#show function
def show() : 
    for i in (products):
        print(f"name : {i} , price : {products[i]['price']} , number : {products[i]['number']}")
#search function
def search() :
    name = input("please enter your product name : ")
    if name in products.keys() :
        print(f"the {name} with {products[name]['price']} is available")
    else :
        print("sorry we don't have that product you want :) ")
#buy function
def buy() :
    name = input("please enter the name of product you want to buy it : ")
    number = int(input("please enter the number of product : "))
    if name in products.keys() and number <= products[name]["number"] :
        products[name]["number"] = products[name]["number"] - number
        if products[name]["number"] == 0 :
            remove(name)
        user_price = number * products[name]["price"]
    else :
        print("sorry we don't have that product you want :) ")
#checking function
def checking(admin , pass_admin) :
    name = input("please enter your name :")
    password = input("please enter your password : ")
    if name == admin and password == pass_admin:
        return True
    return False
#********************************************************************************************
products = {}
add()
show()
edit()
print(products)
admin = "ahmad"
pass_admin = "123456"
while True :
    answer1=input("choose your career \"admin/user\" : ")
    if answer1 == "admin" :
        while True:
            admin_answer = input("please select add / remove / edit / exit : ")
            if admin_answer == "add" :
                flag = checking(admin , pass_admin)
                if flag:
                    add() 
                else:
                    print("not correct")
            elif admin_answer == "remove" :
                remove()
            elif admin_answer == "edit" :
                edit()
            elif admin_answer == "exit" :
                break
            else :
                print(f"{admin_answer} not found :) ")
    elif answer1 == "user" :
        while True :
            user = input("please select search / show / buy / exit ")
            if user == "search" :
                search()
            elif user == "show" :
                show()
            elif user == "buy" :
                buy()
            elif user == "exit" :
                break
            else :
                print("not found")
    else :
        print("not found")
    exit1=input("do you want to exit ? y / n : ")
    if exit1.lower() == "y":
        break