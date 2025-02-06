def tinh_tong(muc_tieu):
    tong = 0
    for i in range(1, muc_tieu ):
        if i % 3 == 0 or i % 5 == 0:
            tong += i
    return tong

print(tinh_tong(1000))
