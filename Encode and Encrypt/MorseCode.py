from sys import exit as sysExit

morseDict = {'a':'·-'   ,'b':'-···' ,'c':'-·-·' ,'d':'-··'  ,'e':'·'    ,
             'f':'··-·' ,'g':'--·'  ,'h':'····' ,'i':'··'   ,'j':'·---' ,
             'k':'-·-'  ,'l':'·-··' ,'m':'--'   ,'n':'-·'   ,'o':'---'  ,
             'p':'·--·' ,'q':'--·-' ,'r':'·-·'  ,'s':'···'  ,'t':'-'    ,
             'u':'··-'  ,'v':'···-' ,'w':'·--'  ,'x':'-··-' ,'y':'-·--' ,'z':'--··',

             '1':'·----','2':'··---','3':'···--','4':'····-','5':'·····',
             '6':'-····','7':'--···','8':'---··','9':'----·','0':'-----',

             '.':'·-·-·-', ':':'---···',',':'--··--',';':'-·-·-·','?':'··--··' ,
             '=':'-···-' ,'\'':'·----·','/':'-··-·' ,'!':'-·-·--','-':'-····-' ,
             '_':'··--·-','\"':'·-··-·','(':'-·--·' ,')':'-·--·-','$':'···-··-',
             '&':'·-···' ,'@':'·--·-·' ,'+':'·-·-·' }

morseDictZY = {'ㄅ':'-···','ㄆ':'·--··','ㄇ':'·--·' ,'ㄈ':'··-·-',
               'ㄉ':'·--' ,'ㄊ':'--·-' ,'ㄋ':'---·' ,'ㄌ':'···'  ,
               'ㄍ':'-··-','ㄎ':'--··-','ㄏ':'··--' ,
               'ㄐ':'-··' ,'ㄑ':'·-··-','ㄒ':'··--·',
               'ㄓ':'····','ㄔ':'-·-·' ,'ㄕ':'·-·'  ,'ㄖ':'·---'  ,
               'ㄗ':'···-','ㄘ':'-·-··','ㄙ':'-·-'  ,
               'ㄧ':'·'   ,'ㄨ':'-'    ,'ㄩ':'··-'  ,
               'ㄚ':'---' ,'ㄛ':'--'   ,'ㄜ':'-·--' ,'ㄝ':'--··'  ,
               'ㄞ':'·-·-','ㄟ':'··-··','ㄠ':'·-··' ,'ㄡ':'··-·'  ,
               'ㄢ':'·-'  ,'ㄣ':'-·'   ,'ㄤ':'--·'  ,'ㄥ':'··'    ,'ㄦ':'·---·'}