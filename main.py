import cv2
from IPython.display import Image, display
import os
import glob

# 画像読み込み
data_path = glob.glob("datasets/*.jpg")
template = cv2.imread("tmp.jpg")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
tmp_h, tmp_w = template.shape[:2]
images = []
for filename in data_path:
    with open(filename, 'r') as input:
        img = cv2.imread(filename)
        base_h, base_w = img.shape[:2]
        scale = ((tmp_h * tmp_w) / (base_h * base_w))**0.5
        img = cv2.resize(img, (int(base_w * scale), int(base_h * scale)))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        images.append(img)

# テンプレートマッチング
for img in images:
    type = cv2.AKAZE_create()
    kp1, desc1 = type.detectAndCompute(template, None)
    kp2, desc2 = type.detectAndCompute(img, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(desc1, desc2, k=2)
    good_matches = []
    dist = []
    thresh = 0.7
    for first, second in matches:
        if first.distance < second.distance * thresh:
            good_matches.append(first)
            dist.append(first.distance)
    if len(dist) == 0:
        print("Zero division error!")
        ret = 10000
    else:
        ret = sum(dist) / len(dist)
    dst = cv2.drawMatches(img, kp1, template, kp2, good_matches, None)
    print(len(dist),ret)