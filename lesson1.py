from microbit import *
#从  微电脑仓库  导入   所有

display.show(Image.HEART)
#显示器  显示  爱心

while True: #无限循环
  display.show(Image.HEART)  #对象.方法()
  #显示器  显示  爱心
  sleep(1000)
  #暂停1秒
  display.show(Image.HEART_SMALL)
  #显示器  显示  小爱心
  sleep(1000)
  #暂停1秒
