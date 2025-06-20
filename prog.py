from tkinter import PhotoImage
from tkinter import *
import ttkbootstrap as tk
from PIL import Image, ImageTk
import printing_task as pt
import monmoteur as m
import sys
import os
import gettext

# pyinstaller --onefile --add-data "img/359346.ico;img" --windowed  --name bracelet_taille prog.py
lang = "fr"

localedir = os.path.join(os.path.abspath("."), "locales")
lang_trans = gettext.translation(
    "base", localedir=localedir, languages=[lang], fallback=True
)
lang_trans.install()

_ = lang_trans.gettext


def resource_path(relative_path):
    """
        Retourne le chemin absolu vers une ressource, compatible avec l'utilisation via PyInstaller.

        Args:
            relative_path (str): Chemin relatif vers la ressource.

        Returns:
            str: Chemin absolu vers la ressource.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = None

# Build Main

def main():
    """
       Initialise la fenêtre principale de l'application, configure son icône,
       et construit l'interface utilisateur.

       Returns:
           ttkbootstrap.Window: La fenêtre principale initialisée.
    """
    global root
    root = tk.Window(
        title="Générateur Bracelet",
    )
    root.geometry("650x500")

    # Build Icon

    ico = Image.open(resource_path("img/359346.ico"))

    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    build_main_field(root)  # Call for build my field of my Window

    return root

# Build Translate

def translate_prog(lang_code):
    """
        Met à jour la langue de l'interface en fonction du code de langue donné.

        Args:
            lang_code (str): Code de la langue à utiliser (ex : 'fr', 'nl', 'en').
    """
    global _
    lang = gettext.translation(
        domain="base", localedir="locales", languages=[lang_code], fallback=True
    )
    lang.install()
    _ = lang.gettext
    rebuild_ui()

# Build Rebuild

def rebuild_ui():
    """
        Reconstruit l'interface utilisateur pour refléter la langue sélectionnée.
        Détruit tous les widgets existants et les reconstruit.
    """
    for widget in root.winfo_children():
        widget.destroy()
    build_main_field(root)

# Build Main Field

def build_main_field(master):
    """
        Construit les éléments principaux de la fenêtre : entête, boutons, champs de saisie et pied de page.

        Args:
            master (tk.Widget): Le conteneur parent (typiquement la fenêtre principale).
    """

    # Build Main Frame

    frm_main = tk.Frame(master, style="frame_style.TFrame")
    frm_main.pack(expand=TRUE, fill=BOTH)

    for i in range(4):
        frm_main.rowconfigure(i)  # 0, 1, 2, 3
        frm_main.columnconfigure(0, weight=1)

    frm_main.rowconfigure(2, weight=1)
    # Build 3 row - Into _ frm_main

    r0 = tk.Frame(frm_main, borderwidth=5, relief="solid", style="r0_style.TFrame")
    r0.grid(row=0, column=0, sticky="nsew")

    r1 = tk.Frame(frm_main, style="r1_style.TFrame")
    r1.grid(row=1, column=0, sticky="nsew")
    for e in range(3):
        r1.columnconfigure(e, weight=1)  # r1 - col 0, 1, 2
    build_buttons(r1)

    r2 = tk.Frame(frm_main, style="r2_style.TFrame")
    r2.grid(row=2, column=0, sticky="nsew")
    for a in range(4):
        r2.rowconfigure(a, weight=0)  # r2 - row 0, 1, 2, 3
    for b in range(3):
        r2.columnconfigure(b, weight=0)  # r2 - col 0, 1, 2

    r3 = tk.Frame(frm_main, style="r3_style.TFrame")
    r3.grid(row=3, column=0, sticky="nsew")

    # Call Building Functions Into Container (Frame)

    build_header_image(r0)
    build_buttons(r1)
    build_main_label_entry(r2)
    build_footer(r3)

# Build Buttons

def build_buttons(container):
    """
        Crée les boutons de sélection de langue (FR, NL, EN) dans le conteneur fourni.

        Args:
            container (tk.Widget): Le widget parent où ajouter les boutons.
    """
    but_padx = 3
    but_pady = 3
    but_width = 1

    style_but = tk.Style()
    style_but.configure("TButton", background="grey", width=but_width, relief="raised")

    langs = {"FR": "fr", "NL": "nl", "EN": "en"}
    col = 0
    for label, code in langs.items():
        lang_button = tk.Button(
            container, text=label, command=lambda c=code: translate_prog(c)
        )
        lang_button.grid(row=0, column=col, sticky="nsew", padx=but_padx, pady=but_pady)
        col += 1

# Build Image Logo - Header

def build_header_image(container):
    """
        Affiche le logo/une image d'en-tête dans le conteneur fourni.

        Args:
            container (tk.Widget): Le widget parent pour l'image.
    """
    img = Image.open(resource_path("img/359346.ico"))

    img_resized = img.resize((100, 100))
    src_image = ImageTk.PhotoImage(img_resized)

    container.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)

    img_label = tk.Label(container, image=src_image)
    img_label.image = src_image
    img_label.grid(row=0, column=0, sticky="n")

# Build Main Label & Entry

def build_main_label_entry(container):
    """
        Crée les champs de saisie pour les informations personnelles et un bouton d'impression.

        Args:
            container (tk.Widget): Le widget parent pour les champs et le bouton.
    """
    size_lbl = 13
    size_ety = 35

    label_text = {
        "first_label": "Prénom :",
        "name_label": "Nom :",
        "size_label": "Taille (cm) :",
        "gsm_label": "Téléphone :",
    }
    lb_col = 0
    lb_row = 0

    for label, code in label_text.items():
        label = tk.Label(container, text=_(code), width=size_lbl)
        label.grid(row=lb_row, column=lb_col, sticky="nsew")
        lb_row += 1

    # Entry

    first_entry = tk.Entry(container, width=size_ety)
    first_entry.grid(row=0, column=1)

    name_entry = tk.Entry(container, width=size_ety)
    name_entry.grid(row=1, column=1)

    size_entry = tk.Entry(container, width=size_ety)
    size_entry.grid(row=2, column=1)

    gsm_entry = tk.Entry(container, width=size_ety)
    gsm_entry.grid(row=3, column=1)
    # Dictionary Entries

    all_entries = {
        "First": first_entry,
        "Name": name_entry,
        "Size": size_entry,
        "GSM": gsm_entry,
    }

    #  Button Printing

    container.columnconfigure(2, weight=1)
    print_button = tk.Button(
        container, text=_("Imprimer"), command=lambda: pt.get_data_entries(all_entries)
    )
    print_button.grid(column=2, row=0, rowspan=4, sticky="nsew")

# Build - Footer
def build_footer(container):
    """
        Affiche le pied de page de l'application avec un texte de copyright.

        Args:
            container (tk.Widget): Le widget parent pour le pied de page.
    """
    container.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)

    footer_label = tk.Label(
        container,
        text="© Copyright - WALIBI BELGIUM - v1",
        anchor="center",
        justify="center",
    )
    footer_label.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    main().mainloop()