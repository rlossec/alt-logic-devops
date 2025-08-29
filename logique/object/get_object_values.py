
def get_object_values(object: dict) -> list:
    return list(object.values())


if __name__ == "__main__":
    scores = {
        "level1": 100,
        "level2": 85,
        "level3": 95
    }
    assert get_object_values(scores) == [100, 85, 95]

