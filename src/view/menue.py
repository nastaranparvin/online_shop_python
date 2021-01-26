from models.categorey import Categorey
from models.productmain import Product
from models.user import User
from src.view.register_view import Register_View
from src.view.product_view import Product_View
from src.view.categorey_view import Categorey_View
from src.view.loginlogout_view import Loginlogout_User




class Menu_View :

    @classmethod
    def show_menu(cls):
        menue = {
            "0": "exit",
            "1": "Add product",
            "2": "Show product",
            "3": "Update product",
            "4": "Delete product",

            "5": "Add Category",
            "6": "Show Category",
            "7": "Update categories",
            "8": "Delet categories",

            "9": "Show user",
            "10": "Add Customer",
            "11": "Add employee",


            "12": "Buy products",
            "13": "Show orders",
            "14": "export csv of orders ( ./csv/datetime/*.csv )",

            "15": "login",
            "16": "logout",

            "17": "show menu",


        }
        print("****welcome****")
        for num, title in menue.items():
            if num in ("5","9","12","15","17","1"):
                print("*************************")
            print(f' {num} : {title} ')
        print("**************************")


        print("please login and Enter the number 15 ")

        num_user = input("Enter your number : ")
        print(num_user)

        while True:

            if num_user == "1":
                 Product_View.add_products()

            if num_user == "2":
                print(Product.get_product_db())

            if num_user == "3":
                Product_View.update_product()

            if num_user == "4":
               print(Product_View.delet_product())


            if num_user == "5":
                print(Categorey_View.new_categorey())


            if num_user == "6":
                print(Categorey.get_all_catagorey())

            if num_user == "7":
                Categorey_View.update_categorey()

            if num_user == "8":
                print(Categorey_View.delet_categorey())

            if num_user == "9":
                print(User.get_user())

            if num_user == "10":
                Register_View.create_customer()

            if num_user == "11":
                Register_View.create_employee()

            if num_user == "15":
                if Loginlogout_User.login():
                    print("login success")

            if num_user == "16":
                print(Loginlogout_User.logout_user())


            if num_user == "17":
                Menu_View.show_menu()


            num_user = input("Enter your number : ")


Menu_View.show_menu()





