a = 0
b = 1

# 據維基百科所述：0不是第一項，而是第零項。故此處以特例方式印出 0
print('0',end=' ')

while True:
    # 原本只需要 input() 就可以完成按一次 Enter 鍵即印出下一數字，
    # 但是終端機卻無法接著執行其他檔案，所以做了一個「輸入任何文字來跳出迴圈」的功能
    break_sign = input()
    if break_sign != '':
        break
    c = a + b
    print(b,end=' ')
    a = b
    b = c
