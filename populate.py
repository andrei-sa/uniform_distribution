import os
import random

random.seed()
for i in range(2, 3000):
    date = random.randint(1, 365 * 3)
    os.system(f"echo \"{date}\" > distribution.txt")
    os.system("git add .")
    os.system(f"git commit --date \"{date} day ago\" -m \"Update distribution\"")
os.system("git push origin")
