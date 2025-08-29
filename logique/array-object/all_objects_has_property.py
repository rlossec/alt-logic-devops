def all_objects_has_property(objects_list, property):
    for object_item in objects_list:
        if not object_item.get(property):
            return False
    return True


if __name__ == "__main__":
    pass