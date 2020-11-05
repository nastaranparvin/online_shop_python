from enume import RoleEnume
from user import User


class Session:

    @classmethod
    def is_admin(cls,user_name: str = None, password: str = None) -> bool:
        user = User.exist_user(user_name, password)
        if user:
            if user.get("role") == RoleEnume.ADMIN :
                return True
            return False

    @classmethod
    def is_employee(cls,user_name: str = None, password: str = None) -> bool:
        user = User.exist_user(user_name, password)
        if user:
            if user.get("role") == RoleEnume.EMPLOYEE :
                return True
            return False

    @classmethod
    def is_customer(cls,user_name: str = None, password: str = None) -> bool:
        user = User.exist_user(user_name, password)
        if user:
            if user.get("role") == RoleEnume.CUSTOMER :
                return True
            return False


