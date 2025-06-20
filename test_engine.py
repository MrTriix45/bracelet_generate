import pytest
import monmoteur as m

def test_tgo_size_file():
    size_value = 125
    m.tgo_size_file(size_value)
    assert "Categ_Taille/Cat 7.txt"

def test_printer_exist():
    printer_name = "HP3000"
    m.printer_exist(printer_name)
    assert printer_name