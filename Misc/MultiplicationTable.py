for i in range(2,10):
    for j in range(2,10):
        theList = str( str(j) + str(' × ') + str(i) + str(' = ') + str(i*j) )

        # 為了保持排版整齊，若算式長度小於 11，則迴圈加入空白以填滿
        while len(theList) < 11:
            theList = str(theList + ' ')

        # 換行判斷式
        if j != 9:
            print(theList + str(', '), end='')
        else:
            print(theList)