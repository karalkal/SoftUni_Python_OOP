from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):  # returns a product (object) with that name
        for this_product in self.products:
            if this_product.name == product_name:
                return this_product

    def remove(self, product_name):
        for this_product in self.products:
            if this_product.name == product_name:
                self.products.remove(this_product)

    def __repr__(self):
        result_dict = {}
        for item in self.products:
            article = item.name
            article_quantity = item.quantity
            result_dict[article] = article_quantity

        result_str = ""
        for k, v in result_dict.items():
            result_str += f"{k}: {v}\n"

        return result_str.strip()
