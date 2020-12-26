from microbit import *
#从  微电脑仓库  导入   所有

while True: #无限循环
  if button_a.is_pressed() and button_b.is_pressed():
  #如果  A按下              并且   B也按下
    display.scroll('A+B') #滚动显示
  elif button_a.is_pressed(): #如果  A按下
    display.scroll('AAA') #滚动显示
  elif button_b.is_pressed(): #如果  B按下
    display.scroll('BBB') #滚动显示
  sleep(200)

  