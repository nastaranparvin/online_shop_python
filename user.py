from enume import RoleEnume
from login import Login_User
import itertools


class User:
    __db_user = []
    __id_user= itertools.count(100)

    @Login_User.is_Admin
    @classmethod
    def register_user_admin(cls, name: str = None, familly: str = None, user_name: str = None, password: str = None, role:str = None) -> (
            bool, str):
        if not User.exist_user(user_name, password):
            user_item = {
                "id": next(cls.__id),
                "name": name,
                "familly": familly,
                "user_name": user_name,
                "pasword": password,
                "role": RoleEnume.ADMIN
            }
            return True
    
    @classmethod
    def register_user_employee(cls, name: str = None, familly: str = None, user_name: str = None, password: str = None, role:str = None) -> (
            bool, str):
        if not User.exist_user(user_name, password):
            user_item = {
                "id": next(cls.__id),
                "name": name,
                "familly": familly,
                "user_name": user_name,
                "pasword": password,
                "role": RoleEnume.EMPLOYEE
            }
            return True
        
    @classmethod
    def register_user_customer(cls, name: str = None, familly: str = None, user_name: str = None, password: str = None, role:str = None) -> (
            bool, str):
        if not User.exist_user(user_name, password):
            user_item = {
                "id": next(cls.__id),
                "name": name,
                "familly": familly,
                "user_name": user_name,
                "pasword": password,
                "role": RoleEnume.CUSTUMER
            }
            return True


    @classmethod
    def exist_user(cls, user_name: str = None, password: str = None) -> (dict):
        if user_name and password:
            for user in cls.__db_user:
                if user.get("user_name") == user_name and user.get("password") == password:
                    return user
        return {}

    @classmethod
    def exist_user_login(cls, user_name: str = None, password: str = None) -> (dict):
        if user_name and password:
            for user in cls.__db_login:
                if user.get("user_name") == user_name and user.get("password") == password:
                    return user
        return {}



