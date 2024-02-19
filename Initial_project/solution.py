def calculator(n : int, m : int, li : list)->int:
    # ساخت لیست جدید بر اساس تقسیم‌بندی گروه‌ها
    grouped_list = []
    for i in range(0, n, m):
        group_sum = sum(li[i:i + m])
        grouped_list.append(group_sum)

    # محاسبه مقدار نهایی با ترتیب کم و زیاد کردن اعضا
    final_value = 0
    sign = 1
    for num in grouped_list:
        final_value += sign * num
        sign *= -1

    return final_value


