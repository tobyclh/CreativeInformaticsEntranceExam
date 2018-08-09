import numpy as np
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
a = []
for s in symbols:
    a.append(np.asarray(s))

print('Input integer : ')
banana = input()
print(f'Your integer : {banana}')
blank = np.asarray([[0],[0],[0],[0],[0]])
result = blank.copy()
for digit in banana: 
    pic = a[int(digit)]
    result = np.concatenate([result, pic], axis=1)
    result = np.concatenate([result, blank], axis=1)
result = result[:, 1:-1]
with open('out1.txt', 'w') as f:
    for row in range(result.shape[0]):
        text_in_line = ''
        if row%2 == 0:
            line_symbol = '*'
        else:
            line_symbol = '|'
        for pixel in result[row,:]:
            if pixel == 1:
                text_in_line += line_symbol
            else:
                text_in_line += ' '
        print(text_in_line)
        f.write(text_in_line + '\n')
# print(f'Result : \n{result}')

