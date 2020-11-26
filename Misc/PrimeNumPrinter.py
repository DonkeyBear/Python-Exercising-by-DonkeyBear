# 產生由 1 到 n (n >= 1) 之間的所有質數。

while True:
    n = int(input('輸入正整數 n：'))
    while n < 1:
        print('格式錯誤，請重新輸入。')
        n = int(input('輸入正整數 n：'))

    prime_num = []

    #從 1 開始數數，把數到的數依序丟下去連除作驗證
    for i in range(1,n+1):
        for j in range(2,i+1):
            if j == i:
                prime_num.append(i)
            if (i%j) == 0:
                break

    print('1,', str(prime_num)[1:-1], '\n由 1 到', n, '共有', len(prime_num) + 1, '個質數。\n')