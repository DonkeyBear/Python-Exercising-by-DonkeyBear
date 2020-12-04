from sys import exit as sysExit

def encryptCaesar():
    plainText = input('請輸入要加密的內容（僅限英文）：')
    plainList = [] 
    plainList[:] = plainText
    cipherList = []
    upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    caesarKey = int(input('請輸入金鑰（偏移量）：'))
    if caesarKey > 25:
        caesarKey = caesarKey % 26

    for i in range(0, len(plainList)):
        if plainList[i].isupper == True:
            j = upperList.index(plainList[i])
            j += caesarKey
            if j > 25:
                j -= 26
            cipherList.append(upperList[j])

        if plainList[i].islower == True:
            j = lowerList.index(plainList[i])
            j += caesarKey
            if j > 25:
                j -= 26
            cipherList.append(lowerList[j])

        else:
            cipherList.append(plainList[i])

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