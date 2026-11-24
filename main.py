import os

TEXT = "Approved. I read every line, understood none of it, but it passes \u2014 and so, eventually, will we."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
