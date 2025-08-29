from typing import List, Dict, Union
from all_objects_has_property import all_objects_has_property


def find_intersection(objects_list_1: List[Dict], objects_list_2: List[Dict], property: str) -> Union[List[Dict], str]:
    ## Tester si les listes ont la propriété
    if not all_objects_has_property(objects_list_1, property) or not all_objects_has_property(objects_list_2, property) :
        return f"Tous les objets n'ont pas la propriété {property}"
    
    ## Trouver les éléments
    return [object_item for object_item in objects_list_1 if object_item.get(property) in [object_item.get(property) for object_item in objects_list_2]]


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
    print(find_intersection(library1, library2, 'title'))
    # [{"id": 1, "title": "1984", "author": "Orwell", "available": True}]

    library3 = [
        {"id": 1, "title": "1984", "author": "Orwell", "available": True},
        {"id": 2, "title": "Dune", "author": "Herbert", "available": False}
    ]
    library4 = [
        {"id": 3, "author": "Orwell", "available": True},
        {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
    ]
    print(find_intersection(library3, library4, 'title'))