def parse_strs(strs: list[str]) -> list[str]:
    """
    This function capitalize first letter of str and append dot at the end
    :param strs: List of strs
    :return: List of parsed strs
    """
    return list(map(lambda x: x.capitalize() + '.', strs))

print(parse_strs(["123", "abc", "", "_sd"]))