from categorey import Categorey
from productmain import Product
from user import User

terminate = {
    "0": "exit",
    "1": "Add product",
    "2": "Show product",
    "3": "Update product",
    "4": "Delete product",

    "5": "Add Category",
    "6": "Show Category",
    "7": "Update categories",
    "8": "Delet categories",

}
print("****welcome****")
for num, title in terminate.items():
    print(f' {num} : {title} ')
print("**************************")

booll, role = User.login(user_name, password)
print("please login and Enter the number 12")

num_user = input("enter your number : ")
print(num_user)

while True:

    if num_user == "5":
        name= input("name")
        if Categorey.save(name):
            print(f"success creat category {name}")
        else:
            print(f"categorey with name {name} is exist")

    if num_user == "2":
        print(Product().get_product_db())

    if num_user == "1":
        name = input("name")
        price = input("price")
        categorey = input("categorey")
        off = input("off")
        print((Product().save(name, price, categorey, off)))

    if num_user == "3":
        id = input("id")
        name = input("name")
        price = input("price")
        categorey = input("categorey")
        off = input("off")
        print((Product().update_p(id, name, price, categorey, off)))

    if num_user == "4":
        id = int(input("id"))
        print((Product().delet_p(id)))

    if num_user == "6":
        print(Categorey().get_all_catagorey())

    if num_user == "7":
        id = int(input("id"))
        name = input("name")
        print((Categorey().update_cat(id, name)))

    if num_user == "8":
        id = int(input("id"))
        print((Categorey().delete(id)))

    num_user = input("enter your number : ")

    if num_user == "12":
        user_name: str = input("please Enter your username:> ")
        password: str = input("please Enter your password :> ")
        if booll:
            if role == "admin":
                print("welcom ADMIN, you have access to numbers '[0 to 18]'")
                print("please Enter a number")
            elif role == "employee":
                print("welcom EMPLOYEE, you have access to numbers '[0 to 8 , 17, 18]'")
                print("please Enter a number")
            elif role == "customer":
                print("welcom CUSTOMER, you have access to numbers '[0 , 13, 14. 17, 18 ]'")
                print("please Enter a number")
        print({role})


