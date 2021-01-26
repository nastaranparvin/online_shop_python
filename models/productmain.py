from models.categorey import Categorey
import itertools


class Product:
    __db = []
    __id = itertools.count(100, 2)
    @classmethod
    def save(cls, name: str = None, price: int = None, categorey: str = None, off: float = None,categorey_id: str = None) -> (bool,str):
        # ctg = Categorey.exist(categorey)
        # if ctg:
        p = {
            "id": next(Product.__id),
            "name": name,
            "price": int(price),
            "off": float(off),
            "categorey_id": str(categorey_id)
        }
        cls.__db.append(p)
        return True ,

        # if not name or not price or not categorey or not off:
        #     return False, f"name :{name} or price :{price} or categorey :{categorey}or off {off} not found
        # for categorey in Categorey().get_all_catagorey():
        #     if categorey.get("name") == name:

    @classmethod
    def get_product_db(cls):
        return cls.__db

    @classmethod
    def __repr__(cls):
        return cls.name

    @classmethod
    def delet_p(cls, id:int) -> bool:
        if not id:
            return False

        for num, pro in enumerate(cls.__db, 0):
            if pro.get("id") == id:
                del cls.__db[num]
                return True
        return False

    @classmethod
    def update_p(cls, id: int, name: str = None, price: int = None, categorey: str = None, off: float = None) -> (
            bool, str):

        if int(id):
            for products in cls.__db:
                if int(id) == products.get("id"):
                    # print(products)
                    if categorey:
                        if Categorey.exist(categorey):
                            products["categorey"] = categorey
                        else:
                            return False, "categorey is new please first add categorey"
                    if name:
                        products["name"] = name
                    if price:
                        products["price"] = price
                    if off:
                        products["off"] = off

                    return True, "update successful"

            return False, "id not found"
        return False, "please Enter New Id :"
