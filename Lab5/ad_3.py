class MathCalculations:
    @classmethod
    def sum_to_n(cls, n):
        return n * (n + 1) // 2

    @classmethod
    def factorial(cls, n):
        if n == 0:
            return 1
        else:
            return n * cls.factorial(n - 1)


calc = MathCalculations()

print(f"sum_to_n(10): {calc.sum_to_n(10)}")
print(f"factorial(5): {calc.factorial(5)}")
