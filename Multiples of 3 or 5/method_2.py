def tong_cap_so_nhan(x, muc_tieu):
    p = muc_tieu // x
    return x * (p * (p + 1))//2

print(tong_cap_so_nhan(3,999) + tong_cap_so_nhan(5, 999) - tong_cap_so_nhan(15,999))
