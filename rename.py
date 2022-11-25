import os, glob

os.chdir("train/100/")

filelist=glob.glob("*")

for i, file in enumerate(filelist):
    _, ext = os.path.splitext(file)
    number = str(i).zfill(3)
    os.rename(file, f'{number}_KR_100 Won{ext}')