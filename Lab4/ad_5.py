def fun(*args, **kwargs) -> None:
    
    """
    This function prints *args as a list, save *kwargs in file, print dict if both are provided
    :param *args:
    :param *kwargs:
    """

    if args and not kwargs:
        print("Args (list):")
        print('\t'.join(map(str, args)))

    elif kwargs and not args:
        print("Kwargs (file) 'file.txt'")
        with open("file.txt", "w", encoding="utf-8") as f:
            for key, value in kwargs.items():
                f.write(f"| {key} | -> {value}\n")

    elif args and kwargs:
        print("Args and kwargs (dictionary):")
        arg = {}
        for i, value in enumerate(args, start=1):
            arg[f"arg{i}"] = arg
        arg.update(kwargs)
        print(arg)
        
fun(1, 2, 3, "test")
fun(imie="Jan", wiek=25)
fun(1, 2, miasto="Kraków", kraj="Polska")