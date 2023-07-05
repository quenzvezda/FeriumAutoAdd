import subprocess

data_file = "modrinth.txt"

with open(data_file, "r") as file:
    data_list = file.read().splitlines()

for data in data_list:
    command = f"ferium-v2 add {data} --dont-check-game-version"
    print(command)
    subprocess.run(command, shell=True)