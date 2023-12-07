import os
import tkinter as tk
from tkinter import filedialog

def select_folder_and_save_list():
    # Mendapatkan path direktori %APPDATA%
    appdata_directory = os.getenv('APPDATA')

    # Memilih folder dengan %APPDATA% sebagai lokasi awal
    selected_folder = filedialog.askdirectory(initialdir=appdata_directory)
    if not selected_folder:
        # Pengguna membatalkan dialog, jadi tidak melakukan apa-apa
        return

    # Membuat daftar file dalam folder
    files_list = os.listdir(selected_folder)

    # Menyimpan daftar file ke "mods-target.txt" dalam direktori skrip Python
    current_directory = os.path.dirname(os.path.realpath(__file__))
    target_file_path = os.path.join(current_directory, 'mods-target.txt')

    with open(target_file_path, 'w') as file:
        for file_name in files_list:
            file.write(file_name + '\n')

    # Memberi tahu pengguna bahwa daftar telah disimpan
    label_status.config(text="Daftar file telah disimpan ke 'mods-target.txt'.")

# Membuat window GUI
root = tk.Tk()
root.title("File List Creator")

# Tombol untuk memilih folder
button_select_folder = tk.Button(root, text="Pilih Folder", command=select_folder_and_save_list)
button_select_folder.pack()

# Label status
label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()
