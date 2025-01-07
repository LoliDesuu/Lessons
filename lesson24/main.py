import re

class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name = open('products.txt', 'a')):
        self.__file_name = file_name
        self.__file_name.close()

    def get_products(self):
        with open('products.txt', 'r') as file:
            str_file = ''
            line = file.readline()

            while line:
                str_file += line
                line = file.readline()
        file.close()
        return str_file


    def add(self, *products: Product):
        str_file = self.get_products()
        list_of_products = str_file.split('\n')
        with open('products.txt', 'a') as file:
            for elem in products:
                elem = str(elem)
                if elem in list_of_products:
                    file.close()
                    print(f'Продукт {elem} уже есть в магазине.')
                else:
                    file.write(f'{elem}\n')
        file.close()

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())