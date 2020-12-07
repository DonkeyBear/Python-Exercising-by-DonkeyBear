from sys import exit as sysExit

upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

plainText = input()
plainText = input('請輸入要加密的內容（僅限英文）：')
plainList = [] 
plainList[:] = plainText
cipherList = []

for i in range(0, len(plainList)):
    if plainList[i] not in upperList and plainList[i] not in lowerList:
        print('qwdqwdwdqwwqdd')