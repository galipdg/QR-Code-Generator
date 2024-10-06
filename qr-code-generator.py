import pyqrcode
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr():
    url = url_input.get()
    scale = scale_var.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    try:
        qr = pyqrcode.create(url)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("SVG files", "*.svg")])
        if save_path:
            if save_path.endswith(".svg"):
                qr.svg(save_path, scale=scale)
            elif save_path.endswith(".png"):
                qr.png(save_path, scale=scale)
            else:
                messagebox.showerror("Error", "Unsupported file format! Please use .png or .svg extensions only.")
                return
            stat.config(text=f"QR Code successfully saved as '{save_path}' with scale {scale}")
        else:
            stat.config(text="Save operation canceled.")
    except Exception as e:
        stat.config(text=f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred while generating the QR code: {e}")

window = tk.Tk()
window.title("QR Code Generator")

label = tk.Label(window,text="Enter the URL")
url_input = tk.Entry(window,width=40)

scale = tk.Label(window, text="Select Scale:")
scale_var = tk.IntVar(value=12)
scale_options = [8,12,16,20]
scale_menu = tk.OptionMenu(window, scale_var, *scale_options)

button = tk.Button(window,text="Generate QR Code",command=generate_qr)
stat = tk.Label(window,text="")

label.grid(row=0,column=0,padx=10,pady=10)
url_input.grid(row=0,column=1,padx=10,pady=10)
button.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
stat.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
scale.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
scale_menu.grid(row=2,column=1,columnspan=2,padx=200,pady=10)

window.mainloop()