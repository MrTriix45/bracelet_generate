"""
README.md

# 🧵 Générateur de Bracelet - Application Tkinter

Une application graphique Python pour générer et imprimer des bracelets personnalisés avec les champs : prénom, nom, taille (cm) et téléphone. L'interface prend en charge la traduction multilingue (FR, NL, EN) et est compatible avec un export en exécutable via PyInstaller.

---

## ✨ Fonctionnalités

- Interface graphique moderne via **ttkbootstrap**
- Changement de langue à la volée (**FR**, **NL**, **EN**)
- Impression des données saisies (fonctionnalité à connecter via `printing_task.py`)
- Support d’icône et d’image en-tête
- Compatible avec **PyInstaller** (mode `--onefile`)

---

## 📦 Dépendances

Assurez-vous d’avoir installé les bibliothèques suivantes :

```bash
pip install ttkbootstrap Pillow
