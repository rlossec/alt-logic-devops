## 1. Fonction qui prend une chaîne de caractères en paramètre et retourne sa longueur après avoir supprimé tous les espaces.

from typing import Any

def length_string(string: Any) -> int:
    if not isinstance(string, str):
        if isinstance(string, str|int|bool|float):
            string = str(string)
        else:
            return 0
    string_without_space = string.replace(' ', '')
    return len(string_without_space)



if __name__ == "__main__":
    
    assert length_string("Bonjour le monde !") == 15

    # Tests cas particuliers
    assert length_string("") == 0
    assert length_string(" ") == 0

    # Tests si le typage n'est pas string
    ## Si le type a une logique de conversion
    assert length_string(145) == 3
    assert length_string(1.5) == 3
    assert length_string(True) == 4
    assert length_string(False) == 5
    
    ## Si le type n'a pas de logique de conversion
    assert length_string(dict()) == 0
    assert length_string(None) == 0



          