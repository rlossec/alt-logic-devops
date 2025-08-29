## 1. Fonction qui prend une chaîne de caractères en paramètre et retourne sa longueur après avoir supprimé tous les espaces.

def length_string(string: str) -> int:
    
    string_without_space = string.replace(' ', '')
    return len(string_without_space)


if __name__ == "__main__":
    
    assert length_string("Bonjour le monde !") == 15

    # Tests cas particuliers
    assert length_string("") == 0
    assert length_string(" ") == 0

    # # Tests si le typage n'est pas string
    # ## Si le type est convertible
    # assert length_string(145) == 3

    # ## Si le type est convertible
    # assert length_string(dict()) == 0
    # assert length_string(None) == 0
    # assert length_string(True) == 0
    # assert length_string(False) == 0
    # assert length_string(1.5) == 0

          