# Bài Toán 1: Tính Tổng Các Bội Số của 3 hoặc 5 Nhỏ Hơn 1000

## 1. Mô Tả Bài Toán
Bài toán yêu cầu tính tổng tất cả các số là bội số của 3 hoặc 5 nhỏ hơn 1000.

Các số cần tính gồm:

```
3, 5, 6, 9, 10, 12, 15, ...
```

Cách đơn giản nhất là duyệt qua tất cả các số từ 1 đến 999, kiểm tra xem số đó có chia hết cho 3 hoặc 5 không, nếu có thì cộng vào tổng.

### Cách tiếp cận đầu tiên

```python
def tinh_tong(muc_tieu):
    tong = 0
    for i in range(1, muc_tieu ):
        if i % 3 == 0 or i % 5 == 0:
            tong += i
    return tong
```

## 2. Vấn Đề Hiệu Suất
Cách trên tuy đơn giản nhưng nếu mở rộng phạm vi lên đến 1,000,000,000 thì cách làm này sẽ rất chậm. Ngoài ra, biến `tong` có thể bị tràn dữ liệu.

Thay vì duyệt từng số, ta có thể dùng cách tính nhanh hơn bằng tổng cấp số cộng:

- Tổng các số chia hết cho 3.
- Tổng các số chia hết cho 5.
- Trừ đi tổng các số chia hết cho 15 (để loại bỏ số bị tính trùng).

## 3. Giải Thích Theo Cấp Số Cộng

### Công thức tổng cấp số cộng:

Dãy số có dạng:
```
a, a + d, a + 2d, ..., l
```
Với:
- `a` là số hạng đầu tiên.
- `d` là công sai (khoảng cách giữa hai số liên tiếp).
- `l` là số hạng cuối cùng.
- `n` là số lượng phần tử.

Tổng cấp số cộng:
```
S = (n/2) * (a + l)
```

Số hạng thứ `n` của một cấp số cộng được tính bằng công thức:
```
a + (n - 1) * d = x
```

Biến đổi để tìm `n`:
```
n = (x - a)/d + 1
```

Rút gọn công thức:
```
n = int(x/d)
```

Số hạng cuối cùng:
```
l = d * n = d * int(x/d)
```

Thay vào công thức tổng cấp số cộng:
```
S = d * int(x/d) * [1 + int(x/d)]/2
```

## 4. Áp Dụng Vào Bài Toán

Tổng các bội số của 3 và 5 nhỏ hơn 1000 (loại bỏ bội số của 15):
```
T = S(3) + S(5) - S(15)
```

Ta có:
```
x = 999
n(3) = (999 - 3) / 3 + 1 = 333
n(5) = (995 - 5) / 5 + 1 = 199
n(15) = (990 - 15) / 15 + 1 = 66
```

Từ đó:
```
T = 3 * [333 * (1 + 333)] / 2 + 5 * [199 * (1 + 199)] / 2 - 15 * [66 * (1 + 66)] / 2
  = 3 * 55611 + 5 * 19900 - 15 * 2211
  = 166833 + 99500 - 33165
  = 233168
```

## 5. Định Nghĩa Hàm

```python
def tong_cap_so_cong(a, muc_tieu):
    p = muc_tieu // a
    return a * (p * (p + 1)) // 2

tong = tong_cap_so_cong(3, 999) + tong_cap_so_cong(5, 999) - tong_cap_so_cong(15, 999)
print(tong)  # Kết quả: 233168
```

## 6. Giải Thích Hàm
Xét trường hợp `n = 3`:
```
3 + 6 + 9 + 12 + ... + 999 = 3 * (1 + 2 + 3 + ... + 333)
```

Tương tự, với `n = 5`:
```
5 + 10 + 15 + ... + 995 = 5 * (1 + 2 + ... + 199)
```

Với công thức tổng dãy số tự nhiên:
```
1 + 2 + 3 + ... + p = (p * (p + 1)) / 2
```

Từ đó, ta có thể viết hàm `tong_cap_so_cong(a, muc_tieu)` như trên.

## 7. Tổng Kết
Cách tiếp cận bằng cấp số cộng giúp bài toán chạy nhanh hơn đáng kể so với cách duyệt tuần tự, đặc biệt khi áp dụng với số lớn. Đây là phương pháp tối ưu để tính tổng các bội số trong phạm vi rộng.

---

Bằng cách này, ta không cần duyệt từng số mà vẫn tính được kết quả chính xác một cách hiệu quả.

