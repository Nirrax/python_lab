from statistics import median

def fun(*args) -> float:
    """
    This function calculates avg if *args is numbers, median of len if *args is strs
    :param *args:
    :return: avg if *args is numbers, median of len if *args is strs
    """
    
    
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args) / len(args) if args else 0

    elif all(isinstance(arg, str) for arg in args):
        lengths = [len(arg) for arg in args]
        return median(lengths) if lengths else 0

    else:
        print("Invalid args")
        return 0.0


print(fun(1, 2, 3, 4))
print(fun("apple", "banana", "kiwi"))
print(fun(1, "banana", 3))