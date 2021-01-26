from decoratores.access_decoreate import check_access
from models.categorey import Categorey

class Categorey_View:

    @classmethod
    @check_access(access_admin=False, access_employee=True, access_customer=False)
    def new_categorey(cls)-> str:
        name= input("name ")
        if not Categorey.exist(name):
            return f"categorey with name {name} is creat" if Categorey.save(name) else "problem"
        else:
            return f"categorey {name} is exist"

    @classmethod
    @check_access(access_admin=False, access_employee=True, access_customer=False)
    def delet_categorey(cls):
        id = int(input("id"))
        return f"This categorey with id {id} is deleted" if Categorey.delete(id) else f"id {id} not found"
        # if Product.delet_p(id):
        #     return f"This product with id{id} is deleted"
        # else:
        #     return f"id {id} not found"


    @classmethod
    @check_access(access_admin=False, access_employee=True, access_customer=False)
    def update_categorey(cls):
        id = int(input("id"))
        name = (input("name"))
        print(Categorey.update_cat(id,name))


# print(Categorey_View.new_categorey())
# print(Categorey.get_all_catagorey())
# print(Categorey_View.new_categorey())
# print(Categorey.get_all_catagorey())
# print(Categorey_View.new_categorey())
# print(Categorey.get_all_catagorey())
# Categorey_View.update_categorey()
# print(Categorey.get_all_catagorey())
# print(Categorey_View.delet_categorey())
# print(Categorey.get_all_catagorey())
