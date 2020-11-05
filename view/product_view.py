from productmain import Product


class Product_View :

    @classmethod
    def input_products(cls):
        name = input("name")
        price = input("price")
        categorey = input("categorey")
        off = input("off")
        if Product.save(cls, name: str = None, price: int = None, category: str = None, off: float = None):
            print("add product success")
        print("categorey isnt exist please first add categorey")

    @classmethod
    def input_update(cls)
        id = input("id")
        name = input("name")
        price = input("price")
        categorey = input("categorey")
        off = input("off")
            if Product.update_p(cls, id: int, name: str = None, price: int = None, category: str = None, off: float = None):
