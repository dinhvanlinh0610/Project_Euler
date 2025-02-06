total = 0
a, b = 2, 8  # Hai số Fibonacci chẵn đầu tiên
max_value = 4000000

while a <= max_value:
    total += a
    a, b = b, 4 * b + a  # Dùng công thức E(n) = 4E(n-1) + E(n-2)

print(total)
