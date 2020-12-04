from sys import exit as sysExit

def encryptCaesar():
    plainText = input('請輸入要加密的內容（僅限英文）：')
    plainList = [] 
    plainList[:0] = plainText
    cipherList = []

def decryptCaesar():
    None

modeCheck = input('【凱薩密碼轉換器】\n輸入 1 進入「加密模式」，\n輸入 2 進入「解密模式」：')

# 加密模式
if modeCheck == 1:
    encryptCaesar()
    sysExit()

# 解密模式
if modeCheck == 2:
    decryptCaesar()
    sysExit()

else:
    print('退出程式……')
    sysExit()