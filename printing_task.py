from tkinter import messagebox
import win32print
from pathlib import Path
from unidecode import unidecode


def get_data_entries(data_entries):
    global ftgo
    first_data = data_entries["First"].get()
    name_data = data_entries["Name"].get()
    size_data = data_entries["Size"].get()
    tel_data = data_entries["GSM"].get()

    i_size = size_data = int(data_entries["Size"].get())

    if i_size < 80:
        file = Path("Categ_Taille/Cat 1.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 90:
        file = Path("Categ_Taille/Cat 2.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 100:
        file = Path("Categ_Taille/Cat 3.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 105:
        file = Path("Categ_Taille/Cat 4.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 110:
        file = Path("Categ_Taille/Cat 5.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 120:
        file = Path("Categ_Taille/Cat 6.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 130:
        file = Path("Categ_Taille/Cat 7.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 140:
        file = Path("Categ_Taille/Cat 8.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))
    elif i_size < 195:
        file = Path("Categ_Taille/Cat 9.txt")
        ftgo = (unidecode(file.read_text("utf-8", "ignore")))

    messagebox.showinfo("Infos :", f"Prenom : {first_data}\nName : {name_data}\nTaille : {size_data} cm\nGSM : {tel_data}")

    content = "^XA\n"
    content += f"^FO275,650^A0R,50,50^FDPrenom : {first_data}^FS\n"
    content += f"^FO225,650^A0R,50,50^FDNom : {name_data}^FS\n"
    content += f"^FO175,650^A0R,50,50^FDTaille : {size_data} cm^FS\n"
    content += f"^FO125,650^A0R,50,50^FDGSM : {tel_data}^FS\n"

    # Impression des attractions ligne par ligne
    x_position = 275
    y_position = 1300
    for line in ftgo.splitlines():
        content += f"^FO{x_position},{y_position}^A0R,25,25^FD{line}^FS\n"
        x_position -= 25

    content += "^XZ"

    printer_name = "ZDesigner HC100 300 dpi"
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Bracelet Print", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, content.encode("ascii"))
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)
