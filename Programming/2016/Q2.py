import numpy as np
with open('out1.txt', 'r') as f:
    lines = f.readlines()
    image = []
    for line in lines:
        _line = line[:-1]
        # print(_line)
        image_line = []
        for char in _line:
            if char is not ' ':
                image_line.append(1)
            else:
                image_line.append(0)
        image.append(np.asarray(image_line))
    image = np.asarray(image)
    print(image.shape)
    num_digits = 0
    indices = []
    for col in range(image.shape[1]):
        if all(image[:,col] == 0):
            num_digits += 1
            indices.append(col)
    # print(f'num_digits {num_digits}')
    indices.append(image.shape[1])
    extracted_digits= []
    for index in range(len(indices)):
        previous_index = indices[index - 1] + 1  if index > 0 else 0
        current_index = indices[index]
        # print(f'banan {current_index} {previous_index}')
        # print(image[:,previous_index:current_index])
        extracted_digits.append( image[:,previous_index:current_index].copy())
        
zero = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
one = [[1],[1],[1],[1],[1]]
two = [[1,1,1,1],[0,0,0,1],[1,1,1,1],[1,0,0,0],[1,1,1,1]]
three = [[1,1,1,1],[0,0,0,1],[1,1,1,1],[0,0,0,1],[1,1,1,1]]
four = [[1,0,0,1],[1,0,0,1],[1,1,1,1],[0,0,0,1],[0,0,0,1]]
five = [[1,1,1,1],[1,0,0,0],[1,1,1,1],[0,0,0,1],[1,1,1,1]]
six = [[1,0,0,0],[1,0,0,0],[1,1,1,1],[1,0,0,1],[1,1,1,1]]
seven = [[1,1,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
eight = [[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,1,1,1]]
nine = [[1,1,1,1],[1,0,0,1],[1,1,1,1],[0,0,0,1],[0,0,0,1]]
symbols = [zero, one, two, three, four, five, six, seven, eight, nine]
_symbols = []
for s in symbols:
    _symbols.append(np.asarray(s))
symbols = _symbols
for digit in extracted_digits:
    for i,s in enumerate(symbols):
        if  np.all(s == digit):
            print(i)

# print(f'Result : \n{result}')

