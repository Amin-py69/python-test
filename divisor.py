n = int(input())
divisors_sum = 0

# بررسی همه مقسوم‌علیه‌ها به جز n خودش
for i in range(1, n):
    if n % i == 0:
        divisors_sum += i

# بررسی آیا مجموع مقسوم‌علیه‌ها برابر با n است
if divisors_sum == n:
    print("YES")
else:
    print("NO")