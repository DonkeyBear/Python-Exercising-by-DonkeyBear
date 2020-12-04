binaryInput = input()
binaryList = [] 
binaryList[:0] = binaryInput
grayList = []

# 檢查輸入是否為二元碼
for i in range(0, len(binaryList)):
    if binaryList[i] == '0' or binaryList[i] == '1':
        continue
    print('Error')
    break

# 從 LSB 往回作互斥或運算
for i in range(1, len(binaryList)):
    if binaryList[-i] == binaryList[-i-1]:
        grayList.insert(0, '0')
    if binaryList[-i] != binaryList[-i-1]:
        grayList.insert(0, '1')

# 將二元碼之 MSB 置於格雷碼之 MSB
grayList.insert(0, binaryList[0])

# 將串列轉換成字串後印出
grayOutput = ''.join(grayList)
print(grayOutput)