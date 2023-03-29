import tkinter as tk
import re


class TabSwitcher:
    def __init__(self, flag):
        self.flag = flag

    def set_flag(self, flag):
        self.flag = flag


def clear_text(entry: tk.Entry):
    entry.delete(0, tk.END)


def copy_to_clipboard(root: tk.Tk, text: str):
    root.clipboard_clear()
    root.clipboard_append(text)


def convert_to_vw(root: tk.Tk, vw_input: tk.Entry, pixels_input: tk.Entry, result_label: tk.Label,
                  copy_button: tk.Button):
    try:
        vw_input_var = int(vw_input.get())
        if vw_input_var == 0:
            vw_input.configure(textvariable=tk.StringVar())
            return
        pixels_var = float(re.sub('(?i)' + re.escape('px'), lambda m: '', pixels_input.get()))
        result = (pixels_var / vw_input_var) * 100
        round_number = 10 - int(result // 1).bit_length()
        result = round(result, round_number)
        result_label.configure(state=tk.NORMAL, text=str(result) + 'vw')
        copy_button.grid(row=0, column=1, padx=25, pady=(10, 0))
        copy_to_clipboard(root, result_label.cget('text'))
    except ValueError:
        result_label.configure(state=tk.NORMAL, text='Error')


def clear_all(vw_input: tk.Entry, pixels_input: tk.Entry, result_label: tk.Label, copy_button: tk.Button):
    clear_text(vw_input)
    clear_text(pixels_input)
    result_label.configure(text='')
    copy_button.grid_forget()
    vw_input.focus_set()


def tab_order(vw_input: tk.Entry, pixels_input: tk.Entry, switcher: TabSwitcher):
    if not switcher.flag:
        pixels_input.focus_set()
        switcher.set_flag(True)
        return
    vw_input.focus_set()
    switcher.set_flag(False)


def on_key_release(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 86 and ctrl:
        event.widget.event_generate("<<Paste>>")
    if event.keycode == 88 and ctrl:
        event.widget.event_generate("<<Cut>>")
    if event.keycode == 67 and ctrl:
        event.widget.event_generate("<<Copy>>")
    if event.keycode == 65 and ctrl:
        event.widget.event_generate("<<SelectAll>>")
