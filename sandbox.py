from tkinter import PhotoImage
from tkinter import *
import ttkbootstrap as tk
from PIL import Image, ImageTk


def main():
    root = tk.Window(
        title= 'Printer_Bracelet',
    )
    root.geometry("800x800")

    # Build Icon

    ico = Image.open("img/359346.ico")
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    build_main_field(root) # Call for build my field of my Window

    return root

def build_main_field(master):

    # Build Style DEFAULT Frame

    style = tk.Style()
    style.configure("frame_style.TFrame", background="grey")
    style.configure("r0_style.TFrame", background="red")

    # Build Main Frame

    frm_main = tk.Frame(master, style = "frame_style.TFrame")
    frm_main.pack(
        expand = TRUE,
        fill = BOTH
    )

    for i in range(3):
        frm_main.rowconfigure(i, weight=1)

    # Build 3 row - Into _ frm_main

    r0 = tk.Frame(frm_main, borderwidth=5, relief="solid", height = 10, style = "r0_style.TFrame")
    r0.grid(
        row = 0,
        column = 0,
        sticky = "nsew"
    )
    for e in range(3):
        r0.columnconfigure(e, weight=1) #r0 - col 0, 1, 2

    r1 = tk.Frame(frm_main)
    r1.grid(
        row = 1,
        column = 0
    )

    r2 = tk.Frame(frm_main)
    r2.grid(
        row = 2,
        column = 0
    )

    fr_button = tk.Button(r0, text = "FR")
    fr_button.grid(
        row = 0,
        column = 0,
        sticky = "nsew"
    )

    fr_button = tk.Button(r0, text="NL")
    fr_button.grid(
        row = 0,
        column = 1
    )

    fr_button = tk.Button(r0, text="EN")
    fr_button.grid(
        row = 0,
        column = 2
    )


if __name__ == "__main__":
    main().mainloop()

# First Main - Build 1 Row ( 6 Buttons/Column )

    r1 = tk.Frame(frm_main)
    r1.grid(
        row = 0,
        column = 0,
        sticky = "nsew"
    )

    for j in range(6): # Build 6 Column

        frm_main.columnconfigure(j, weight=1)

    r2 = tk.Frame(frm_main)
    r2.grid(
        row=1,
        column=0,
        sticky="nsew"
    )

    # Label First Name + Entry

    label_firstname = tk.Label(r1, justify="right", text = "First Name :") # Label First Name + Entry
    label_firstname.grid(
        row = 0,
        column = 0,
        padx=3,
        pady = 3,
        sticky = "nsew"
    )

    entry_firstname = tk.Entry(
        r1
    )
    entry_firstname.grid(
        row = 0,
        column = 1,
        sticky = "nsew",
        padx=3,
        pady = 3
    )

    # Label Name

    label_name = tk.Label(r1, justify="right", text="Name :")  # Label Name + Entry
    label_name.grid(
        row=0,
        column=2,
        padx=3,
        pady=3,
        sticky="nsew"
    )

    entry_name = tk.Entry(
        r1
    )
    entry_name.grid(
        row=0,
        column=3,
        sticky="nsew",
        padx = 3,
        pady=3
    )

    # Birth Date + Age

    # Label Birth Date

    label_birth_date = tk.Label(r1, justify="right", text="Birth Date :")
    label_birth_date.grid(
        row=0,
        column=4,
        padx=3,
        pady=3,
        sticky="nsew"
    )

    birth_date = tk.DateEntry(r1, style = "success")
    birth_date.grid(
        row = 0,
        column = 5,
        sticky = "nsew",
        padx = 3,
        pady = 3
    )

    img = Image.open("img/test_error.png")
    img_resized = img.resize((25, 25))
    src_image = ImageTk.PhotoImage(img_resized)

    img_label = tk.Label(r1, image=src_image)
    img_label.image = src_image
    img_label.grid(
        row=0,
        column=6,
        padx=3,
        pady=3
    )