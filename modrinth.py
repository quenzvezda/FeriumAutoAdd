import subprocess
import time

data_file = "modrinth.txt"

with open(data_file, "r") as file:
    data_list = file.read().splitlines()

for data in data_list:
    command = f"ferium add {data}"
    print(command)
    subprocess.run(command, shell=True)
    time.sleep(0.2)
    