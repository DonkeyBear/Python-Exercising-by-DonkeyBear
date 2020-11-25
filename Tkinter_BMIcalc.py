# 範例來源：
# https://blog.techbridge.cc/2019/09/21/how-to-use-python-tkinter-to-make-gui-app-tutorial/

import tkinter as tk
import math

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title('BMI App')
window.geometry('300x150')
#window.configure(background='white')

# 定義區 -------------------------
def calculate_bmi_number():
    # height 變數擷取身高，weight 變數擷取體重，bmi_value 變數作BMI計算
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi_value = round(weight / math.pow(height, 2), 2)
    # 使用 str.format() 格式化字串函數
    result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    # 將計算結果更新到 result_label 文字內容
    result_label.configure(text=result)

def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'

# Tkinter區 --------------------

# pack() 為流水式排版，預設元件會依加入先後順序由上而下，由左而右自行排列
# 參數 side 為排列方向：TOP（預設）、BOTTOM、LEFT、RIGHT

# grid() 為表格式排版，元件是依據所指定的索引位置，如同二維陣列元素一般放入表格中
# place() 則可指定絕對或相對座標將元件精確擺放到視窗版面中
# 注意：一個視窗容器中不能同時使用 pack 與 grid 排版，但 place 卻可以與 pack 或 grid 同時使用
# http://yhhuang1966.blogspot.com/2018/10/python-gui-tkinter_12.html

header_label = tk.Label(window, text='BMI 計算器')
header_label.pack()

# 以 height 為名建立一個 frame，並將元件（身高的文字與輸入框）加入 frame
# 讓系統自動擺放元件，預設為由上而下（靠左）
height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
# 將 height 和 weight 的 label 都加上 width=10 的參數
# 讓兩個 label 的長度都固定為 10 個字元，用以對齊，方便排版
height_label = tk.Label(height_frame, text='身高（m）', width=10)
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

# 以 weight 為名建立一個 frame，並將元件（體重的文字與輸入框）加入 frame
weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）', width=10)
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

# calculate_btn 綁定 calculate_bmi_number 事件處理，點擊該按鈕會進行計算並印出 BMI
calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number)
calculate_btn.pack()

# 運行主程式
window.mainloop()