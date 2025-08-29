from typing import Callable

def transform_values(object: dict, function: Callable) -> dict:
    return {key: function(value) for key, value in object.items()}


if __name__ == "__main__":
    
    # Tests 1
    prices_in_euros = {
        "book": 20,
        "pen": 5,
        "notebook": 10
    }
    to_dollars = lambda euros: euros * 1.1


    assert transform_values(prices_in_euros, to_dollars) == { "book": 22.0, "pen": 5.5, "notebook": 11.0 }
