import os, glob

nation = "KR"
price = "100"
name = "Won"
BorF = "B"

os.chdir(f'{nation}/{price}/{BorF}')

filelist=glob.glob("*")

for i, file in enumerate(filelist):
    _, ext = os.path.splitext(file)
    number = str(i).zfill(3)
    os.rename(file, f'{number}_{nation}_{price} {name}({BorF}){ext}')