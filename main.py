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
 50|  +----------+  +-----+  +---------+  |
   |  |          |  | --> |  |         |  |
   |  |          |  +-----+  |         |  |
   |  |          |  +-----+  |         |  |
   |  |          |  | <-- |  |         |  |
350|  +----------+  +-----+  +---------+  |
   |                                      |
360+--------------------------------------+
"""

window = tk.Tk()
window.title(u"Tkinter practice")
window.geometry("480x360")

# 左コンボボックス
left_combobox_value = tk.StringVar()
left_combobox = ttk.Combobox(window, height=3, textvariable=left_combobox_value, values=values).place(
    x=10, y=10, width=200, height=30)

# 右コンボボックス
right_combobox_value = tk.StringVar()
right_combobox = ttk.Combobox(window, height=3, textvariable=right_combobox_value, values=values).place(
    x=270, y=10, width=200, height=30)

# 左テキストエリア
left_text_area = tk.Text(window).place(x=10, y=50, width=200, height=300)

# 右テキストエリア
left_text_area = tk.Text(window).place(x=270, y=50, width=200, height=300)

window.mainloop()
