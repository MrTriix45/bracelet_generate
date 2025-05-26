from tkinter import PhotoImage
from tkinter import *
import ttkbootstrap as tk
from PIL import Image, ImageTk
import printing_task as pt
import monmoteur
import sys
import os


#pyinstaller --onefile --add-data "img/359346.ico;img" --windowed  --name bracelet_taille prog.py
def resource_path(relative_path):
    try:
        # PyInstaller crée un dossier temporaire accessible via _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    root = tk.Window(
        title= 'Générateur Bracelet',
    )
    root.geometry("500x450")

    # Build Icon

    ico = Image.open(resource_path("img/359346.ico"))

    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    build_main_field(root) # Call for build my field of my Window

    return root

def build_main_field(master):

    # Build Style DEFAULT Frame

    style = tk.Style()
    style.configure("frame_style.TFrame", background="grey")
    style.configure("r0_style.TFrame", background="red")
    style.configure("r1_style.TFrame", background="green")

    # Build Main Frame

    frm_main = tk.Frame(master, style = "frame_style.TFrame")
    frm_main.pack(
        expand = TRUE,
        fill = BOTH
    )

    for i in range(3):
        frm_main.rowconfigure(i)
        frm_main.columnconfigure(0, weight=1)

    frm_main.rowconfigure(2, weight=1)
    # Build 3 row - Into _ frm_main

    r0 = tk.Frame(frm_main, borderwidth=5, relief="solid", style = "none")
    r0.grid(
        row = 0,
        column = 0,
        sticky = "nsew"
    )

    r1 = tk.Frame(frm_main, borderwidth=5, relief="solid", style = "r1_style.TFrame")
    r1.grid(
        row = 1,
        column = 0,
        sticky = "nsew"
    )
    for e in range(3):
        r1.columnconfigure(e, weight=1) #r1 - col 0, 1, 2
    build_buttons(r1)


    r2 = tk.Frame(frm_main, style = "frame_style.TFrame")
    r2.grid(
        row = 2,
        column = 0,
        sticky = "nsew"
    )
    for a in range(3):
        r2.rowconfigure(a, weight = 0) #r2 - row 0, 1, 2, 3
    for b in range(2):
        r2.columnconfigure(b, weight = 0) #r2 - col 0, 1, 2

    # Call Building Functions Into Container (Frame)

    build_header_image(r0)
    build_buttons(r1)
    build_main_label_entry(r2)

def build_buttons(container):

    fr_button = tk.Button(container, text = "FR")
    fr_button.grid(
        row = 0,
        column = 0,
        sticky = "nsew"
    )

    fr_button = tk.Button(container, text="NL")
    fr_button.grid(
        row = 0,
        column = 1,
        sticky = "nsew"
    )

    fr_button = tk.Button(container, text="EN")
    fr_button.grid(
        row = 0,
        column = 2,
        sticky = "nsew"
    )

# Build Image Logo - Header

def build_header_image(container):

    img = Image.open(resource_path("img/359346.ico"))

    img_resized = img.resize((100, 100))
    src_image = ImageTk.PhotoImage(img_resized)

    container.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)

    img_label = tk.Label(container, image=src_image)
    img_label.image = src_image
    img_label.grid(
        row=0,
        column=0,
        sticky="n"
    )

def build_main_label_entry(container):

    size_lbl = 10
    size_ety = 35

    # Label

    first_label = tk.Label(container, text = "Prénom :", width = size_lbl)
    first_label.grid(
        row = 0,
        column = 0,
        sticky = "ns"
    )
    name_label = tk.Label(container, text="Nom :", width = size_lbl)
    name_label.grid(
        row=1,
        column=0,
        sticky = "ns"
    )
    size_label = tk.Label(container, text="Taille (cm) :", width = size_lbl)
    size_label.grid(
        row=2,
        column=0,
        sticky = "ns"
    )
    gsm_label = tk.Label(container, text="Téléphone :", width=size_lbl)
    gsm_label.grid(
        row=3,
        column=0,
        sticky="ns"
    )

    # Entry

    first_entry = tk.Entry(container, width = size_ety)
    first_entry.grid(
        row = 0,
        column = 1
    )

    name_entry = tk.Entry(container, width = size_ety)
    name_entry.grid(
        row = 1,
        column=1
    )

    size_entry =tk.Entry(container, width = size_ety)
    size_entry.grid(
        row = 2,
        column = 1
    )

    gsm_entry =tk.Entry(container, width = size_ety)
    gsm_entry.grid(
        row = 3,
        column = 1
    )

    # Dictionary Entries

    all_entries = {
        "First": first_entry,
        "Name": name_entry,
        "Size": size_entry,
        "GSM": gsm_entry
    }

    #  Button Printing

    container.columnconfigure(2, weight=1)
    print_button = tk.Button(container, text = "Print", command = lambda: pt.get_data_entries(all_entries))
    print_button.grid(
        column = 2,
        row = 0,
        rowspan = 4,
        sticky = "nsew"

    )



if __name__ == "__main__":
    main().mainloop()