Ý tưởng đơn giản nhất mà tôi nghĩ đến để giải quyết là:

Tạo dãy Fibonacci.

Kiểm tra số nào chẵn thì cộng vào tổng.

Trước kia khi mới học về Fibonaci mình được dạy tính bằng cách dùng đệ quy

```python
def fibonaci(x):
    if x == 0:
        return 0
    if x == 1 :
        return 1
    else: 
        return fibonaci(x-1) + fibonaci(x-2)
```
---

Vì mình vừa luyện giải thuật toán và vừa viết ra tài liệu này nên mình sẽ trình bày lại từ những đoạn code ban đầu tôi làm để giải bài này.

Cách giải quyết khá ngây ngô nhưng nó là suy nghĩ của mình.

```python
list = []
max = 4000000
i = 0
while True:
    if(fibonaci(i) > max):
        break
    elif fibonaci(i) %2 == 0:
        list.append(fibonaci(i))
    i+=1   
print(sum(list))
```

---

Nhận xét cách trên:

Đệ quy không phải là cách tối ưu cho bài toán này, vì mỗi lần gọi lại hàm lại tính lại các giá trị trước đó. 

Vòng lặp while của bạn thực hiện tốt việc dừng khi số Fibonacci vượt quá 4 triệu. 

Tuy nhiên, mỗi lần trong vòng lặp bạn gọi fibonaci(i) ba lần: một lần để kiểm tra giá trị, một lần để kiểm tra nếu nó chẵn, và một lần để thêm vào danh sách. Điều này làm tăng thời gian tính toán, vì mỗi lần gọi hàm đệ quy đều tốn tài nguyên.

Cách tối ưu:

Tính lại Fibonacci theo vòng lặp: Bạn có thể sử dụng một vòng lặp để tính số Fibonacci mà không cần đến đệ quy.

Tính tổng các số chẵn: Thay vì lưu trữ tất cả các số chẵn trong một danh sách, bạn có thể trực tiếp cộng vào tổng khi gặp số chẵn.

```python
total = 0
max_value = 4000000
c = 0
a = 0
b = 1
while c <= max_value:
    c = a + b
    a = b
    b = c
    
    if c % 2 == 0:
        total += c
    
print(total)
```

---

Cách trên đã khá tối ưu nhưng vẫn có thể cải thiện thêm 1 chút về mặt hiệu suất:

Sử dụng 2 biến thay vì 3: Bạn có thể giảm một biến c và chỉ cần duy trì hai biến a và b để tính số Fibonacci mà không cần phải lưu trữ giá trị c sau mỗi lần tính.

Không cần phải kiểm tra điều kiện trong vòng lặp: Thực tế, bạn có thể chỉ tính các số Fibonacci chẵn mà không cần phải duy trì tất cả các số Fibonacci. Điều này giúp giảm số lần tính toán, nhưng việc này chỉ hiệu quả nếu bạn muốn tối ưu thêm về mặt số lượng phép toán.

```python
total = 0
a, b = 1, 2
max_value = 4000000

while a <= max_value:
    if a % 2 == 0:
        total += a
    a, b = b, a + b 

print(total)

```

---

Lúc đầu mình nghĩ đây là cách tối ưu nhất rồi nhưng sau khi tìm hiểu thêm ở Project Euler thì mình thấy vài cách tiếp cận rất hay khác.

Cách này giúp chúng ta không cần kiểm tra số chẵn hay lẻ 

```python
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

```

---

Đây là một cách tiếp cận nữa

Chúng ta hãy quan sát chuỗi Fibonacci thì thấy rằng có 1 quy luật là mỗi số Fibonacci thứ 3 luôn là số chẵn

Dãy số Fibonacci có dạng:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
Các số chẵn: 2, 8, 34, 144...

Ta thấy các số chẵn xuất hiện ở vị trí  F(3), F(6), F(9), F(12), ...

Thay vì tính từng số Fibonacci và kiểm tra chẳn lẻ, ta chỉ cần tập trung vào các số chẵn trong dãy.

Nếu gọi E(n) là số Fibonacci chẵn thứ n, ta có;

E(1)=2

E(2)=8

E(3)=34

E(4)=144

Từ trên ta suy luận ra: E(n)=4*E(n−1)+E(n−2)  (144 = 4 * 34 + 8)

Dựa vào chuỗi Fibonacci ta nhận thấy F(n)=4F(n−3)+F(n−6)

Vì các số chẵn xuất hiện ở vị trí n=3k, ta có công thức trên đúng với tất cả các số Fibonacci chẵn.

F(n) = F(n-1) + F(n-2) 
= F(n-2)+F(n-3)+F(n-2)=2 F(n-2) + F(n-3) 

= 2(F(n-3)+F(n-4))+F(n-3))=3 F(n-3) + 2 F(n-4) 

= 3 F(n-3) + F(n-4) + F(n-5) + F(n-6) 

= 4 F(n-3) + F(n-6)

Ta có thể viết chương trình sau
Với công thức: E(n)=4⋅E(n−1)+E(n−2)

Bắt đầu với: 

E(1)=2

E(2)=8


```python
total = 0
a, b = 2, 8  # Hai số Fibonacci chẵn đầu tiên
max_value = 4000000

while a <= max_value:
    total += a
    a, b = b, 4 * b + a  # Công thức đặc biệt cho số Fibonacci chẵn

print(total)

```
