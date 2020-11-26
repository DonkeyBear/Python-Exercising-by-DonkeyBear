# 將 Markdown 中的標題貼上後，自動轉換成符合文法的錨點名稱。

while True:
    a = input('直接輸入 Enter 即可退出程式。\n請輸入標題：')
    if a == '':
        break
    '''
    a = a.lower().split('.') # 轉小寫，並以 . 為分界拆分字串為 list。
    a = (''.join(a)).split(' ') # 將 list 重新組合後，以空格為分界再次拆分字串為 list。
    a = '-'.join(a) # 將 list 用 # 重新組合
    '''
    # 將以上三句重新嵌套拼裝
    a = '-'.join((''.join(a.lower().split('.'))).split(' '))
    print('輸出結果為：#' + a, end='\n\n')