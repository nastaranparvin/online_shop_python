from decoratores.access_decoreate import check_access
from enume import RoleEnume
from models.user import User

class Register_View:

    @classmethod
    # @chek_login
    @check_access(access_admin=True, access_employee=False, access_customer=False)
    def create_employee(cls):
        inputs=("user_name","pasword","name","familly",)
        user_name,password,name,familly= list(input(f"{inputt}: ") for inputt in inputs)

        if not User.exist_user(user_name):
            User.save_user(
                user_name=user_name,
                password=password,
                name= name,
                familly = familly,
                role=RoleEnume.EMPLOYEE
               )
            print(f" user {user_name} aded as employee" )
        else:
            print(f"user {user_name} already exist")

    @classmethod
    # @check_access(access_admin=True, access_employee=True, access_customer=True)
    def create_customer(cls):
        inputs = ("user_name", "pasword", "name", "familly",)
        user_name, password, name, familly = list(input(f"{inputt}: ") for inputt in inputs)
        if not User.exist_user(user_name):
            User.save_user(
                user_name=user_name,
                password=password,
                name=name,
                familly=familly,
                role=RoleEnume.CUSTOMER
            )
            print(f" user {user_name} aded as customer")
        else:
            print(f"user {user_name} already exist")


# Register_View.create_employee()
# print(User.get_user())