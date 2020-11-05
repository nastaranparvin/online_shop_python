from enume import RoleEnume
from user import User
class Login_User:
    __db_login=[]

    @classmethod
    def login(cls, user_name, password):
        if user_name and password:
            user = User.exist_user(user_name, password)
            if user:
                if  (len(cls.__db_login) == 0):
                    cls.__db_login.append(user)
                    if user.get("role") == RoleEnume.ADMIN:
                        return True, "admin"
                    elif user.get("role") == RoleEnume.EMPLOYEE:
                        return True, "employee"
                    elif user.get("role") == RoleEnume.CUSTUMER:
                        return True, "customer"
                return False, "you are already login"
            return False, "This username is Not Definde or password is incorrect"
        return False, "username or password is empty"


    @classmethod
    def exist_user_login(cls, user_name: str = None, password: str = None) -> (dict):
        if user_name and password:
            for user in cls.__db_login:
                if user.get("user_name") == user_name and user.get("password") == password:
                    return user
        return {}


    @classmethod
    def logout_user(cls):
        if cls.__db_login:
            cls.__db_login = []
            return True, f"user {user_name} is logout"
        return False, f"user_name {user_name} dont login"





