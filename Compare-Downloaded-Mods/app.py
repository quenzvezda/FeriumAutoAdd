import tkinter as tk
from tkinter import Listbox, Scrollbar, END
import difflib
import os

# Initialize main window
root = tk.Tk()
root.title("File Matcher")

# Create frames for each column
frame_left = tk.Frame(root)
frame_left.pack(side="left", fill="both", expand=True)

frame_middle = tk.Frame(root)
frame_middle.pack(side="left", fill="both", expand=True)

frame_right = tk.Frame(root)
frame_right.pack(side="left", fill="both", expand=True)

def normalize_string(s):
    return ''.join(e for e in s.replace(' ', '').lower() if e.isalnum())

def find_similar_files(base_mods, target_files):
    similar_files = {}
    normalized_target_files = [normalize_string(f) for f in target_files]

    for i, base_mod in enumerate(base_mods, 1):
        normalized_base_mod = normalize_string(base_mod)
        # Cari kata kunci di nama file target
        for target_file in normalized_target_files:
            if normalized_base_mod in target_file:
                # Jika kata kunci ditemukan, tambahkan ke daftar pencocokan
                similar_files[str(i) + '. ' + base_mod] = str(normalized_target_files.index(target_file) + 1) + '. ' + target_files[normalized_target_files.index(target_file)]
                break

    return similar_files

def update_matches():
    # Clear the current list
    listbox_matches.delete(0, END)
    
    # Find similar files
    matches = find_similar_files(base_files, target_files)
    
    # Dictionary to keep track of matched targets and their corresponding base indexes
    matched_targets = {}

    # Update the matches listbox and apply color coding
    for i, base in enumerate(base_files, 1):
        base_with_index = f"{i}. {base}"
        if base_with_index in matches:
            target = matches[base_with_index]
            listbox_matches.insert(END, f"{base_with_index} ditemukan pada {target}")
            
            # Check if this target has been matched before
            if target in matched_targets:
                # This target has been matched before, set the color to blue
                listbox_matches.itemconfig(END, {'fg': 'blue'})
                # Also set the previously matched base to blue
                previous_base_index = matched_targets[target]
                listbox_matches.itemconfig(previous_base_index, {'fg': 'blue'})
            else:
                # First time this target is matched, set color to black and store the index
                listbox_matches.itemconfig(END, {'fg': 'black'})
                matched_targets[target] = listbox_matches.size() - 1
        else:
            # Item did not match, add it to the matches listbox with red color
            listbox_matches.insert(END, f"{base_with_index} tidak ditemukan")
            listbox_matches.itemconfig(END, {'fg': 'red'})



# Base files listbox (left)
listbox_base = Listbox(frame_left)
listbox_base.pack(side="left", fill="both", expand=True)

# Scrollbar for base files listbox
scrollbar_base = Scrollbar(frame_left, orient="vertical")
scrollbar_base.config(command=listbox_base.yview)
scrollbar_base.pack(side="right", fill="y")
listbox_base.config(yscrollcommand=scrollbar_base.set)

# Matches listbox (middle)
listbox_matches = Listbox(frame_middle, width=50)
listbox_matches.pack(side="left", fill="both", expand=True)

# Target files listbox (right)
listbox_target = Listbox(frame_right)
listbox_target.pack(side="left", fill="both", expand=True)

# Scrollbar for target files listbox
scrollbar_target = Scrollbar(frame_right, orient="vertical")
scrollbar_target.config(command=listbox_target.yview)
scrollbar_target.pack(side="right", fill="y")
listbox_target.config(yscrollcommand=scrollbar_target.set)

current_directory = os.path.dirname(os.path.realpath(__file__))

base_filepath = os.path.join(current_directory, 'mods-base.txt')
target_filepath = os.path.join(current_directory, 'mods-target.txt')


def read_file_list(filepath):
    with open(filepath, 'r') as file:
        return file.read().splitlines()
    
# Read the file lists
base_files = read_file_list(base_filepath)
target_files = read_file_list(target_filepath)
    
# Populate the base and target listboxes
for i, file in enumerate(base_files, 1):
    listbox_base.insert(END, f"{i}. {file}")

for i, file in enumerate(target_files, 1):
    listbox_target.insert(END, f"{i}. {file}")

# Update button to find and display matches
update_button = tk.Button(frame_middle, text="Find Matches", command=update_matches)
update_button.pack(side="bottom")

root.mainloop()
