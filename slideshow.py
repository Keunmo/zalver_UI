import glob
import os
import cv2
from cv2 import *

def slideshow():
    # img_files = glob.glob('./imgs/*.jpg')
    file_list = os.listdir('./imgs')
    img_files = [os.path.join(os.getcwd(), 'imgs', file) for file in file_list if file.endswith('.jpg')]
    img_files.sort()
    for f in img_files:
        print(f)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cnt = len(img_files)
    idx = 0
    while True:
        img = cv2.imread(img_files[idx])

        if img is None: # 이미지가 없는 경우
            print('Image load failed!')
            break

        img = cv2.resize(img, dsize=(3072, 1920), interpolation=cv2.INTER_LINEAR)

        cv2.imshow('image', img)
        if cv2.waitKey(1000) >= 0: # 1초 동안 사진보여주는데 만약에 키보드 입력이 있으면 종료
            break

        # 사진을 다 보면 첫번째 사진으로 돌아감
        idx += 1
        if idx >= cnt:
            idx = 0

    # cv2.destroyAllWindows()

if __name__ == '__main__':
    slideshow()