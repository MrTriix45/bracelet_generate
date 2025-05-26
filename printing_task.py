from tkinter import messagebox
import win32print
from pathlib import Path
from unidecode import unidecode
import monmoteur as m


def get_data_entries(data_entries):
    global ftgo
    first_data = data_entries["First"].get()
    name_data = data_entries["Name"].get()
    size_data = data_entries["Size"].get()
    tel_data = data_entries["GSM"].get()

    i_size = size_data = int(data_entries["Size"].get())

    file = m.load_file(m.tgo_size_file(i_size))

    messagebox.showinfo("Infos :", f"Prenom : {first_data}\nName : {name_data}\nTaille : {size_data} cm\nGSM : {tel_data}")

    content = "^XA\n"
    content += f"^FO225,950^A0R,40,40^FDPrenom : {first_data}^FS\n"
    content += f"^FO175,950^A0R,40,40^FDNom : {name_data}^FS\n"
    content += f"^FO125,950^A0R,40,40^FDTaille : {size_data} cm^FS\n"
    content += f"^FO75,950^A0R,40,40^FDGSM : {tel_data}^FS\n"

    # Impression des attractions ligne par ligne
    x_position = 225
    y_position = 1450
    for line in file:
        content += f"^FO{x_position},{y_position}^A0R,40,25^FD{line}^FS\n"
        x_position -= 50

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
