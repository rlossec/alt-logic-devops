def group_by(objects_list: list, property: str) -> dict:
    pass


if __name__ == "__main__":
    # Usage fourni
    # Cas d'usage : Regroupement de produits par catégorie dans un e-commerce
    products = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
        {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
        {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
    ]
    print(group_by(products, 'category'))
    # {"Electronics": [...], "Clothing": [...]}