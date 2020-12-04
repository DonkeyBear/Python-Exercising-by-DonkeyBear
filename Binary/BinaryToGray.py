binaryInput = input()
binaryList = [] 
binaryList[:0] = binaryInput

for i in range(0, len(binaryList)):
    if binaryList[i] == '0' or binaryList[i] == '1':
        continue
    print('Error')
    break