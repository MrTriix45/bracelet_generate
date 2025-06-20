from pathlib import Path
from unidecode import unidecode
import win32print


def tgo_size_file(size_value: int):
    if 50 <= size_value < 80:
        return "Categ_Taille/Cat 1.txt"
    elif 80 <= size_value < 90:
        return "Categ_Taille/Cat 2.txt"
    elif 90 <= size_value < 100:
        return "Categ_Taille/Cat 3.txt"
    elif 100 <= size_value < 105:
        return "Categ_Taille/Cat 4.txt"
    elif 105 <= size_value < 110:
        return "Categ_Taille/Cat 5.txt"
    elif 110 <= size_value < 120:
        return "Categ_Taille/Cat 6.txt"
    elif 120 <= size_value < 130:
        return "Categ_Taille/Cat 7.txt"
    elif 130 <= size_value < 140:
        return "Categ_Taille/Cat 8.txt"
    elif 140 <= size_value < 195:
        return "Categ_Taille/Cat 9.txt"
    else:
        raise ValueError(f"Aucune catégorie trouvée pour la valeur: {size_value}")


def load_file(path_file):
    # Exist File Words.txt in my dir .\

    file = Path(path_file)
    if not file.exists():
        raise FileNotFoundError("File not Found")
    else:
        ftgo = unidecode(file.read_text("utf-8", "ignore"))
    return ftgo.splitlines()


def printer_exist(printer_name):
    # Check the printer installed in Local
    printers = [
        printers[2]
        for printers in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
    ]

    # return the list
    return printer_name in printers
