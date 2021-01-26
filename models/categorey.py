import itertools

class Categorey :
    __db=[]
    __id= itertools.count(10)
    @classmethod
    def save(cls, name:str = None) -> bool :
        # if  not cls.exist(name) :
        c= {
            "id" : next(cls.__id),
            "name": name
        }
        cls.__db.append(c)
        # id = next(self.__id)
        # self.__db.append({"id" : id , "name" : name})
        return True


    @classmethod
    def delete(cls, id: int =None) -> bool:
        if not id:
            return False
        for num , cat in enumerate(cls.__db, 0) :
            if cat.get("id") == id :
                del cls.__db[num]
                return True
        return False


    @classmethod
    def get_all_catagorey(cls):
        return (cls.__db)



    @classmethod
    def exist(cls, name : str = None) -> (dict):
        if name :
            for cat in cls.__db :
                if cat.get("name") == name :
                    return cat
            return {}
        else:
            {}

    @classmethod
    def update_cat(cls,id:int, name: str = None) -> (bool, str):
        if id:
            for categorey in cls.__db :
                if id == categorey.get("id") :
                    if name:
                        categorey["name"] = name
                    return True,"update categorey"
        return False,"please Enter new id"




