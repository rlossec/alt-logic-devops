from typing import List, Dict, Union
from filter_by_property import filter_by_property

def group_by(objects_list: List[Dict], property: str) -> Dict[str, List[Dict]]:
    return { object_item[property]: filter_by_property(objects_list, property, object_item[property]) for object_item in objects_list}



if __name__ == "__main__":
    # Usage fourni
    # Cas d'usage : Regroupement de produits par catégorie dans un e-commerce
    products = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
        {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
        {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
    ]
    print(group_by(products, 'category'))
    # {'Electronics': [{'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 999}, {'id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 699}], 'Clothing': [{'id': 3, 'name': 'T-shirt', 'category': 'Clothing', 'price': 29}]}

    assert group_by(products, 'category') == {'Electronics': [{'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 999}, {'id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 699}], 'Clothing': [{'id': 3, 'name': 'T-shirt', 'category': 'Clothing', 'price': 29}]}