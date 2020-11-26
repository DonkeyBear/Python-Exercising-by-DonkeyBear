# 將 Markdown 中的標題貼上後，自動轉換成符合文法的錨點名稱。

while True:
    a = input('直接輸入 Enter 即可退出程式。\n請輸入標題：')
    if a == '':
        break
    a = a.lower().split('.')
    print('輸出結果為：#' + ''.join(a), end='\n\n')