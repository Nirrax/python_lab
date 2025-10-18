def sum_of_digits(val: int) -> int:
    val = abs(val)
    output = 0
    while val > 0:
        output += val%10
        val = val//10
    return output
    
def factorial(val: int) -> int:
    if val < 0:
        raise ValueError("Cannot count factorial for negative number")
    i = 1
    output = 1
    while i <= val:
        output *= i
        i += 1
    return output
    