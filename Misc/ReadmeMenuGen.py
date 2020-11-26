from chardet import detect as chardetDetect

# 透過 chardet 套件判斷 README.md 文件編碼
f_temp = open('README.md', 'rb')
readmeChardet = chardetDetect(f_temp.read())
readmeCodec = readmeChardet['encoding']
f_temp.close()

f_readme = open('README.md', 'r', encoding = readmeCodec)
asd = f_readme.read()
print(asd)