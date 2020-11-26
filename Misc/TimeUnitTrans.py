# 將輸入之秒數轉換成「時:分:秒」。如輸入 10000，則輸出 02:46:40。

# 在Python3中，'/'為除，'//'為求除法整數，'%'為求除法餘數。
print('請輸入秒數：')
v_sec = input()
v_min = int(v_sec) // 60
v_hr  = int(v_min) // 60
v_sec = int(v_sec) % 60
v_min = int(v_min) % 60
print(str(v_hr) + '：' + str(v_min) + '：' + str(v_sec))
input() #用於暫停