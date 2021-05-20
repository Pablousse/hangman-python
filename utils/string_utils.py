def pluralize(count: int) -> str:
    """Util function to put a string in plural when the count is bigger than 1

    Args:
        count (int): the number of time the string to pluralize is counted

    Returns:
        str: return s if the string should be put to plural
    """
    if count > 1:
        return "s"
    else:
        return ""
