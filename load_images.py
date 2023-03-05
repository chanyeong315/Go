import os
import shutil
import tempfile
import matplotlib.pyplot as plt
import torch
import numpy as np
import PIL


data_dir = "C:/Users/고찬영/OneDrive - postech.ac.kr/바탕 화면/Dataset_BUSI/Dataset_BUSI_with_GT" #이미지 폴더 경로

class_names = sorted(x for x in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, x))) # 폴더 이름 읽어서 class_names에
num_class = len(class_names) #class 갯수
image_files = [ # 각 class의 이미지 불러오기
    [os.path.join(data_dir, class_names[i], x) for x in os.listdir(os.path.join(data_dir, class_names[i]))]
    for i in range(num_class)
]
num_each = [len(image_files[i]) for i in range(num_class)] # 각 class의 이미지 갯수를 num_each에
image_files_list = [] # 전체 class들을 image_files_list로 묶음
image_class = [] # 전체 image를 image_class로 묶음
for i in range(num_class):
    image_files_list.extend(image_files[i])
    image_class.extend([i] * num_each[i])
num_total = len(image_class) # 총 image 갯수
image_width, image_height = PIL.Image.open(image_files_list[0]).size # image size 계산 -> image_width, image_height

print(f"Total image count: {num_total}") # 총 image 갯수
print(f"Image dimensions: {image_width} x {image_height}") # image dimension
print(f"Label names: {class_names}") # class 이름
print(f"Label counts: {num_each}") # 각 class의 image 갯수

# image 3*3개 랜덤하게 출력
plt.subplots(3, 3, figsize=(8, 8))
for i, k in enumerate(np.random.randint(num_total, size=9)):
    im = PIL.Image.open(image_files_list[k])
    arr = np.array(im)
    plt.subplot(3, 3, i + 1)
    plt.xlabel(class_names[image_class[k]])
    plt.imshow(arr, cmap="gray", vmin=0, vmax=255)
plt.tight_layout()
plt.show()