from sys import exit as sysExit

grayInput = input('請輸入格雷碼：')
grayList = [] 
grayList[:0] = grayInput
binaryList = []

# 檢查輸入是否為二元碼
for i in range(0, len(grayList)):
    if grayList[i] == '0' or grayList[i] == '1':
        continue
    print('Error')
    sysExit()
    break

# 將格雷碼之 MSB 置於二元碼之 MSB
binaryList.append(grayList[0])

# 
for i in range(1, len(grayList)):
    if grayList[-i] == grayList[-i-1]:
        grayList.insert(0, '0')
    if grayList[-i] != grayList[-i-1]:
        binaryList.insert(0, '1')

# 將串列轉換成字串後印出
binaryOutput = ''.join(binaryList)
print('轉換為二元碼：' + binaryOutput)