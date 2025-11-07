from random import randrange
def gen_n_numbers(n: int) -> list[int]:
    output = []

    for i in range (0, n):
        val = randrange(-100, 100)
        if val > 0:
            output.insert(0, val)
            continue
        output.append(val)
    return output

print(gen_n_numbers(19))
