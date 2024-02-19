def calculate_floor(string: str) -> int:
    current_floor = 0  # ابتدا در طبقه‌ی همکف قرار داریم

    for move in string:
        if move == 'U':
            current_floor += 1
        elif move == 'D':
            current_floor -= 1

    return current_floor


# مثال: 'UDDU' به معنای رفتن به طبقه‌ی بالا، پایین، پایین، و دوباره بالا است.

result = calculate_floor('DDDD')
print(result)
