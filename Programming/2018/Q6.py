import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
with open('image2.txt', 'r') as f:
    # replace end of line with space, just to deal with shitty line ending
    digits = f.read().replace('\n', ' ').split(' ')
    clean_digits = []
    for i, d in enumerate(digits):
        if int(d) is not None:
            clean_digits.append(int(d))
pixel_cnt = len(clean_digits)
img = np.asarray(clean_digits, dtype=np.uint8).reshape([400, 400, 3])
# plt.imshow(img.astype(np.uint8))
# plt.show()
img = img.astype(np.float)

intensity = img[..., 0]**2 + img[..., 1]**2 + img[..., 2]**2
height, width = intensity.shape
# original_intensity = intensity.copy()
intensity_flat = intensity.flatten()
print(f'min {intensity.min()}, max {intensity.max()}')
sort_idx = np.argsort(intensity_flat, kind='mergesort')

n = 400*400
k = 32  # int(input('input k'))
# centroid_idx = [40, 80, 120]
assert n is not None, 'is not integer'
# assert n%2 == 0, 'is not even'
assert n % k == 0
assert n//2 < len(sort_idx)
pixel_val = []
for _ in range(10):
    for i in range(k):
        index = sort_idx[int(n*i/k)]
        pixel_val.append(img[index//width, index % width, :])
    current_distance = np.ones([400, 400])*5000
    clusters = np.ones([400, 400])*-1
    for i, pixel in enumerate(pixel_val):
        distance = np.abs(img - pixel).sum(-1)
        clusters[distance <= current_distance] = i
        current_distance[distance <
                         current_distance] = distance[distance < current_distance]
        # print(clusters)
    print(f'Mean distance :{current_distance.mean()}')
    # print(f'cluster :{clusters}')
    pixel_val = []
    for cluster_idx in range(k):
        pixel_val.append(
            img[clusters == cluster_idx, :].mean(0).astype(np.int))
# for c in centroid_idx:
#     print(f'Centroid Index {c}: {pixel_val[c]}')

img_clone = img.copy()
for cluster_idx in range(k):
    print(img_clone)
    img_clone[clusters == cluster_idx,
              :] = pixel_val[cluster_idx].astype(np.uint8)
img_clone = img_clone.astype(np.uint8)
plt.imshow(img_clone)
plt.show()

from skimage.io import imsave
imsave('image.tif', img_clone)


header = [77, 77, 0, 42, 0, 0, 0, 8, 0, 7, 1, 0, 0, 4, 0, 0,
          0, 1, 0, 0, 0, 0, 1, 1, 0, 4, 0, 0, 0, 1, 0, 0, 
          0, 0, 1, 2, 0, 3, 0, 0, 0, 3, 0, 0, 0, 98, 1, 6, 
          0, 3, 0, 0, 0, 1, 0, 2, 0, 0, 1, 17, 0, 4, 0, 0, 
          0, 1, 0, 0, 0, 104, 1, 21, 0, 3, 0, 0, 0, 1, 0, 3, 
          0, 0, 1, 23, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 
          0, 0, 8, 0, 8, 0, 8]
with open('_image.tif', 'wb') as f:
    for i, h in enumerate(header):       
        if i not in [18, 19, 20, 21, 30, 31, 32, 33, 93, 92, 91, 90]:
            f.write(int.to_bytes(h, 1, byteorder='big'))
        else:
            if i == 18:
                # print(f'a {len(int.to_bytes(width))}')
                f.write(int.to_bytes(width, 4, byteorder='big'))
            elif i == 30:
                f.write(int.to_bytes(height, 4, byteorder='big'))
            elif i == 90:
                f.write(int.to_bytes(width*height*3, 4, byteorder='big'))
    for j in range(height):
        for i in range(width):
            r,g,b = img[i, j,0], img[i, j,1], img[i, j,2]
            f.write(int.to_bytes(int(r), 1, byteorder='big'))
            f.write(int.to_bytes(int(g), 1, byteorder='big'))
            f.write(int.to_bytes(int(b), 1, byteorder='big'))