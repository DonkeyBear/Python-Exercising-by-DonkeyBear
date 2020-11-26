# 句子重組器
# 將輸入的內容以空白為分界進行隨機重新排列。
import random
a = input().split()
b = []

j = len(a)
for i in range(j):
    k = random.randint(0,len(a)-1)
    b.append(a[k])
    a.remove(a[k])
    
print(' '.join(b))