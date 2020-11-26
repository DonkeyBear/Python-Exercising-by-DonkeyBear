# 計算 1 + 2 + ... + n = ?

while True:
    n = int(input('請輸入整數 n：'))
    m = int(0)
    i = int(0)
    while (n+1) != m:
        i = i + m
        m += 1
    print('1 + 2 + ... + n =', i, '\n')