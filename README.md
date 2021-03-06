# Donkey Bear's Python Exercising

　　這裡是一個簡單的 Repo。用於放置一些我在學習 Python 中的練習作品，並藉由此 Repo 來熟悉 Git, GitHub, GitHub Desktop 的技術原理及使用方法。

## 目錄

> * [**Automate the boring stuff with Python**](#automate-the-boring-stuff-with-python)
>     * [birthday_dictionary.py](#birthday_dictionarypy)
>     * [print_a_heart.py](#print_a_heartpy)
>     * [tictactoe.py](#tictactoepy)
> * [**Encode and Encrypt**](#encode-and-encrypt)
>     * [BinaryToGray.py](#binarytograypy)
>     * [CaesarBrute-force.py](#caesarbrute-forcepy)
>     * [CaesarCipher.py](#caesarcipherpy)
>     * [GrayToBinary.py](#graytobinarypy)
>     * [MorseCode.py](#morsecodepy)
>     * [VigenereCipher.py](#vigenerecipherpy)
> * [**Misc**](#misc)
>     * [AnchorTrans.py](#anchortranspy)
>     * [Fibonacci.py](#fibonaccipy)
>     * [IntSumSeries.py](#intsumseriespy)
>     * [MultiplicationTable.py](#multiplicationtablepy)
>     * [NumSorter.py](#numsorterpy)
>     * [PrimeNumPrinter.py](#primenumprinterpy)
>     * [SentenceRandomRebuilder.py](#sentencerandomrebuilderpy)
>     * [TextReverser.py](#textreverserpy)
>     * [TimeUnitTrans.py](#timeunittranspy)
> * [**Tkinter**](#tkinter)
>     * [Rainbow.py](#rainbowpy)
>     * [Tkinter_BMIcalc.py](#tkinter_bmicalcpy)

## Automate the boring stuff with Python

　　依照《[Automate the boring stuff with Python](https://automatetheboringstuff.com/)》（另有簡體中譯本：《[Python編程快速上手 - 讓繁瑣工作自動化](https://www.books.com.tw/products/CN11361197)》）一書範例，經過個人改良後增加註解說明的程式練習。

### birthday_dictionary.py

　　輸入 `人名` 後，即可查詢該 `人名` 對應的 `生日`，若該 `人名` 在程式碼中無對應的 `生日`，則可自行輸入新建之。

### print_a_heart.py

　　以串列（list）搭配 `for` 迴圈，在終端印出由文字組成之愛心圖樣。

### tictactoe.py

　　使用字典（dictionary）繪製棋盤，進行雙人對戰的井字遊戲。

[返回目錄](#目錄)

## Encode and Encrypt

　　轉換編碼、加密、解密等程式作品。

### BinaryToGray.py

　　輸入 `二元碼`（binary code）後即可自動轉換為對應的 `格雷碼`（gray code）。

### CaesarBrute-force.py

　　用窮舉法，將凱薩密碼的偏移量從 1 ~ 25 全部列出來，達成最簡單的暴力破解。

### CaesarCipher.py

　　用於將文字加密為凱薩密碼，或將凱薩密碼解密成文字。

### GrayToBinary.py

　　輸入 `格雷碼`（gray code）後即可自動轉換為對應的 `二元碼`（binary code）。

### MorseCode.py

　　建置了英文、數字、標點符號、注音符號的摩斯電碼字典。目前無實際用途。

### VigenereCipher.py

　　用於將文字加密為維吉尼亞密碼，或將維吉尼亞密碼解密成文字。

[返回目錄](#目錄)

## Misc

　　雜項。即無特定範例或參考，隨意練習而作的小作品。

### AnchorTrans.py

　　輸入 Markdown 之下的標題名稱，即可自動轉換成符合文法的錨點標記。順便一提，這是我第一個為了實際需求所寫的 Python 程式，特此紀念。

### Fibonacci.py

　　以遞迴的方式印出費氏數列。

### IntSumSeries.py

　　輸入 `n`，輸出 `1 + 2 + ... + n` 之計算結果。

### MultiplicationTable.py

　　經過計算與排版後印出九九乘法表。

### NumSorter.py

　　輸入四個數字，依照大小重新排序，並指出最大與最小值。

### PrimeNumPrinter.py

　　輸入 `n`，產生由 `1` 到 `n (n >= 1)` 之間的所有質數。

### SentenceRandomRebuilder.py

　　將輸入的內容以空白為分界進行隨機重新排列。

### TextReverser.py

　　雙功能文字反轉器：

* 字串反轉。如：輸入 `abcdef`，則輸出 `fedcba`。
* 文字順序反轉。如：輸入 `see you later`，則輸出 `later see you`。

### TimeUnitTrans.py

　　輸入 `秒數`，自動將其轉換為「`時：分：秒`」。

[返回目錄](#目錄)

## Tkinter

　　使用 Python 內建的 GUI 函式庫 **Tkinter** 建立的範例與練習。

### Rainbow.py

　　用 Tkinter 視窗的背景色作為彩色漸變燈。

### Tkinter_BMIcalc.py

　　使用《[如何使用 Python Tkinter 製作 GUI 應用程式入門教學](https://blog.techbridge.cc/2019/09/21/how-to-use-python-tkinter-to-make-gui-app-tutorial/)》中的 BMI 計算器範例加以改良及增加註解標示，增加作為範例的可讀性。

[返回目錄](#目錄)