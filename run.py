from detect_coin import imageshow
import argparse, os, glob

parser = argparse.ArgumentParser(description="폴더 이름을 입력해주세요")
parser.add_argument('-fo','--folder',type=str, help='폴더 이름을 지정해주세요')
parser.add_argument('-fi','--file',type=str, help='파일 이름을 지정해주세요')
args = parser.parse_args()

foldname = args.folder
filename = args.file

if (foldname == None) & (filename == None):
    raise Exception("빈 값을 입력하셨습니다")

elif (foldname == None):
    filelist = [filename]

else:
    os.chdir(foldname)
    filelist=glob.glob('*')

def filtering(n):
    if n < 0:
        n = 0

    if n > 1:
        n = 1
    
    return n

try:
    os.makedirs("cooTXT")
    os.makedirs("trash")
except FileExistsError:
    pass

for name in filelist:
    if os.path.isdir(name):
        continue
    box_list = imageshow(filename=name)

    f = open(f"./cooTXT/{name.replace('.','_')}.txt",'w')

    for box in box_list:
        f.write("{} {} {} {}\n".format(*list(map(filtering,box))))
    f.close()