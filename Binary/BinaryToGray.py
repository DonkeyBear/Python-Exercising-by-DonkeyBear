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

for i in range(1, len(binaryList)):
    if binaryList[:-i] == binaryList[:-i-1]:
        grayList.insert(0, '0')
    if binaryList[:-i] != binaryList[:-i-1]:
        grayList.insert(0, '1')

grayList.insert(0, binaryList[0])