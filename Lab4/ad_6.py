import datetime

def logger(func) -> None:
    """
    This function logs to file which function was when called with what args and kwargs
    :param func: Function to log
    """
    def wrapper(*args, **kwargs):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.datetime.now()} | "
                f"{func.__name__} | "
                f"args={args}, kwargs={kwargs}\n"
            )
        return func(*args, **kwargs)
    return wrapper

@logger
def adder(a: int, b: int) -> int:
    return a+b

@logger
def printer(s="") -> None:
    print(s)
    
@logger
def kwarger(**kwargs) -> None:
    print(kwargs)
    
adder(1, 2)
printer()
printer("Print")
kwarger(a=2, b="abc")