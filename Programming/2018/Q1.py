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
    print(f"pixel_cnt : {pixel_cnt}")
    for i in tqdm(range(100, len(clean_digits))):
        if pixel_cnt % (i*3) != 0:
            continue
        img_array = np.asarray(clean_digits, dtype=np.uint8).reshape([i, -1, 3])
        # print(img_array[0,0,:])
        # break
        should_show = True
        if np.all(img_array[:, -1] == 255):
            for j in range(img_array.shape[1]-1):
                if np.all(img_array[:, j] == 255):
                    should_show = False
            if should_show:
                plt.imshow(img_array)
                plt.show()
                print(img_array.shape)
            should_show = True