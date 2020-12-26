from microbit import *
#从  微电脑仓库  导入   所有

import random #导入随机数仓库

while True: #无限循环
  if button_a.is_pressed(): #如果  A按下
    # 思考：加入判断不能超过10
    i = random.randint(0, 2)
    if i == 0: #如果为  #判断是否相同，要用两个=
      display.show(Image.SQUARE_SMALL)
    elif i == 1: #否则如果为
      display.show(Image.SQUARE)
    else: #否则
      display.show(Image.SWORD)
  elif button_b.is_pressed(): #如果  B按下
    display.show(Image.HEART) #显示心型

  sleep(200)

  