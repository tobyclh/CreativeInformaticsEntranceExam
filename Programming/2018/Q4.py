import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
with open('image2.txt','r') as f:
    digits = f.read().replace('\n', ' ').split(' ') #replace end of line with space, just to deal with shitty line ending
    clean_digits = []
    for i, d in enumerate(digits):
        if int(d) is not None:
         clean_digits.append(int(d))
pixel_cnt = len(clean_digits)
img = np.asarray(clean_digits, dtype=np.float).reshape([400, 400, 3])
intensity = img[...,0]**2 + img[...,1]**2 + img[...,2]**2
height, width = intensity.shape
# original_intensity = intensity.copy()
intensity_flat = intensity.flatten()
print(f'min {intensity.min()}, max {intensity.max()}')
sort_idx = np.argsort(intensity_flat, kind='mergesort')

n = 160000#int(input('input n'))
k = int(input('input k'))
assert n is not None, 'is not integer'
# assert n%2 == 0, 'is not even'
assert n%k == 0
# assert n//2 < len(sort_idx)
for i in range(k):
    index = sort_idx[int(n*i/k)]
    print(f'pixel value {img[index//width, index%width, :]}, index : {index}, intensity {intensity_flat[index]}, {(img[index//width, index%width, :]**2).sum()}')
    


