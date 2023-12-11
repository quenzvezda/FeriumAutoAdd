def interleave_texts(text1, text2):
    # Pastikan kedua teks memiliki panjang yang sama
    if len(text1) != len(text2):
        raise ValueError("Panjang teks tidak sama")

    # Interleave karakter dari kedua teks
    interleaved_text = "".join([char1 + char2 for char1, char2 in zip(text1, text2)])
    return interleaved_text

# Membaca teks dari file
path_text1 = 'E:\\Github Private\\FeriumAutoAdd\\Compare-Downloaded-Mods\\YSV74.txt'
path_text2 = 'E:\\Github Private\\FeriumAutoAdd\\Compare-Downloaded-Mods\\WOS34.txt'

with open(path_text2, 'r', encoding='utf-8') as file:
    text2 = file.read()

with open(path_text1, 'r', encoding='utf-8') as file:
    text1 = file.read()

# Melakukan proses interleave
interleaved_text = interleave_texts(text1, text2)

# Opsional: Menyimpan teks gabungan ke file baru
output_path = 'E:\\Github Private\\FeriumAutoAdd\\Compare-Downloaded-Mods\\interleaved_text.txt'
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(interleaved_text)

print("Interleaved text has been saved to:", output_path)
