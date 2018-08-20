import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
with open('image1.txt','r') as f:
    digits = f.read().replace('\n', ' ').split(' ') #replace end of line with space, just to deal with shitty line ending
    clean_digits = []
    for i, d in enumerate(digits):
        if int(d) is not None:
         clean_digits.append(int(d))
pixel_cnt = len(clean_digits)
img = np.asarray(clean_digits, dtype=np.float).reshape([800, 1200, 3])
intensity = img[...,0]**2 + img[...,1]**2 + img[...,2]**2
height, width = intensity.shape
# original_intensity = intensity.copy()
intensity_flat = intensity.flatten()
print(f'min {intensity.min()}, max {intensity.max()}')
sort_idx = np.argsort(intensity_flat, kind='mergesort')

n = int(input('input n'))
assert n is not None, 'is not integer'
assert n%2 == 0, 'is not even'
assert n//2 < len(sort_idx)
index = sort_idx[n//2]

print(f'pixel value {img[index//width, index%width, :]}, index : {index}, intensity {intensity_flat[index]}, {(img[index//width, index%width, :]**2).sum()}')
    


