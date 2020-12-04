from sys import exit as sysExit

modeCheck = input('【凱薩密碼轉換器】\n輸入 1 進入「加密模式」，\n輸入 2 進入「解密模式」：')

if modeCheck == 1:
    None
    sysExit()

if modeCheck == 2:
    None
    sysExit()

else:
    print('退出程式……')
    sysExit()

plainText = input()
plainList = [] 
plainList[:0] = plainText
cipherList = []