import tkinter as tk
import tkinter.font as font
from os import path

from PIL import Image
from PIL import ImageTk

import utils as utils

bg_color: str = "#2E323C"
input_bg_color: str = '#3A4247'
fg_color: str = "#CFD0D3"
border_color: str = "#CFD0D3"
font_family: str = "Open Sans"

# Create root window
window_width: int = 418
window_height: int = 261
window = tk.Tk()
window.geometry(str(window_width) + "x" + str(window_height))
window.title("PX to VW converter")
window.iconbitmap(path.abspath(path.join(path.dirname(__file__), 'window_icon.ico')))
window.config(bg=bg_color)
window.resizable(False, False)

# Init fonts
font1 = font.Font(family=font_family, size=30)
font2 = font.Font(family=font_family, size=18)
font3 = font.Font(family=font_family, size=12)

# Top frame
top_frame = tk.Frame(window, bg=bg_color, width=window_width, height=window_height / 1.5)
top_frame.pack(anchor=tk.W)

# Viewport params
vw_label = tk.Label(top_frame, font=font3, text="Viewport width", bg=bg_color, fg=fg_color)
vw_label.grid(row=0, column=0, padx=(20, 0), pady=(30, 0), sticky=tk.W)

vw_input = tk.Entry(top_frame, font=font2, bg=input_bg_color, fg=fg_color, insertbackground=fg_color,
                    highlightthickness=1, highlightbackground=border_color, highlightcolor=border_color,
                    textvariable=tk.StringVar())
vw_input.grid(row=1, column=0, padx=(20, 0), pady=0, ipadx=20, ipady=3, sticky=tk.W)
vw_input.focus_set()

reset_icon_path = path.abspath(path.join(path.dirname(__file__), 'reset_icon.png'))
reset_button_image = ImageTk.PhotoImage(Image.open(reset_icon_path).resize((25, 25)))
reset_button = tk.Button(top_frame, image=reset_button_image, bg=bg_color, activebackground=bg_color, relief=tk.FLAT,
                         borderwidth=0,
                         command=lambda: utils.clear_all(vw_input, pixels_input, result_label, copy_button))
reset_button.grid(row=1, column=1, padx=25)

# Pixels params
pixels_label = tk.Label(top_frame, font=font3, text="Size in px", bg=bg_color, fg=fg_color)
pixels_label.grid(row=2, column=0, padx=(20, 0), pady=(10, 0), sticky=tk.W)

pixels_input = tk.Entry(top_frame, font=font2, bg=input_bg_color, fg=fg_color, insertbackground=fg_color,
                        highlightthickness=1, highlightbackground=border_color, highlightcolor=border_color,
                        textvariable=tk.StringVar())
pixels_input.grid(row=3, column=0, padx=(20, 0), pady=0, ipadx=20, ipady=3, sticky=tk.W)

enter_icon_path = path.abspath(path.join(path.dirname(__file__), 'enter_icon.png'))
enter_button_image = ImageTk.PhotoImage(Image.open(enter_icon_path).resize((35, 35)))
enter_button = tk.Button(top_frame, image=enter_button_image, bg=bg_color, activebackground=bg_color, relief=tk.FLAT,
                         borderwidth=0,
                         command=lambda: utils.convert_to_vw(window, vw_input, pixels_input, result_label, copy_button))
enter_button.grid(row=3, column=1, padx=25)

# Result frame
result_frame = tk.Frame(window, bg=bg_color, width=window_width)
result_frame.pack(anchor=tk.W)

# Result params
result_label = tk.Label(result_frame, font=font1, text="", bg=bg_color, fg=fg_color)
result_label.grid(row=0, column=0, padx=(20, 0), pady=(10, 0), sticky=tk.W)

copy_icon_path = path.abspath(path.join(path.dirname(__file__), 'copy_icon.png'))
copy_button_image = ImageTk.PhotoImage(Image.open(copy_icon_path).resize((25, 25)))
copy_button = tk.Button(result_frame, image=copy_button_image, bg=bg_color, activebackground=bg_color, relief=tk.FLAT,
                        borderwidth=0, command=lambda: utils.copy_to_clipboard(window, result_label.cget('text')))

window.event_delete("<<Paste>>")
window.event_delete("<<Cut>>")
window.event_delete("<<Copy>>")
window.event_delete("<<SelectAll>>")
window.unbind_all("<<NextWindow>>")
window.bind_all("<Return>", lambda event: enter_button.invoke())
window.bind_all("<Escape>", lambda event: reset_button.invoke())
switcher = utils.TabSwitcher(False)
window.bind_all("<Tab>", lambda event: utils.tab_order(vw_input, pixels_input, switcher))
window.bind_all("<Key>", utils.on_key_release, "+")

if __name__ == '__main__':
    window.mainloop()
