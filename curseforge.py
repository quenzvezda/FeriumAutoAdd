import subprocess
import time

data_file = "curseforge.txt"
api_key = "$2a$10$sI.yRk4h4R49XYF94IIijOrO4i3W3dAFZ4ssOlNE10GYrDhc2j8K."

with open(data_file, "r") as file:
    data_list = file.read().splitlines()

for data in data_list:
    # command = f'ferium --curseforge-api-key "{api_key}" add {data}'
    command = f'ferium add {data}' #without api key
    print(command)
    subprocess.run(command, shell=True)