max_value = 4000000
total = 0
a = 1 #( số thứ 1)
b = 1 #(số thứ 2)
c = a + b  # Fibonacci số thứ 3 (chẵn, số thứ 1 + số thứ 2)

while c < max_value:
    total += c # Cộng số thứ 3k vào tổng (3,6,9,...)
    a = b + c  # Cập nhật a thành số thứ 4 ( số thứ 2 + 3)
    b = c + a  # Cập nhật b thành số thứ 5 ( số thứ 3 + 4)
    c = a + b  # Cập nhật c thành số thứ 6 ( số thứ 4 + 5) 

print(total)
