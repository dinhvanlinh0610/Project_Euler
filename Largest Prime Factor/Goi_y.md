Ta cần tìm ước số nguyên tố lớn nhất của số 600851475143.

Đầu tiên phải định nghĩa được số nguyên tố. Phần này chắc là dễ nhất rồi. Số nguyên tố là số chỉ có hai ước là 1 và chính nó.

**Ước số**: Nếu \( x \) có một ước số \( a \) lớn hơn căn bậc hai của \( x \), thì ước số còn lại \( b \) (tức là \( b = {x}/{a} )) sẽ phải nhỏ hơn căn bậc hai của \( x \). Điều này có nghĩa là nếu \( x \) có ước số, ít nhất một trong số các ước số đó sẽ nằm trong khoảng từ 2 đến căn bậc hai của \( x \).

```python
import math
def nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
```

---

Sau đó chúng ta kiểm tra từ 2 đến căn bậc 2 của 600851475143.

```python
list = []
for i in range(2,int(math.sqrt(target))):
    if target % i == 0 and nguyen_to(i):
        list.append(i)
```

--- 

Cùng nhau đến với 1 cách tiếp cận hoàn toàn khác

Ý tưởng ở đây là:
1. Bắt đầu với số nhỏ nhất: Ta khởi tạo 1 factor = 2 ( thừa số ), vì 2 là số nguyên tố nhỏ nhất.
2. Chia số n ( số cần tìm ước nguyên tố ) cho factor nếu factor là ước của n:
  -  Nếu n % factor == 0, nghĩa là factor là một ước số
  -  Ta chia n cho factor nhiều lần nhất có thể để loại bỏ hoàn toàn factor này ra khỏi n
  -  Gán lastFactor = factor để lưu lại ước số nguyên tố mới nhất
3. Tăng factor lên 1 và tiếp tục
  -  Sau khi loại bỏ hoàn toàn factor khỏi n, ta tăng factor lên để tìm ước số tiếp theo
4. Lặp lại cho tới khi n = 1:
  -  Khi n = 1 thì lastFactor chính thức là ước số nguyên tố lớn nhất

Hãy thử áp udnjg với n = 13195

## Giải thích từng bước với ví dụ nhỏ

### Ví dụ: `n = 13195`
Ta áp dụng thuật toán với `n = 13195`.

| Bước | Giá trị `factor` | `n` ban đầu | `n % factor == 0`? | Chia hết `n` cho `factor` | Cập nhật `lastFactor` |
|------|----------------|------------|-----------------|----------------------|------------------|
| 1    | 2              | 13195      | ❌ Không        | Giữ nguyên `n`      | Không đổi        |
| 2    | 3              | 13195      | ❌ Không        | Giữ nguyên `n`      | Không đổi        |
| 3    | 5              | 13195      | ✅ Có           | `n = 13195 / 5 = 2639` | `lastFactor = 5` |
| 4    | 6              | 2639       | ❌ Không        | Giữ nguyên `n`      | Không đổi        |
| 5    | 7              | 2639       | ✅ Có           | `n = 2639 / 7 = 377` | `lastFactor = 7` |
| 6    | 8 đến 12       | 377        | ❌ Không        | Giữ nguyên `n`      | Không đổi        |
| 7    | 13             | 377        | ✅ Có           | `n = 377 / 13 = 29`  | `lastFactor = 13` |
| 8    | 29             | 29         | ✅ Có           | `n = 29 / 29 = 1`    | `lastFactor = 29` |

Khi n = 1, ta dừng lại. Ước số nguyên tố lớn nhất là 29.

```python
def uoc_so_nguyen_to_lon_nhat(n):
    factor = 2
    lastFactor = 2
    
    while n!=1:
        if n % factor == 0:
            lastFactor = factor
            n = n / factor
        else:
            factor += 1
    return lastFactor
```
