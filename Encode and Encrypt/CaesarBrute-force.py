from sys import exit as sysExit

upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


cipherText = input('【凱薩密碼窮舉解密器】\n請輸入要解密的內容：')
cipherList = [] 
cipherList[:] = cipherText
plainList = []

# 金鑰範圍：1 ~ 25
for caesarKey in range(1, 26):
    plainList = []
    for i in range(0, len(cipherList)):
        if cipherList[i].isupper() == True:
            j = upperList.index(cipherList[i])
            j -= caesarKey
            plainList.append(upperList[j])
            continue

        if cipherList[i].islower() == True:
            j = lowerList.index(cipherList[i])
            j -= caesarKey
            plainList.append(lowerList[j])
            continue

        else:
            plainList.append(cipherList[i])

    plainText = ''.join(plainList)
    keyNum = str(caesarKey)
    if caesarKey < 10:
        keyNum = str(caesarKey) + ' '
    print('以 ' + keyNum + ' 作為金鑰解密後的內容為：' + plainText)

input()