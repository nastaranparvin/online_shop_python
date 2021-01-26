from session.session import Session
from enume import RoleEnume
from src.view.loginlogout_view import Loginlogout_User


def check_access(access_admin:bool= False, access_employee:bool= False, access_customer:bool= False):
    def decoratore(function):
        def wrapper(*args , **kwargs):
            if Session.exist_sesion():
                if ((access_admin and Session.is_admin()) or (access_employee and Session.is_employee()) or (access_customer and Session.is_customer()) ):
                    function(*args , **kwargs)
                else:
                    message = "this option access only"
                    acceses=list()
                    if access_admin:
                        acceses.append(f"\"{RoleEnume.ADMIN}\"")
                    if access_customer:
                        acceses.append(f"\"{RoleEnume.CUSTOMER}\"")
                    if access_employee:
                        acceses.append(f"\"{RoleEnume.EMPLOYEE}\"")
                    message+= "and" .join(acceses)
                    print(message)
            else:
                print("you dont login")
                Loginlogout_User.login()
        return wrapper
    return decoratore



