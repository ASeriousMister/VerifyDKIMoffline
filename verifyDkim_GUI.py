import email
import dkim
import os

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def show_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Information", message)
    root.destroy()  # Destroy the root window after showing the message


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.update()  # Update the window to ensure it stays hidden

    # Open the file dialog and store the selected file path
    file_path = filedialog.askopenfilename(title="Select email file (.eml)")

    # Destroy the root window after the file has been selected
    root.destroy()

    return file_path

def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.update()  # Update the window to ensure it stays hidden

    # Open the file dialog to select the first file
    file_path_1 = filedialog.askopenfilename(title="Select eml file (.eml)")
    if not file_path_1:
        print("No file selected for the first prompt.")
        root.destroy()
        return None, None
    
    # Open the file dialog to select the second file
    file_path_2 = filedialog.askopenfilename(title="Select the file containing the DKIM key")
    if not file_path_2:
        print("No file selected for the second prompt.")
        root.destroy()
        return file_path_1, None

    # Destroy the root window after both files have been selected
    root.destroy()

    return file_path_1, file_path_2


def verify_dkim_signature(eml_file):
    with open(eml_file, 'r') as f:
        msg = email.message_from_string(f.read())

    try:
        return dkim.verify(msg.as_bytes())
    except dkim.DKIMException:
        return False

eml_file, dkim_key = select_files()

temp_key_path = open('temp_key', 'w')
temp_key_path.write(dkim_key)
temp_key_path.close()

if verify_dkim_signature(eml_file):
    show_popup('DKIM signature is valid')
else:
    show_popup('DKIM signature is NOT valid')
os.remove('temp_key')
