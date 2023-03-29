import pyqrcode
import png
print("请输入您想要转换成二维码的文字")
s = input()
url = pyqrcode.create(s)
url.svg("E:\编程\项目\二维码.svg",scale = 8)
url.png("E:\编程\项目\二维码.png",scale = 6)
print(url.terminal())
