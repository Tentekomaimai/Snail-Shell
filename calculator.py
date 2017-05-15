# coding: utf-8
import sys
try:
    x = input('式を入力:')
    print(float(x))
except:
    print("エラー")
    sys.exit()
y = input('計算を続けるには0 止めるには1を入力:')
while y == 0:
    try:
        x = input('Input :')
        print(float(x))
    except:
        print("エラー")
        sys.exit()
    y = input('計算を続けるには0 止めるには1を入力:')
if y == 1:
    print("終了します")
    sys.exit()
else:
    print("エラー")
    sys.exit()
