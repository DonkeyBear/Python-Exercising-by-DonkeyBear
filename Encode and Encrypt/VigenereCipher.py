from sys import exit as sysExit

upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryptVigenere():
    plainText = input('請輸入要加密的內容（僅限英文）：')
    plainList = [] 
    plainList[:] = plainText
    cipherList = []

    vigenereKey = input('請輸入密鑰（僅限英文）：')

def decryptVigenere():
    None

#--------------------------------------------------------------------------------

modeCheck = input('【維吉尼亞密碼轉換器】\n輸入 1 進入「加密模式」，\n輸入 2 進入「解密模式」：')

# 加密模式
if modeCheck == '1':
    encryptVigenere()
    input()
    sysExit()

# 解密模式
if modeCheck == '2':
    decryptVigenere()
    input()
    sysExit()

else:
    print('退出程式……')
    sysExit()