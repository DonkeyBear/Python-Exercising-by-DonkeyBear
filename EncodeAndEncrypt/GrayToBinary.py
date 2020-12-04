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

# 將格雷碼與二元碼作互斥或運算（二元碼之 MSB 對格雷碼第二位）
for i in range(1, len(grayList)):
    if grayList[i] == binaryList[i-1]:
        binaryList.append('0')
    if grayList[i] != binaryList[i-1]:
        binaryList.append('1')

# 將串列轉換成字串後印出
binaryOutput = ''.join(binaryList)
print('轉換為二元碼：' + binaryOutput)