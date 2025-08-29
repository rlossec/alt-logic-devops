## 1. Fonction qui prend une chaîne de caractères en paramètre et retourne sa longueur après avoir supprimé tous les espaces.

def length_string(string: str) -> int:
    string_without_space = string.replace(' ', '')
    return len(string_without_space)


if __name__ == "__main__":
    assert length_string("Bonjour le monde !") == 15