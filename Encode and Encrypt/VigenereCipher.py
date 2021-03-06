from sys import exit as sysExit

upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryptVigenere():
    plainText = input('\n請輸入要加密的內容：\n（僅限英文，空白、符號及特殊字元維持原樣不加密）\n')
    plainList = [] 
    plainList[:] = plainText
    cipherList = []

    vigenereKey = input('\n請輸入密鑰：\n（僅限英文字母，不分大小寫，不可使用空白、符號及其他字元）\n').lower()
    keyList = []
    keyList[:] = vigenereKey
    k = 0

    for i in range(0, len(plainList)):
        if plainList[i].isupper() == True:
            j = upperList.index(plainList[i])
            j += lowerList.index(keyList[k])
            if j > 25:
                j -= 26
            cipherList.append(upperList[j])
            k += 1
            if k == len(keyList):
                k = 0
            continue

        if plainList[i].islower() == True:
            j = lowerList.index(plainList[i])
            j += lowerList.index(keyList[k])
            if j > 25:
                j -= 26
            cipherList.append(lowerList[j])
            k += 1
            if k == len(keyList):
                k = 0
            continue

        else:
            cipherList.append(plainList[i])

    cipherText = ''.join(cipherList)
    print('\n加密後的內容為：\n' + cipherText)

def decryptVigenere():
    cipherText = input('\n請輸入要解密的內容：\n')
    cipherList = [] 
    cipherList[:] = cipherText
    plainList = []

    vigenereKey = input('\n請輸入密鑰：\n').lower()
    keyList = []
    keyList[:] = vigenereKey
    k = 0

    for i in range(0, len(cipherList)):
        if cipherList[i].isupper() == True:
            j = upperList.index(cipherList[i])
            j -= lowerList.index(keyList[k])
            plainList.append(upperList[j])
            k += 1
            if k == len(keyList):
                k = 0
            continue

        if cipherList[i].islower() == True:
            j = lowerList.index(cipherList[i])
            j -= lowerList.index(keyList[k])
            plainList.append(lowerList[j])
            k += 1
            if k == len(keyList):
                k = 0
            continue

        else:
            plainList.append(cipherList[i])

    plainText = ''.join(plainList)
    print('\n解密後的內容為：\n' + plainText)

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