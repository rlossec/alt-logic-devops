
def get_object_values(object: dict) -> list:
    try:
        values = list(object.values())
    except AttributeError:
        return []
    return values


if __name__ == "__main__":
    scores = {
        "level1": 100,
        "level2": 85,
        "level3": 95
    }
    assert get_object_values(scores) == [100, 85, 95]

    # Test cas particuliers
    ## Objets vides
    assert get_object_values(object()) == []

    # Test si l'objet est un autre type
    assert get_object_values(True) == []
    assert get_object_values(None) == []
    assert get_object_values(1) == []
    assert get_object_values("Hello") == []
    assert get_object_values(dict()) == []
    assert get_object_values(list()) == []




