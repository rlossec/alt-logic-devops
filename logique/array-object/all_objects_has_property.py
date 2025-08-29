from typing import List, Dict

def all_objects_has_property(objects_list: List[Dict], key: str) -> bool:
    for object_item in objects_list:
        if not object_item.get(property):
            return False
    return True


if __name__ == "__main__":
    pass