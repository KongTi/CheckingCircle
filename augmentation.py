import albumentations as A
import cv2, glob, os

filelist = glob.glob("*")

number = 0 # 3은 transform1 변경 -> 끝나고 다시 변경

transform = A.Compose([
    A.Rotate(limit=[90*(number+1),90*(number+1)],rotate_method="largest_box",border_mode=cv2.BORDER_CONSTANT,p=1)
    ], bbox_params = A.BboxParams(format="yolo"))

transform1 = A.Compose([
    A.RandomBrightnessContrast(brightness_limit=(-0.2, 0.2), contrast_limit=(-0.2, 0.2), p=1),
    A.CLAHE(p=1),
    A.OpticalDistortion(p=0.5),
    A.RandomRotate90(p=0.5),
    A.GaussNoise(p=0.5, var_limit=(100, 200))
    ], bbox_params = A.BboxParams(format="yolo"))

transform2 = A.Compose([
    A.PadIfNeeded(2000,2000,border_mode=cv2.BORDER_REPLICATE, p=1)

    ], bbox_params = A.BboxParams(format="yolo"))

def savefig(file):
    boxes = []
    image = cv2.imread(file)

    filename, _ = os.path.splitext(file)

    with open(f'./cooTXT/{filename}.txt','r') as txt:
        for line in txt.readlines():
            cls,center_x,center_y,width,height = list(map(float,line.strip().split(" ")))

            x_min = center_x - width/2; x_max = center_x + width/2
            y_min = center_y - height/2; y_max = center_y + height/2

            if x_min < 0:
                width = center_x*2
            
            elif x_max > 1:
                width = (1 - center_x)*2

            if y_min < 0:
                height = center_y*2

            elif y_max > 1:
                height = (1 - center_y)*2

            axis = [center_x,center_y,width,height,cls]
            boxes.append(axis)

    transformed = transform2(image=image,bboxes=boxes)
    transformed_image = transformed['image']
    transformed_bboxes = transformed['bboxes']

    cv2.imwrite(f"./trash/{number}{file}",transformed_image)

    f = open(f"./trash/cooTXT/{number}{filename}.txt",'w')

    for box in transformed_bboxes:
        f.write(f"{int(box[-1])} {box[0]} {box[1]} {box[2]} {box[3]}\n")
    f.close()

for file in filelist:
    if os.path.isdir(file):
        continue

    savefig(file)