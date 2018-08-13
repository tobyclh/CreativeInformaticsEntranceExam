import numpy as np
with open('array.txt') as f:
    line = f.read().replace('\n', ' ') #replace end of line with space, just to deal with shitty line ending
    if '.' in line:
        line = line.split('.')[0] #remove everything else after full stop
    rows = line.rstrip().split(',')
    current_line, processed_lines = [], []
    for row in rows:
        elements = row.split(' ')
        for element in elements:
            if element is '' or element is None:
                print(f'Cannot decode element : {element}')
            else:
                e = float(element)
                current_line.append(e)
        processed_lines.append(current_line.copy())
        current_line.clear()

array = np.asarray(processed_lines)
print(array.shape)
print(array)