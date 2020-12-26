from microbit import *
#从  微电脑仓库  导入   所有

i = 0

while True: #无限循环
  if button_a.is_pressed() and button_b.is_pressed():
  #如果  A按下              并且   B也按下
    i = 0 #重置为0
  elif button_a.is_pressed(): #如果  A按下
    # 思考：加入判断不能超过10
    i = i + 1
  elif button_b.is_pressed(): #如果  B按下
    if 1 > 0: #判断是否大于0
      i = i - 1

  display.show(i)  #不用放到每个判断里
  sleep(200)

  