import cv2, os, time
import numpy as np

class HoughImage():
    def __init__(self, filename=None, resize=False):
        self.img = cv2.imread(filename)

        if resize:
            self.img = cv2.resize(self.img,dsize=(0,0),fx=resize,fy=resize)

        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]

    def detect(self, blurValue=5, dp=1, minDist=100, cany_max=200,box_padding=12):

        if blurValue % 2 == 0:
            blurValue += 1
        
        if dp == 0:
            dp += 1
        
        if minDist == 0:
            minDist += 1
        
        if cany_max == 0:
            cany_max += 1

        self.blur = cv2.GaussianBlur(self.gray, (blurValue,blurValue), 0)

        circles = cv2.HoughCircles(self.blur, cv2.HOUGH_GRADIENT, dp, minDist, None, cany_max)
        box_points = []

        if circles is not None:
            circles = np.uint16(np.around(circles))
            count = 0

            for i in circles[0,:]:
                padding = int(i[2] * box_padding/10.)
                top = (i[0]-padding, i[1]-padding)
                bottom = (i[0]+padding, i[1]+padding)

                box_points.append([round(i[0]/self.width,6),round(i[1]/self.height,6),round(padding*2/self.width,6),round(padding*2/self.height,6)])
                
                # select box drow
                cv2.rectangle(self.img,top,bottom, (255, 0, 0), 2)
                
                # center point
                cv2.circle(self.img, (i[0], i[1]), 2, (0,0,255), 5)
                count += 1
            print(count)
        return self.img, box_points

def imageshow(filename=None):
    window_name = str(filename)
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winname=window_name, width=960, height=960)

    cv2.createTrackbar('blur',window_name,5,50,lambda pos:pos)
    cv2.createTrackbar('dp',window_name,11,20,lambda pos:pos)
    cv2.createTrackbar('minDist',window_name,100,200,lambda pos:pos)
    cv2.createTrackbar('cany_max',window_name,200,500,lambda pos:pos)
    cv2.createTrackbar('img_resize',window_name,7,10,lambda pos:pos)
    cv2.createTrackbar('box_padding',window_name,2,10,lambda pos:pos)

    while True:
        blur = cv2.getTrackbarPos('blur',window_name)
        dp = cv2.getTrackbarPos('dp',window_name)/10
        minDist = cv2.getTrackbarPos('minDist',window_name)
        cany_max = cv2.getTrackbarPos('cany_max',window_name)
        resize = cv2.getTrackbarPos('img_resize',window_name)/10.
        box_padding = cv2.getTrackbarPos('box_padding',window_name)+10

        image = HoughImage(filename,resize)

        detect, box = image.detect(blur, dp, minDist, cany_max,box_padding)

        cv2.imshow(window_name,detect)

        input_key = cv2.waitKey(1)

        if input_key == 13:
            break

        if input_key == ord('d'):
            os.replace(filename,'./trash/'+filename)
            break

        time.sleep(0.1)
    cv2.destroyAllWindows()

    return box