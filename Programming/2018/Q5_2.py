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
img = np.asarray(clean_digits, dtype=np.uint8).reshape([400, 400, 3])
plt.imshow(img)#.astype(np.uint8))
plt.show()
img = img.astype(np.float)

intensity = img[...,0]**2 + img[...,1]**2 + img[...,2]**2
height, width = intensity.shape
# original_intensity = intensity.copy()
intensity_flat = intensity.flatten()
# print(f'min {intensity.min()}, max {intensity.max()}')
sort_idx = np.argsort(intensity_flat, kind='mergesort')
n = 400*400
k = 2#int(input('input k'))
centroid_idx = [0, 1]
assert n is not None, 'is not integer'
# assert n%2 == 0, 'is not even'
assert n%k == 0
assert n//2 < len(sort_idx)
pixel_val = []
for _ in range(10):
    for i in range(k):
        index = sort_idx[int(n*i/k)]
        pixel_val.append(img[index//width, index%width, :])
    current_distance = np.ones([400, 400])*5000
    clusters = np.ones([400, 400])*-1
    for i, pixel in enumerate(pixel_val):
        distance = np.abs(img - pixel).sum(-1)
        # print(f'_distance :{distance.mean()}')        
        clusters[distance <= current_distance] = i
        current_distance[distance < current_distance] = distance[distance < current_distance]
        # print(clusters)
    # print(f'Mean distance :{current_distance.mean()}')
    prevois_pixel_val = pixel_val.copy()
    # print(f'cluster :{clusters}')
    pixel_val = []
    for cluster_idx in range(k):
        pixels = img[clusters == cluster_idx,:]
        if len(pixels) != 0:
            color = pixels.mean(0)
            pixel_val.append(color.astype(np.int))
        else:
            pixel_val.append(prevois_pixel_val[cluster_idx])

for c in centroid_idx:
    print(f'Centroid Index {c}: {pixel_val[c]}')
    




