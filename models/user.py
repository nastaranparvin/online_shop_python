from enume import RoleEnume

import itertools


class User:
    __db_user = [
        {
        "id_user":"1",
        "user_name" : "a",
        "password" : "a",
        "name": "nastaran",
        "familly" :"parvin",
            "role" : RoleEnume.ADMIN

        }
    ]
    __id_user= itertools.count(100)


    @classmethod
    def save_user(cls, name: str = None, familly: str = None, user_name: str = None, password: str = None, role:str = None) ->bool :
            user_item = {
                "id": str(next(cls.__id_user)),
                "name": name,
                "familly": familly,
                "user_name": user_name,
                "pasword": password,
                "role": role,
            }
            cls.__db_user.append(user_item)
            return True
    


    @classmethod
    def exist_user(cls, user_name: str = None) -> (dict):

        if user_name :
            for user in cls.__db_user:
                # print(">>>>>>>", user, user.get("user_name") == user_name)
                if user.get("user_name") == user_name :
                    return user
        return {}


    @classmethod
    def get_user(cls)-> list:
        return cls.__db_user





# obj1_save_admin= User()
# obj1_save_admin.register_user_admin("nastaran","parvin","09151035721","1234","admin")
# obj2_save_admin= User()
# obj2_save_admin.register_user_admin("nas","rvin","0916301721","4597","admin")
# obj3_save_admin= User()
# obj3_save_admin.register_user_employee("htjjs","uyukukn","09578901721","43247","employee")
# print(User.get_user())


