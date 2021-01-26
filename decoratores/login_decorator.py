from session.session import Session
from src.view.loginlogout_view import Loginlogout_User
# from src.view.menue import Menu_View


def chek_login(function):
    def wrapper(*args):
        # print("s111", Session.get_session())
        if Loginlogout_User.login():
            # print("s222222", Session.get_session())
            function(args)
        else:
            print("first press 15 and logining")
    return wrapper
