from collections import namedtuple, defaultdict

TupleProduct = namedtuple("TupleProduct",["name", "price", "weight"])

def group_by_name(products: list[TupleProduct]) -> defaultdict:
    group_products = defaultdict(list)
    
    for product in products:
        group_products[product.name].append(product)
    
    return group_products

p1 = TupleProduct("wood", 2100, 2.7)
p2 = TupleProduct("fabric", 3100, 1.0)
p3 = TupleProduct("steel", 5000, 6.0)
p4 = TupleProduct("wood", 2100, 5.1)

products = [p1,p2,p3,p4]

grouped_products = group_by_name(products)

for name, product in grouped_products.items():
    print(name,"->",product)