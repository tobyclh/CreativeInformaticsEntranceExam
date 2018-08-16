import numpy as np
zero =  [['*','*','*','*'],['|',' ',' ','|'],['*',' ',' ','*'],['|',' ',' ','|'],['*','*','*','*']]
one =   [['*'],['|'],['*'],['|'],['*']]
two =   [['*','*','*','*'],[' ',' ',' ','|'],['*','*','*','*'],['|',' ',' ',' '],['*','*','*','*']]
three = [['*','*','*','*'],[' ',' ',' ','|'],['*','*','*','*'],[' ',' ',' ','|'],['*','*','*','*']]
four =  [['*',' ',' ','*'],['|',' ',' ','|'],['*','*','*','*'],[' ',' ',' ','|'],[' ',' ',' ','*']]
five =  [['*','*','*','*'],['|',' ',' ',' '],['*','*','*','*'],[' ',' ',' ','|'],['*','*','*','*']]
six =   [['*',' ',' ',' '],['|',' ',' ',' '],['*','*','*','*'],['|',' ',' ','|'],['*','*','*','*']]
seven = [['*','*','*','*'],[' ',' ',' ','|'],[' ',' ',' ','|'],[' ',' ',' ','|'],[' ',' ',' ','|']]
eight = [['*','*','*','*'],['|',' ',' ','|'],['*','*','*','*'],['|',' ',' ','|'],['*','*','*','*']]
nine =  [['*','*','*','*'],['|',' ',' ','|'],['*','*','*','*'],[' ',' ',' ','|'],[' ',' ',' ','*']]

symbols = [zero, one, two, three, four, five, six, seven, eight, nine]

    
a = []
for s in symbols:
    a.append(np.asarray(s))
    # print(a[0].dtype)

print('Input integer : ')
banana = input()
# print(f'Your integer : {banana}')

splitted = banana.split(' ')
number = splitted[0]


horizontal_offset = []
vertical_offset = []
for i, digit in enumerate(splitted): 
    if i == 0: 
        horizontal_offset.append(0)
        continue
    if i%2 == 1:
        vertical_offset.append(int(digit))
    if i%2 == 0:
        horizontal_offset.append(int(digit))
assert len(vertical_offset) == len(horizontal_offset) == len(number)
width = np.asarray(horizontal_offset).sum()
width += np.array([a[int(d)].shape[1] for d in number]).sum()
width += len(number)-1 #divider
canvas = np.full([np.asarray(vertical_offset).max()+5, width], ' ', dtype=object)

h_pointer = 0
for digit, v_offset, h_offset in zip(number, vertical_offset, horizontal_offset):
    h_pointer += h_offset
    pic = a[int(digit)]
    print(pic.shape)
    # print(canvas[v_offset:v_offset+pic.shape[0], h_pointer:h_pointer+pic.shape[1]].shape)
    canvas[v_offset:v_offset+pic.shape[0], h_pointer:h_pointer+pic.shape[1]] = pic
    h_pointer += pic.shape[1]
    h_pointer += 1
# print(f'Canvas \n {canvas}')

result = canvas
with open('out1.txt', 'w') as f:
    for row in range(result.shape[0]):
        text_in_line = ''
        for pixel in result[row,:]:
            # if pixel == 0 or pixel == '0':
            #     text_in_line += ' '
            # else:
            text_in_line += pixel
        print(text_in_line)
        f.write(text_in_line + '\n')
# print(f'Result : \n{result}')

