import sys
import tkinter as tk
import tkinter.ttk as ttk

values = ('Shogi-dokoro', 'Shogi GUI')

"""
                 2  2     2  2         4  4
      1          1  2     6  7         7  8
   0  0          0  0     0  0         0  0
  0+--------------------------------------+
   |                                      |
 10|  +----------+           +---------+  |
   |  | Japanese |           | English |  |
 40|  +----------+           +---------+  |
 50|  +----------+           +---------+  |
   |  |          |           |         |  |
160|  |          |  +-----+  |         |  |
   |  |          |  | --> |  |         |  |
190|  |          |  +-----+  |         |  |
210|  |          |  +-----+  |         |  |
   |  |          |  | <-- |  |         |  |
240|  |          |  +-----+  |         |  |
   |  |          |           |         |  |
350|  +----------+           +---------+  |
   |                                      |
360+--------------------------------------+
"""
scale = 2

window = tk.Tk()
window.title(u"Tkinter practice")
# window.geometry("480x360")
window.geometry("960x720")

# [-->]ボタン
button1 = ttk.Button(window, text='-->').place(x=220*scale,
                                               y=160*scale, width=40*scale, height=30*scale)
# ,command=lambda: root.quit()
# [<--]ボタン
button1 = ttk.Button(window, text='<--').place(x=220*scale,
                                               y=210*scale, width=40*scale, height=30*scale)

# 左コンボボックス
left_combobox_value = tk.StringVar()
left_combobox_value.set("Shogi-dokoro")
left_combobox = ttk.Combobox(window, height=3, textvariable=left_combobox_value, values=values).place(
    x=10*scale, y=10*scale, width=200*scale, height=30*scale)

# 右コンボボックス
right_combobox_value = tk.StringVar()
right_combobox_value.set("Shogi GUI")
right_combobox = ttk.Combobox(window, height=3, textvariable=right_combobox_value, values=values).place(
    x=270*scale, y=10*scale, width=200*scale, height=30*scale)

# 左テキストエリア
left_text_area = tk.Text(window).place(
    x=10*scale, y=50*scale, width=200*scale, height=300*scale)

# 右テキストエリア
left_text_area = tk.Text(window).place(
    x=270*scale, y=50*scale, width=200*scale, height=300*scale)

window.mainloop()
