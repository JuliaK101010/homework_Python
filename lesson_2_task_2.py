def is_year_leap(year):
    return year % 4 == 0


# Выбираем год
year_to_check = 2028

result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")
