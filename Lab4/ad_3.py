def parse_strs(strs: list[str]) -> list[str]:
    return list(map(lambda x: x.capitalize() + '.', strs))

print(parse_strs(["123", "abc", "", "_sd"]))