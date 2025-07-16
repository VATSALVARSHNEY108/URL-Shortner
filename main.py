import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_link():
    original_url = entry.get()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL to shorten.")
        return

    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(original_url)
        shortened_label.config(text=f"Shortened URL: {shortened_url}")
        copy_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_to_clipboard():
    shortened_url = shortened_label.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(shortened_url)
    messagebox.showinfo("Success", "Shortened URL copied to clipboard!")

root = tk.Tk()
root.title("Link Shortener")

label = tk.Label(root, text="Enter URL:")
label.pack()

entry = tk.Entry(root)
entry.pack()

shorten_button = tk.Button(root, text="Shorten", command=shorten_link)
shorten_button.pack()

shortened_label = tk.Label(root, text="")
shortened_label.pack()

copy_button = tk.Button(root, text="Copy Shortened URL", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

root.mainloop()
