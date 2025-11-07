def sort_by_chars_count(numbers: list[int]) -> None:
    strs = [str(abs(number)) for number in numbers]
    strs.sort(key= lambda x: len(x))
    print(f"shortest number: {strs[0]} | longest number: {strs[-1]}")

sort_by_chars_count([21, 51, -1, 222, 0])