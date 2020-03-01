import os
import pathlib


path = pathlib.Path().absolute()
files = []
for root, dir, f in os.walk(path):
    for file in f:
        if file.endswith(".vtt"):
            files.append(os.path.join(root, file))
for file in files:
    with open(file, "r", encoding="utf8") as file_vtt:
        data = file_vtt.read()
        data = data.replace(".", ",")

    with open(file.replace(".vtt", ".srt"), "wa") as fout:
        print(data[12:], file=fout)
    print("{} is done".format(file))





