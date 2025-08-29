def find_intersection(objects_list_1: list, objects_list_2: list, property: str) -> list:
    ## Tester si les listes ont la propriété


    ## Sinon, retour d'info

    ## Si oui trouver les éléments

    pass

if __name__ == "__main__":
    # Cas d'usage : Trouver les livres disponibles dans deux bibliothèques
    library1 = [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True},
        {"id": 2, "title": "Dune", "author": "Herbert", "available": False}
    ]
    library2 = [
        {"id": 3, "title": "1984", "author": "Orwell", "available": True},
        {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
    ]
    # print(find_intersection(library1, library2, 'title'))
    # [{"id": 1, "title": "1984", "author": "Orwell", "available": True}]