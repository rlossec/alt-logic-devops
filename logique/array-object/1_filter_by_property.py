# Pydantic pour le typage User


def filter_by_property(objects_list: list, property: str, value: any) -> list:
    return [object_item for object_item in objects_list if object_item[property] == value]


if __name__ == "__main__":
    users = [
        {"id": 1, "name": "Alice", "age": 25, "active": True},
        {"id": 2, "name": "Bob", "age": 30, "active": False},
        {"id": 3, "name": "Charlie", "age": 35, "active": True}
    ]
    print(filter_by_property(users, 'active', True))
    # [{"id": 1, "name": "Alice", "age": 25, "active": True}, {"id": 3, "name": "Charlie", "age": 35, "active": True}]
    print(filter_by_property(users, 'name', "Alice"))
    # [{"id": 1, "name": "Alice", "age": 25, "active": True}]

    # Tests
    assert filter_by_property(users, 'active', True) == [{"id": 1, "name": "Alice", "age": 25, "active": True}, {"id": 3, "name": "Charlie", "age": 35, "active": True}]
    assert filter_by_property(users, 'name', "Alice") == [{"id": 1, "name": "Alice", "age": 25, "active": True}]
