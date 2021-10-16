import sys
import tkinter as tk

window = tk.Tk()
window.title(u"Tkinter practice")
window.geometry("480x360")

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

# 左テキストエリア
left_text_area = tk.Text(window).place(x=10, y=50, width=200, height=300)

# 右テキストエリア
left_text_area = tk.Text(window).place(x=270, y=50, width=200, height=300)

window.mainloop()
