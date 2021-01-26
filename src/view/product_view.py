from decoratores.access_decoreate import check_access
from models.categorey import Categorey
from models.productmain import Product


class Product_View :

    @classmethod
    @check_access(access_admin=False, access_employee=True, access_customer=False)
    def add_products(cls):
        name = input("name")
        price =int(input("price"))
        categorey = input("categorey")
        ctg = Categorey.exist(categorey)
        off =float( input("off"))
        categorey_id =ctg.get("id")
        if ctg:
            if Product.save( name, price, categorey, off,categorey_id):
                print("add product success")
        else:
            print("categorey isnt exist please first add categorey")

    @classmethod
    @check_access(access_admin=False, access_employee=True, access_customer=False)
    def delet_product(cls):
        id = int(input("id"))
        return f"This product with id {id} is deleted" if Product.delet_p(id) else f"id {id} not found"
        # if Product.delet_p(id):
        #     return f"This product with id{id} is deleted"
        # else:
        #     return f"id {id} not found"


    @classmethod
    # @chek_login
    @check_access(access_admin=False, access_employee=True, access_customer=False)
    def update_product(cls):
        filds = ("id", "name", "price", "category", "off")
        id, name, price, categorey, off = list(input(f"{filde}:") for filde in filds)
        print(Product.update_p(id, name, price, categorey, off))










# Categorey_View.new_categorey()
# print(Categorey.get_all_catagorey())
# Product_View.add_products()
# Product_View.add_products()
# Product_View.update_product()
# print(Product.get_product_db())
# print(Product_View.delet_product())
# print(Product.get_product_db())
# Product_View.add_products()
# Product_View.add_products()
#
