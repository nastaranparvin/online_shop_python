from enume import RoleEnume
from models.user import User


class Session:
    __db_session = []

    @classmethod
    def save(cls, user_name: str = None, role: str = None) -> bool:
        if user_name:
            user = User.exist_user(user_name)
            if user:
                if not cls.exist_sesion():
                    cls.__db_session.append(user)
                    return True

    @classmethod
    def exist_sesion(cls) -> bool:
        return True if cls.__db_session else False

    @classmethod
    def del_sesion(cls):
         cls.__db_session = []


    @classmethod
    def is_admin(cls) -> bool:

        user = Session.get_session()
        if user:
            if len(user) > 0 and user[0].get("role") == RoleEnume.ADMIN:
                return True
            return False

    @classmethod
    def is_employee(cls) -> bool:
        user = Session.get_session()
        if user:
            if len(user) > 0 and user[0].get("role") == RoleEnume.EMPLOYEE:
                return True
            return False

    @classmethod
    def is_customer(cls) -> bool:
        user = Session.get_session()
        if user:
            if len(user) > 0 and user[0].get("role") == RoleEnume.CUSTOMER:
                return True
            return False

    @classmethod
    def get_session(cls) -> list:
        return cls.__db_session


# Loginlogout_User.login()
# print(Session.get_session())
