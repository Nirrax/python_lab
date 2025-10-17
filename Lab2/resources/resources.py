def mean_and_median_from_list(vals: list[int | float]) -> tuple[float, float]:
    mean = sum(vals) / len(vals)

    vals_len = len(vals)
    sorted_vals = sorted(vals)
    if vals_len%2 != 0:
        median = sorted_vals[(vals_len//2)]
    else:
        median = (sorted_vals[(vals_len//2) - 1] + sorted_vals[(vals_len//2)]) / 2

    return float(mean), float(median)

def sorted_list_from_tuple(vals: tuple[int, ...]) ->list[int]:
    return sorted([x for x in vals])

def count_empty_fields_in_matrix(matrix: list[list[int|None]]) -> int:
    counter = 0
    for row in matrix:
        for val in row:
            if val is None:
                counter += 1
    return counter

