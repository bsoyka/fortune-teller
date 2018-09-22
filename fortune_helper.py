def represents_int(string):
    """Used to check if str can be turned into an int
    Args:
        string - String to test
    Returns:
        True - string represents an int
        False - string does not represent an int
    """
    try:
        int(string)
        return True
    except ValueError:
        return False