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
    size_print = 35

    i_size = int(size_data)
    file = m.load_file(m.tgo_size_file(i_size))

    messagebox.showinfo(
        "Infos :",
        f"Prenom : {first_data}\nName : {name_data}\nTaille : {size_data} cm\nGSM : {tel_data}",
    )
    file_log = open("log.txt", "w")
    print(f"Prenom : {first_data}\nName : {name_data}\nTaille : {size_data} cm\nGSM : {tel_data}", file=file_log)
    file_log.close()

    # 1. Start ZBL
    content = "^XA\n"

    # 2. Load the label for the bracelet
    content += "^XFE:BRTAILLE.ZPL^FS\n"

    # 3. Placement du contenu dynamiquement sur mon bracelet
    content += f"^FO180,1500^A0B,{size_print},{size_print}^FDPrenom : {first_data}^FS\n"
    content += f"^FO150,1500^A0B,{size_print},{size_print}^FDNom : {name_data}^FS\n"
    content += (
        f"^FO120,1500^A0B,{size_print},{size_print}^FDTaille : {size_data} cm^FS\n"
    )
    content += f"^FO200,1500^A0B,{size_print},{size_print}^FDGSM : {tel_data}^FS\n"

    x_position = 250
    y_position = 1000
    for line in file:
        content += (
            f"^FO{x_position},{y_position}^A0R,{size_print},{size_print}^FD{line}^FS\n"
        )
        x_position -= 25

    # 4. Fin ZBL
    content += "^XZ"

    # 5. Envoie Job sur l'imprimante

    # Printer Exist or not
    printer_name = "ZDesigner HC100 300 dpi"
    if m.printer_exist(printer_name):
        messagebox.showinfo("PRINTER FOUND :", "Printer found")
        hPrinter = win32print.OpenPrinter(printer_name)
        try:
            hJob = win32print.StartDocPrinter(
                hPrinter, 1, ("Bracelet Print", None, "RAW")
            )
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, content.encode("ascii"))
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
    else:
        messagebox.showinfo("PRINTER NOT FOUND :", "Printer not found")

