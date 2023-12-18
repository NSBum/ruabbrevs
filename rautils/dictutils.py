def find_integer_key(dictionary):
    """
    Finds and returns the first key in the dictionary that can be converted to an integer.

    Args:
    dictionary (dict): The dictionary to search through.

    Returns:
    str: The key that can be converted to an integer, or None if no such key is found.
    """
    for key in dictionary.keys():
        try:
            int(key)  # Attempt to convert the key to an integer
            return key  # If successful, return the key
        except ValueError:
            continue  # If the key cannot be converted to an integer, continue to the next key

    return None  # Return None if no integer key is found
