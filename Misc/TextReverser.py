# 一、字串反轉。如：輸入 abcdef，則輸出 fedcba。
# 二、文字順序反轉。如輸入 see you later，則輸出 later see you。

# 設計構想：
# 以 var_mode 變數代表選擇模式，1 為字串反轉器，2 為句子反轉器，不輸入則為退出。
# 檢測輸入內容是否為已有模式的代號，若否，則跳出錯誤並重新顯示選單。

while True:
    var_mode = str(input('輸入數字 1 進入字串反轉器，\n輸入數字 2 進入句子反轉器，\n或直接輸入 Enter 退出程式：'))
    
    if var_mode == str('1'):
        a = list(input())[::-1]
        print('輸出結果為：\n' + ''.join(a), end='\n\n')
    
    if var_mode == str('2'):
        a = input().split(' ')[::-1]
        print('輸出結果為：\n' + ' '.join(a), end='\n\n')
    
    if var_mode == '':
        break
    
    if var_mode not in ['1', '2','']:
        print('\n輸入格式錯誤！\n')
