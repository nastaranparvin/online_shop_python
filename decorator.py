from session import Session

def is_Admin(function):
    def wrapper():
        if Session.is_admin():
            function()


return wrapper