import itertools

class Categorey :
    __db=[]
    __id= itertools.count(10)

    def save(self, name : str = None ) -> (bool , str) :
        if  not self.exist(name) :
            c= {
                "id" : next(self.__id),
                "name": name
            }
            self.__db.append(c)
            # id = next(self.__id)
            # self.__db.append({"id" : id , "name" : name})
            return True
        else:
            return False

    def delete(self, id: str =None) -> (bool, str):
        if not id:
            return False,'dont found id in parametr'
        for num , cat in enumerate(self.__db,0) :
            if cat.get("id") == id :
                del self.__db[num]
                return True,"deleted"
        return False,"not found"


    @classmethod
    def get_all_catagorey(cls):
        return (cls.__db)




    def exist(self, name : str = None) -> (dict):
        if name :
            for cat in self.__db :
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
            return False, "please Add new categorey"
        return False,"please Enter new id"




