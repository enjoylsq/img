# 词霸每日一句，获取文本和分享图片链接,并转成Markdown形式
# 输出到剪贴板

import requests
import pyperclip



x = requests.get('https://open.iciba.com/dsapi/')
# d = json.loads(x.text)
# print(d)
# print(type(d))
# print(d['content'])

# print(type(x.json()))
t = x.json()

# print(t['content'])
# print(t['note'])
# print(t['fenxiang_img'])
image = t['fenxiang_img']

#重新封装图片
image = f"![]({image})"
content = t['content']+"\n"+t['note']+"\n"+image+"\n"

print(content)
pyperclip.copy(content)
