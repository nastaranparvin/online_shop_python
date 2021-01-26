from models.user import User
from session.session import Session

class Loginlogout_User :

    @classmethod
    def login(cls) -> bool:
        user_name = str(input("> enter your user_name : "))
        password = input("> enter your password : ")
        if user_name and password:
            user = User.exist_user(user_name)
            if user:
                if user.get("password") == password:
                    if Session.save(user.get("user_name")):
                        print(f"{user_name} is loggin")
                        return True
                else:
                    print(" pass dosnt correct")
                    return False
            else:
                print("this user dont exist")
                return False


    # @classmethod
    # def exist_user_login(cls, user_name: str = None, password: str = None) -> (dict):
    #     if user_name and password:
    #         for user in cls.__db_login:
    #             if user.get("user_name") == user_name and user.get("password") == password:
    #                 return user
    #     return {}
    #
    #
    @classmethod
    def logout_user(cls):
        if Session.exist_sesion():
            Session.del_sesion()
            return "user is logout"
        return "this user dont login"



# Loginlogout_User.login()
# print(Session.get_session())
