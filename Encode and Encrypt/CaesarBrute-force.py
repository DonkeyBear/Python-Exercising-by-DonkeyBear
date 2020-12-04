from sys import exit as sysExit

upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


cipherText = input('【凱薩密碼窮舉解密器】\n請輸入要解密的內容：')
cipherList = [] 
cipherList[:] = cipherText
plainList = []

caesarKey = int(input('請輸入金鑰（偏移量）：'))
if caesarKey > 25:
    caesarKey = caesarKey % 26

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
print('解密後的內容為：' + plainText)