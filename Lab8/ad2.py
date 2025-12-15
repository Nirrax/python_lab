import re


def get_date(date: str) -> str:
    pattern = r"^(\d{2})\.(\d{2})\.(\d{4})( p\.n\.e)?$"
    match = re.match(pattern, date)

    if not match:
        return "Invalid date format"

    day, month, year, era = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        match.group(4),
    )
    if day > 31 or day < 1:
        return "Invalid day"
    if month > 12 or month < 1:
        return "Invalid month"
    if year > 2023 or year < 1:
        return "Invalid year"
    if era is not None:
        return f"Data: {day:02d}.{month:02d}.{year} przed naszą erą"

    return f"Data: {day:02d}.{month:02d}.{year} naszej ery"


print(get_date("01.01.2023"))
print(get_date("12.08.0450"))
print(get_date("25.12.1000 p.n.e"))
print(get_date("31.04.2023"))
print(get_date("01.01.2025"))
