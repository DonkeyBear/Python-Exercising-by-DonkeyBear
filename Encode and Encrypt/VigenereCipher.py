from sys import exit as sysExit

upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vigenereDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def encryptVigenere():
    plainText = input('請輸入要加密的內容：\n（僅限英文，空白、符號及特殊字元維持原樣不加密）\n')
    plainList = [] 
    plainList[:] = plainText
    cipherList = []
    plainCount = 0

    vigenereKeyO = input('請輸入密鑰：\n（僅限英文字母，不分大小寫，不可使用空白、符號及其他字元）\n').lower
    vigenereKey = vigenereKeyO
    
    # 計算明文實際長度
    for i in range(0, len(plainList)):
        if plainList[i] in upperList or plainList[i] in lowerList:
            plainCount += 1

    # 調整密鑰長度以匹配明文長度
    while len(vigenereKey) < plainCount:
        vigenereKey += vigenereKeyO
    while len(vigenereKey) > plainCount:
        vigenereKey = vigenereKey[:len(vigenereKey)-1]

    


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