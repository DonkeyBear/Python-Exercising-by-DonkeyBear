# 輸入四個數字，找出最大與最小值。

v_num = [] #定義 v_num 為 List

while True:
    v_num.append(int(input('請輸入第一個數字：')))
    v_num.append(int(input('請輸入第二個數字：')))
    v_num.append(int(input('請輸入第三個數字：')))
    v_num.append(int(input('請輸入第四個數字：')))
    # .append() 用於將新資料加入 List

    print('你輸入的四個數字為：' , v_num[0] , ',' , v_num[1] , ',' , v_num[2] , ',' , v_num[3])
    v_num.sort(reverse=True)
    # .sort() 用於將 List 的內容物排序，預設是由小到大，括號內加入 reverse=True 即為由大到小
    
    print('由大到小，依序為：' , v_num[0] , ',' , v_num[1] , ',' , v_num[2] , ',' , v_num[3])
    print('最大值為' , v_num[0] , ',' , '最小值為' , v_num[3] , '\n')
