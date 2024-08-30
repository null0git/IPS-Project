# gui/utils.py
import tkinter as tk
from tkinter import messagebox

def show_message(title, message):
    messagebox.showinfo(title, message)

def validate_ip(ip):
    import re
    pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                         r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                         r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                         r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$")
    return pattern.match(ip) is not None
