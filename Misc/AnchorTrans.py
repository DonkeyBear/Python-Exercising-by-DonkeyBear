# 將 Markdown 中的標題貼上後，自動轉換成符合文法的錨點名稱。
from pyperclip import copy  as pclipCopy
from pyperclip import paste as pclipPaste

print('直接按下 Enter 會自動貼上標題，輸入 000 可退出程式。')

while True:
    a = input('請輸入標題：')
    if a == '000':
        break
    if a == '':
        a = pclipPaste()
        print(a)
    a = '#' + '-'.join((''.join(a.lower().split('.'))).split(' '))
    pclipCopy(a)
    print('輸出結果為：' + a + '\n　　　　　（已複製到剪貼簿。）\n')